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
            "password": generate_password_hash(request.form.get("password")),
            "age_category": request.form.get("age_category"),
            "gender": request.form.get("gender")
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


# you'll actually want to provide conditional checks on your Python functions to restrict these pages, but redirect users elsewhere if they're not validated.
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
            "date_updated": "Not Applicable", 
            "display": "Y"
        }
        mongo.db.reviews.insert_one(review)
        flash("Your review was successfully added")
        return redirect(url_for("get_reviews"))

    books = mongo.db.books.find().sort("book_title", 1)
    return render_template("add_review.html", books=books)


# no need to add conditional checks as it would be difficult for a user to guess the review id to get on to this page
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        book_title1 = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["book_title"]
        username1 = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["username"]
        date_created1 = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["date_created"]
        todaydate = datetime.today()
        submit = {
            # keep booktitle, username and datecreated the same as before
            "book_title": book_title1,
            "username": username1,
            "date_created": date_created1,
            # update recommend, stars, comment and dateupdated variables
            "recommend": request.form.get("recommend"),
            "stars": request.form.get("stars"),
            "comment": request.form.get("comment"),
            "date_updated": '{0:%d} {0:%B}, {0:%Y}'.format(todaydate, "day", "month", "year"), 
            "display": "Y"
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")
        return redirect(url_for("get_reviews"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    books = mongo.db.books.find().sort("book_title", 1)
    return render_template("edit_review.html", review=review, books=books)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    submit = {
            # keep booktitle, username, datecreated, dateupdated, recommend, stars and comment the same as before
            "book_title": mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["book_title"],
            "username": mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["username"],
            "date_created": mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["date_created"],
            "date_updated": mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["date_updated"],
            "recommend": mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["recommend"],
            "stars": mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["stars"],
            "comment": mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["comment"],
            # change display to N to not show on the website
            "display": "N"
        }
    mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)

    flash("Review Successfully Deleted")
    return redirect(url_for("get_reviews"))


# you'll actually want to provide conditional checks on your Python functions to restrict these pages, but redirect users elsewhere if they're not validated.
@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


# you'll actually want to provide conditional checks on your Python functions to restrict these pages, but redirect users elsewhere if they're not validated.
@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


# no need to add conditional checks as it would be difficult for a user to guess the genre id to get on to this page
@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "book_title": request.form.get("book_title"),
            "genre_name": request.form.get("genre_name"),
            "author": request.form.get("author")
        }
        mongo.db.books.insert_one(book)
        flash("New Book Added")
        return redirect(url_for("get_reviews"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_book.html", genres=genres)


@app.route("/get_books")
def get_books():
    books = list(mongo.db.books.find().sort("book_title", 1))
    return render_template("books.html", books=books)


# no need to add conditional checks as it would be difficult for a user to guess the genre id to get on to this page
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            "book_title": request.form.get("book_title"),
            "genre_name": request.form.get("genre_name"),
            "author": request.form.get("author")
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Successfully Updated")
        return redirect(url_for("get_books"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book, genres=genres)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Book Successfully Deleted")
    return redirect(url_for("get_books"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # dont forget to change this to debug False prior to project
            # submission!
            debug=True)
