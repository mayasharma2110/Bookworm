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
    # create dictionary based on reviews in database
    averageRev1 = {}
    for book in books:
        # 1st value in number of reviews, 2nd is total number of stars from all reviews on the book
        # and 3rd number is average review to 1 decimal place
        averageRev1[book["book_title"]] = ["", "", ""]
    # get number of reviews and average review
    for book in books:
        # number of reviews starts at 0
        num1 = 0
        # total stars
        totalstars = 0
        for review in reviews:
            if review["book_title"] == book["book_title"] and review["display"] == "Y":
                num1 += 1
                totalstars += int(review["stars"])
                # totalStars = totalStars + int(review["stars"])
        averageRev1[book["book_title"]][0] = num1
        averageRev1[book["book_title"]][1] = totalstars
        # create average based on total and number of reviews
        if averageRev1[book["book_title"]][0] != 0:
            averageRev1[book["book_title"]][2] = round(averageRev1[book["book_title"]][1]/averageRev1[book["book_title"]][0], 1)
    return render_template("reviews.html", reviews=reviews, books=books,
                           genres=genres, users=users,
                        averageRev1=averageRev1)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    reviews = list(mongo.db.reviews.find())
    genres = list(mongo.db.genres.find())
    users = list(mongo.db.users.find())
    # create dictionary based on reviews in database
    averageRev1 = {}
    for book in books:
        # 1st value in number of reviews, 2nd is total number of stars from all reviews on the book
        # and 3rd number is average review to 1 decimal place
        averageRev1[book["book_title"]] = ["", "", ""]
    # get number of reviews and average review
    for book in books:
        # number of reviews starts at 0
        num1 = 0
        # total stars
        totalstars = 0
        for review in reviews:
            if review["book_title"] == book["book_title"] and review["display"] == "Y":
                num1 += 1
                totalstars += int(review["stars"])
                # totalStars = totalStars + int(review["stars"])
        averageRev1[book["book_title"]][0] = num1
        averageRev1[book["book_title"]][1] = totalstars
        # create average based on total and number of reviews
        if averageRev1[book["book_title"]][0] != 0:
            averageRev1[book["book_title"]][2] = round(averageRev1[book["book_title"]][1]/averageRev1[book["book_title"]][0], 1)
    return render_template("reviews.html", reviews=reviews, books=books,
                           genres=genres, users=users, 
                           averageRev1=averageRev1)


@app.route("/register", methods=["GET", "POST"])
def register():
    # POST method functionality
    if request.method == "POST":
        # check if username already exists in db
        existing_user= mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please choose something else")
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
        return redirect(url_for("get_reviews", username=session["user"]))
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
                        "get_reviews", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # get other details about the logged in user
    agecat = mongo.db.users.find_one(
        {"username": session["user"]})["age_category"]
    gender = mongo.db.users.find_one(
        {"username": session["user"]})["gender"]
    usercap = username.capitalize()
    # get all reviews 
    reviews = list(mongo.db.reviews.find())
    books = list(mongo.db.books.find())
    genres = list(mongo.db.genres.find())
    if session["user"]:
        return render_template("profile.html", username=username,
        usercap=usercap, agecat=agecat, gender=gender, reviews=reviews, books=books, genres=genres)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add conditional check so only logged in users can add a review
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
            # Used the code from https://www.w3schools.com/python/python_datetime.asp to help my get and format the date created/date updated variables,
            # for more information see the credits section of readme file.
            "date_created": '{0:%d} {0:%B}, {0:%Y}'.format(todaydate, "day", "month", "year"),
            "date_updated": "Not Applicable", 
            "display": "Y"
        }
        mongo.db.reviews.insert_one(review)
        flash("Your review was successfully added")
        return redirect(url_for("get_reviews"))

    if request.method == "GET":
    # check if user is logged in
        if session:
            books = mongo.db.books.find().sort("book_title", 1)
            return render_template("add_review.html", books=books)
        # if not logged in return to home page with text to prompt the user to log in
        else:
            flash("Sorry that did not work, you must be logged in to add a review!")
            return redirect(url_for("get_reviews"))


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
            # Used the code from https://www.w3schools.com/python/python_datetime.asp to help my get and format the date created/date updated variables,
            # for more information see the credits section of readme file.
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


# conditional check so only admin can access this page
@app.route("/get_genres")
def get_genres():
    # check if logged in
    if session:
        # if logged in check if logged in as admin
        if session["user"]=="admin":
            genres = list(mongo.db.genres.find().sort("genre_name", 1))
            return render_template("genres.html", genres=genres)
        # if not admin show warning flash message and redirect to home page
        else:
            flash("Sorry that did not work, you must be logged in as admin to manage genres!")
            return redirect(url_for("get_reviews"))
    # if not logged in show warning flash message and redirect to home page
    else:
        flash("Sorry that did not work, you must be logged in as admin to manage genres!")
        return redirect(url_for("get_reviews"))


# conditional check so only admin can access this page
@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name"), 
            "display": "Y"
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    if request.method == "GET":
        # check if logged in
        if session:
            # if logged in check if logged in as admin
            if session["user"]=="admin":
                return render_template("add_genre.html")
            # if not admin show warning flash message and redirect to home page
            else:
                flash("Sorry that did not work, you must be logged in as admin to add a genre!")
                return redirect(url_for("get_reviews"))
        # if not logged in show warning flash message and redirect to home page
        else:
            flash("Sorry that did not work, you must be logged in as admin to add a genre!")
            return redirect(url_for("get_reviews"))


# no need to add conditional checks as it would be difficult for a user to guess the genre id to get on to this page
@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name"),
            "display": "Y"
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genre Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    submit = {
            # keep genre_name the same as before
            "genre_name": mongo.db.genres.find_one({"_id": ObjectId(genre_id)})["genre_name"],
            # change display to N to not show on the website
            "display": "N"
        }
    mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


# conditional check so only logged in users can add a book
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "book_title": request.form.get("book_title"),
            "genre_name": request.form.get("genre_name"),
            "author": request.form.get("author"), 
            "display": "Y"
        }
        mongo.db.books.insert_one(book)
        flash("New Book Added")
        return redirect(url_for("get_reviews"))

    if request.method == "GET":
    # check if user is logged in
        if session:
            genres = mongo.db.genres.find().sort("genre_name", 1)
            return render_template("add_book.html", genres=genres)
        # if not logged in return to home page with text to prompt the user to log in
        else:
            flash("Sorry that did not work, you must be logged in to add a book!")
            return redirect(url_for("get_reviews"))


# conditional check so only admin can access this page
@app.route("/get_books")
def get_books():
    # check if logged in
    if session:
        # if logged in check if logged in as admin
        if session["user"]=="admin":
            books = list(mongo.db.books.find().sort("book_title", 1))
            return render_template("books.html", books=books)
        # if not admin show warning flash message and redirect to home page
        else:
            flash("Sorry that did not work, you must be logged in as admin to manage books!")
            return redirect(url_for("get_reviews"))
    # if not logged in show warning flash message and redirect to home page
    else:
        flash("Sorry that did not work, you must be logged in as admin to manage books!")
        return redirect(url_for("get_reviews"))


# no need to add conditional checks as it would be difficult for a user to guess the book id to get on to this page
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            "book_title": request.form.get("book_title"),
            "genre_name": request.form.get("genre_name"),
            "author": request.form.get("author"),
            "display": "Y"
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Successfully Updated")
        return redirect(url_for("get_books"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book, genres=genres)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    submit = {
            # keep title, author and genre the same as before
            "book_title": mongo.db.books.find_one({"_id": ObjectId(book_id)})["book_title"],
            "genre_name": mongo.db.books.find_one({"_id": ObjectId(book_id)})["genre_name"],
            "author": mongo.db.books.find_one({"_id": ObjectId(book_id)})["author"],
            # change display to N to not show on the website
            "display": "N"
        }
    mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
    flash("Book Successfully Deleted")
    return redirect(url_for("get_books"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # dont forget to change this to debug False prior to project
            # submission!
            debug=True)
