import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
    print("found env.py")
from datetime import datetime


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    books = list(mongo.db.books.find())
    genres = list(mongo.db.genres.find())
    users = list(mongo.db.users.find())
    # print(list(reviews))
    # print(list(books))
    # print(list(genres))
    # print(list(users))
    return render_template("reviews.html", reviews=reviews, books=books,
                           genres=genres, users=users)


@app.route("/register", methods=["GET","POST"])
def register():
    # POST method functionality
    if request.method == "POST":
        # check if username already exists in db
        existing_user= mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # else if no existing user in db with username
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("myreviews", username=session["user"]))
    # else, GET method functionality
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "myreviews", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/myreviews/<username>", methods=["GET", "POST"])
def myreviews(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("myreviews.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        todaydate = datetime.today()
        review = {
            "book_title": request.form.get("book_title"),
            "recommend": request.form.get("recommend"),
            "stars": request.form.get("stars"),
            "comment": request.form.get("comment"),
            "username": session["user"],
            "date_created": '{0:%d} {0:%B}, {0:%Y}'.format(todaydate, "day", "month", "year"),
            "date_updated": "Not Applicable"
        }
        mongo.db.reviews.insert_one(review)
        flash("Your review was successfully added")
        return redirect(url_for("get_reviews"))

    books = mongo.db.books.find().sort("book_title", 1)
    return render_template("add_review.html", books=books)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "book_title": request.form.get("book_title"),
            "recommend": request.form.get("recommend"),
            "stars": request.form.get("stars"),
            "comment": request.form.get("comment"),
            # "username": session["user"],
            # "date_created": "",
            "date_updated": '{0:%d} {0:%B}, {0:%Y}'.format(todaydate, "day", "month", "year")
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    books = mongo.db.books.find().sort("book_title", 1)
    return render_template("edit_review.html", review=review, books=books)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # dont forget to change this to debug False prior to project
            # submission!
            debug=True)
