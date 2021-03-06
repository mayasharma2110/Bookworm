# Bookworm

[Link to live project.](https://bookworm-maya.herokuapp.com/)

This is a website for a book review/recommendation site.  

It is aimed for those who are interested in getting book recommendaions based on author, genre or trying something completely new, users can also help others by providing reviews of books they have read themselves. 

## Table of Contents

* [UX](#ux)
  * [User Stories](#user-stories)
    * [First Time Visitor Goals](#first-time-visitor-goals)
    * [Returning Visitor Goals](#returning-visitor-goals)
    * [Frequent User Goals](#frequent-user-goals)
  * [Strategy](#strategy)
    * [Business Goals](#business-goals)
    * [User Goals](#user-goals)
  * [Scope](#scope)
  * [Structure](#structure)
   * [Wireframes Navbar](#wireframes-navbar)
   * [Wireframes Home](#wireframes-home)
   * [Wireframes Login](#wireframes-login)
   * [Wireframes Register](#wireframes-register)
   * [Wireframes New and Edit Review](#wireframes-new-edit-review)
   * [Wireframes Manage Books](#wireframes-manage-books)
   * [Wireframes Add and Edit Book](#wireframes-add-edit-book)
   * [Wireframes Manage Genres](#wireframes-manage-genres)
   * [Wireframes Add and Edit Genre](#wireframes-add-edit-genre)
  * [Skeleton](#skeleton)
    * [Colours](#colours)
    * [Imagery](#imagery)
  * [Surface](#surface)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features Left to Implement](#features-left-to-inplement)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
  * [User Authentication Register](#user-authentication-register)
  * [User Authentication Log In](#user-authentication-log-in)
  * [User Authentication Log Out](#user-authentication-log-out)
  * [Home](#home)
  * [Add New Review](#add-new-review)
  * [Edit Review](#edit-review)
  * [Delete Review](#delete-review)
  * [Manage Books](#manage-books)
  * [Add Book](#add-book)
  * [Edit Book](#edit-book)
  * [Delete Book](#delete-book)
  * [Manage Genres](#manage-genres)
  * [Add Genre](#add-genre)
  * [Edit Genre](#edit-genre)
  * [Delete Genre](#delete-genre)
  * [Security](#security)
  * [Online Validation](#online-validation)
  * [Lighthouse Validation](#lighthouse-validation) 
  * [User Stories from the UX Section](#user-stories-from-the-ux-section)
* [Deployment](#deployment)
  * [Creation](#creation)
  * [Heroku](#heroku)
  * [Local Clone](#local-clone)
  * [Forking](#forking)
* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

## UX

### User Stories

#### First Time Visitor Goals

* As a first time user, I want to know the purpose of the site.

* As a first time user, I want to read reviews registered users have made.

* As a first time user, I want to be able to find a new book that I may like to read.

* As a first time user, I want to be able to be able to search in the reviews for a certain book title or author.


#### Returning Visitor Goals

* As a returning user, I have similar needs of a first time user.

* As a returning user, I want to be able to register and login as myself.

* As a returning user, I want to be able to add new books to the database/site.

* As a returning user, I want to be able to add my own reviews to the site, I would also like to update or delete my own reviews.

#### Frequent User Goals

* As a frequent user, I have similar needs of a first time and returning user.

### Strategy

#### Business goals

* As a business owner, I want to help users find new books/authors they may enjoy.

* As a business owner, I want to be able to manage the list of books and genres that are displayed as options to users of the site when adding a new review or book to the database/site.

* As a business owner, I want to be able to manage the reviews and soft delete any that are deemed spam or unacceptable in some way, this will be a soft delete and will remain in the database but not be shown on the site to users.

#### User Goals

* To read reviews and gain information about new books/authors they may like.

* To help the community by providing reviews for books they have read.

* To have the ability to update or delete a review I have made.

### Scope

Key features to be included based on user stories are:

* Responsive website on mobile, tablet and laptop size devices.

* The home page will contain the reviews and a search bar for users to search for a book title or author. 

* The login page will contain a form for registered users to login.

* The register page will contain a form for new members to sign up and be part of the community.

* The new review page will contain a form which allows signed in users to create a new review for a book.

* The manage books page will contain a list of all current books in the database, this will be accessible to admin only.

* The manage genres page will contain a list of all current genres in the database, this will be accessible to admin only.

### Structure

All pages of the website will have a consistent navigation bar. The home, login and register links will be available to users who aren't yet registered and/or logged into the site. For non admin users when logged in this will show home, new review, add books and logout links. For admin users when logged in users this will show home, new review, manage books, manage genres and logout links. 

The website will use Materializecss grids to make the layout responsive to different devices and screen sizes.

* The home page will contain the reviews and a search bar for users to search for a book or author. Signed in users can update or delete their own reviews, this will only be a soft delete and the information will remain in the database but not be shown on the site to users. Admin are able to delete any review they deem spam or unacceptable in some way, this again will be a soft delete only.

* The login page will contain a form for registered users to login. This will ask for username and password, if either are incorrect this will be displayed ot the user and the site will ask them to try again. There will also be a logout link for logged in users to use.

* The register page will contain a form for new members to sign up and be part of the community. This will ask for users username, password, age category and gender. The site will check against the database to make sure there is no current user with such username and if so, will notify the user as such and to choose a different username instead. Age category and gender can be of use for users of the site when deciding on a new book/author based on demogrpahics of those who read such books/authors' work.

* The new review page will contain a form which allows signed in users to create a new review for a book. This will include a dropdown for the book that is being revewed, recommend yes/no field, start out of 5 field and review comment (free text field). Users will also be able to update/delete their own review and admin can delete any review.

* The manage books page will contain a list of all current books in the database. This will be accessible to admin only and allow them to view all books in the database and a links which allow them to a new book and update/delete an existing one. Users who are not admin and logged in will be able to add a new book to the database but not update or delete any existing ones.

* The manage genres page will contain a list of all current genres in the database. This will be accessible to admin only and allow them to view all genres in the database and a links which allow them to add a new genre and update/delete an existing one.

* For the setup of the database, using MongoDB, I decided on 4 collections based on above scope and structure: users, reviews, books and genres. 
  * The users collection would collect/store information about each registered user - mainly username (free text field) and password (free text field) but also age category (several options to pick from) and gender (3 options to pick from) as I thought this information on reader demographics could be useful to others who are reading reviews on books. This way they could see which demographic generally likes/dislikes certain books/authors.
  * The reviews collection would collect/store information whenever a review was made, updated or deleted. This would contain book_title (several options to pick from) of the review, recommend (yes or no), stars out of 5 (options 1 through 5), review comment (free text field), username of user who created the review (free text field), date created (DD MONTH YYYY format of system date), date updated (DD MONTH YYYY format of system date) and display (Y or N, Y by default and changes to N if a user/admin deletes the review).
  * The books collection would collect/store information whenever a book was added, updated or deleted. This would contain the book_title (linking to the reviews collection), author (free text field), genre name (free text field) and display (Y or N, Y by default and changes to N if the admin deletes the book).
  * The genres collection would collect/store information whenever a genre was added, updated or deleted. This would contain the genre_name (linking to the books collection) and display (Y or N, Y by default and changes to N if the admin deletes the genre).

### Skeleton

I used pen and paper to make the wireframes for this project. The website was designed to have 11 pages - Home, Login, Register, New Review, Edit Review, Manage Books, Add Book, Edit Book, Manage Genres, Add Genre and Edit Genre. The webiste also includes a logout link which logs out signed in users and takes them to the home page.

#### Wireframes Navbar

![Navbar Wireframes](static/wireframes/navbar.jpg)  

#### Wireframes Home

![Home Wireframes](static/wireframes/home.jpg)  

#### Wireframes Login

![Login Wireframes](static/wireframes/login.jpg) 

#### Wireframes Register

![Register Wireframes](static/wireframes/register.jpg) 

#### Wireframes New and Edit Review

![New and Edit Review Wireframes](static/wireframes/new_edit_review.jpg)  

#### Wireframes Manage Books

![Manage Books Wireframes](static/wireframes/manage_books.jpg) 

#### Wireframes Add and Edit Book

![Add and Edit Book Wireframes](static/wireframes/add_edit_book.jpg)  

#### Wireframes Manage Genres

![Manage Genres Wireframes](static/wireframes/manage_genres.jpg) 

#### Wireframes Add and Edit Genre

![Add and Edit Genre](static/wireframes/add_edit_genre.jpg)  

#### Wireframes Comments

Please note there are a few changes to the final site since the wireframes were made:

  * I added an image to the home/reviews page.
  * I added a profile page called "My reviews" to the site so logged in users can see the reviews they made easily, from here they can also update/delete the reviews they created.

### Surface

#### Colours
I noticed that the popular booksite [Waterstones](https://www.waterstones.com/) uses a common colour of teal, however I chose a main colour of green as I found this a good colour to represent nature/balance and is also calming. From [Adobe Color](https://color.adobe.com/create/color-wheel) I choose green (#00e676 green accent-3) as the main colour and this site helped me find the split complemantary colours of orange (#ef6c00 orange darken-3) and magenta (#ad1457 pink darken-3). For the navbar and headings text I chose a light (#b9f6ca green accent-1) and dark green (#1b5e20 green darken-4) and other text uses dark grey (#424242 grey darken-3).

#### Imagery
I picked an image of a person reading a book outdoors for the home page as I wanted to create a sense of relaxation and calm. Further information on this is given in the credits - media section of this readme.

## Features

### Existing Features

* The site is responsive on mobile, tablet and laptop size devices.

* The home page contains information of all genres, books and reviews from the database. Users can click on a book to see the reviews on it. With each book the average score out of 5 is displayed with the number of reviews in brackets. A user who created a review is able to edit or delete it when they are logged in. This page also includes a search function where users can search for a book based on its title or the author name. This page also has prompts for a user to add new books/reviews to the site to help it grow.

* The login page allows registered users to log in with their username and password.

* The register page allows unregistered users to register with the site by giving a username, their age category, their gender and choosing a password.

* The profile page allows logged in users to see the reviews they have made and also includes links to update/delete any reviews made my them. If they have made no reviews so far this is shown in text and users are prompted to add a review.

* The new review page allows logged in users to add a review for one of the books already in the database/site. They can say if they recommend it or not, give stars out of 5 and also a review comment to guide other users who view the site into picking new books/authors to read.

* The manage books page is restricted to admins only. It allows admin to view the current books and add a new book to the site, update a book or delete a book. Users who are not admin and who are logged in can also add new books but are not able to update or delete existing records. 

* Although a non admin user can add a book, I did not allow them to update or delete this as if they had already created a review for the book updating the book title later would cause the review to not show in the home page anymore.

* The manage genres page is restricted to admins only. It allows admin to view the current genres and add a new genre to the site, update a book or delete a genre.

* Before a user/admin deletes a review, book or genre there is defensive programming which will display additional buttons to check if a user/admin really wants to delete the review, book or genre. 

* When a user/admin deletes a review, book or genre this is a soft delete only and the information is kept in the database, but the variable "display" will change to "N" (for all reviews, books and genres this is automatically set to "Y" on creation) and therefore this information will not be presented on the site.

* There are security checks so a user cannot gain access to cetrain pages without being logged in or logged in as admin.
  * All users can access register, log in and home pages.
  * Logged in users also gain access to my reviews, add review and add book pages.
  * Admin users also gain access to manage books, manage genres and add genre pages.
  * There are no security checks for edit review, edit book and edit genre pages as these would require a user to guess the review/book/genre id (as in mongobd) and therefore are secure. For example, to edit a review the page would be something like ".../edit_review/613faa0a95b25ad59fd7731c".

### Features Left to Implement

* It would be nice to use some book API, for example [Google Books](https://developers.google.com/books/docs/v1/using), as this could help ensure the spelling of book titles and authors are correct when users add a new book to the site/database (and help avoid having duplicates of the same bok with various spellings of title/author). This could have the users enter a book they have using the ISBN number (usually found on the back of the book near the barcode) or if they do not have the book to hand, they could be prompted to google for its ISBN number or contact the site with the details so a person could manually add it to the site/database. 

* It would be nice to have a check when a user adds a new review to see if they have already made a review for that book - if yes, we could prompt them to edit this review instead.

* It would be nice to have a search function on the manage books page so admin check if a book exists in the database before adding a new one.

* It would be good to have the site collect a users date of birth when they register rather than collecting age category directly. The site could calculate their age at a given time using this date of birth and the system date to derive age and age category. This would be good for instances when a user's age and age category will change over time and it can be automaticaly updated when they make a review.

* If a book title is updated it would be good to automatically update the book_title variable in the reviews collection to make sure all the reviews should show correctly. Similarly, if a genre name is updated it would be good to automatically update the genre_name variable in the books collection to make sure all books should show correctly. 

* If a book was deleted this book and any reviews for it would not show on the site but would remain in the database. If a user had made a review for a book that was deleted in the future, it may be good to notify them of this.

## Technologies Used

* HTML - used to create the main content for the website.

* CSS - used to add style and colour to the content.

* [Materializecss](https://materializecss.com/)
  * Used to help make this website responsive for different devices and to create the collapsible navbar.
  * Used to make the cards on the home page reveal the review details for each book.
  * Used to help create the colours and style on the site. 
  * Used to validate user information in the add/edit review forms. 

* Javascript - used to help make the site responsive to the user's input - defensive programming before deleting a review, book or genre to check if the user is sure they want to proceed.

* jQuery - used to help make the site responsive to the user's input - defensive programming before deleting a review, book or genre to check if the user is sure they want to proceed.

* [MongoDB](https://www.mongodb.com/) used to create, store and update the data used in this site.

* [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/en/2.0.x/) - used to get data from the database in MongoDB to the live site.

* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - used to create the security on the site allowing users to register, log in and logout of their own profiles. It also helped make the user authentication more secure by converting the users password into a random string of letters/numbers before saving this in the database (using the generate_password_hash and check_password_hash functions). 

* [Gitpod](https://www.gitpod.io/) - used to write the code for the website.

* [GitHub](https://github.com/) - used to store the current and previous versions of the code. 

* [Heroku](https://www.heroku.com/) - used to host the live website.

* [Tinypng](https://tinypng.com/) - used to compress the images so they loaded quicker on the website.

## Testing

### User Authentication Register

Expected - When the user registers with a username that already exists in the database this will be shown to the user and they will be asked to pick another username.

Testing - Tested the feature by trying to register under an already created username.

Result - The feature acted as normally, and it did tell me the username was already taken and to choose another username.

Expected - When the user registers with a username that does not already exist in the database thier information will be added to the database (under users collection) and they will be taken back to the home page.

Testing - Tested the feature by registering with a username that did not already exist in the database. 

Result - This information was added to the database and I was taken to the ome page. The password variable was also converted to a random string of letters/numbers using [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/).

![Authentication](static/testing/testing-authentication.PNG)

### User Authentication Log In

Expected - When the user logs in with an incorrect username and/or password they are notified of this and the log in page is reloaded.

Testing - Tested the feature by trying to log in with the wrong password and also the wrong username.

Result - The feature acted as normally, and it did tell me the username and/or password was wrong and reloaded the log in page.

Expected - When the user logs in with the correct username and password and they will be taken to the home page and notified they logged in successfully.

Testing - Tested the feature logging in with the correct username and password.

Result - The feature acted as expected and it did let me know I logged in successfully and took me to the home page.

![Log in](static/testing/testing-login.PNG)

### User Authentication Log Out

Expected - When the user clicks to log out and they will be taken back to the home page and notified they logged out successfully.

Testing - Tested the feature logging out.

Result - The feature acted as expected and it did let me know I logged out successfully and took me to the home page.

### My Reviews

Expected - When the user clicks to edit a review they are taken to the edit_review page.

Testing - Tested the feature clicking on a review to edit.

Result - The feature acted as expected and it did take me to the edit review page.

Expected - When the user clicks to delete a review they are asked if they want to proceed, yes or no. I they click no the current page is reloaded. If they click yes, this review is soft deleted in the database (display changes from Y or N) and they are taken to the home page.

Testing - Tested the feature clicking on a review to delete and then no.

Result - The feature acted as expected and it did reload the current page.

Testing - Tested the feature clicking on a review to delete and then yes.

Result - The feature acted as expected and it did soft delete the review in the database and took me to the home page.

### Home

For each book i wanted to show the average review based on this, within python before loading the page I created a dictionary (called averageRev1) with each book_title and then this function loops throught all the books and reviews for each book to derive the number of reviews, total score and then the average score (out of 5). From this I also wanted the users to be prompted to add more reviews for each book and if no reviews for a certain book to be told this and prompted to add a first review, to do this I had to have a conditional check for the variable averageRev1[book.book_title][0] which was the number of reviews a book had and check if the value was 0 or not.

Expected - When the user adds some text to the search field the site refreshes the page and shows results relating to their search based on the collection books and variables bok_title and author.

Testing - Tested the feature by going doing a search.

Result - The feature did not act as expected and it gave me an error that averageRev1 was not defined. 

Fix - I noticed that when a user clicks search the python function /search was run and this did not include the dictionary averageRev1 that was derived and included in /get_reviews, once I corrected this by doing copying the relevant code from /get_reviews to /search this resolved the issue. I retested and the feature acted as expected and it refreshed the page and showed results relating to my search.

### Add New Review

This page has a drop down selection and only shows books in the database with display Y, additioanlly it has extra fields for users to say if they recommend a book or not, give a star rating out of 5 and enter a review comment. When they create a review, the date created variable is made using the system timedate and to get this variable in the right format I used the [w3schools](https://www.w3schools.com/python/python_datetime.asp) site to help me.

Expected - When the user clicks to add a review, they are taken to the add_review page.

Testing - Tested the feature by adding a review.

Result - The feature acted as expected and created the review in the database and showing it on the website.

![Add review](static/testing/new-review.PNG)

### Edit Review

Expected - When the user clicks to edit a review the fields recommend, stars and comment are updated in the database. Additionally, the date updated variable is changed from "Not Applicable" to the current date based on the system datetime.

Testing - Tested the feature by updating a review.

Result - The feature acted as expected however it overwrote the date created variable as "" rather than keeping as it was previously.

Fix - I extracted the date create variable from the database before updating the review and used this instead. Once the below code was added in the python file the function worked as expected.

> date_created1 = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})["date_created"]

![Edit review](static/testing/edit-review.PNG)

### Delete Review

Expected - When the user clicks to delete a review they are asked if they want to proceed, yes or no. I they click no the current page is reloaded. If they click yes, this review is soft deleted in the database (display changes from Y or N) and they are taken to the home page.

Testing - Tested the feature clicking on a review to delete and then no.

Result - The feature acted as expected and it did reload the current page.

Testing - Tested the feature clicking on a review to delete and then yes.

Result - The feature acted as expected and it did soft delete the review in the database and took me to the home page.

![Delete review](static/testing/delete-review.PNG)

### Manage Books

This shows all books with display Y in the database and allow includes links for admin to add a new book or update/delete any current books in the database. All links work as expected to add, edit or delete a book.

### Add Book

This page has a drop down selection and only shows genres in the database with display Y, additioanlly it has extra fields for the book title and author.

Expected - When the user clicks to add a book this is added to the database and they are taken to the home page.

Testing - Tested the feature by adding a new book.

Result - The feature acted as expected and created the book in the database and showing it on the website.

![Add book](static/testing/add-book.PNG)

### Edit Book

This page is similar to the add book page however it pre-populates the book name, author and genre as currently in the database.

![Edit book](static/testing/edit-book.PNG)

### Delete Book

Expected - When the user clicks to delete a book they are asked if they want to proceed, yes or no. I they click no the current page is reloaded. If they click yes, this book is soft deleted in the database (display changes from Y or N) and the current page is reloaded.

Testing - Tested the feature clicking on a book to delete and then no.

Result - The feature acted as expected and it did reload the current page.

Testing - Tested the feature clicking on a book to delete and then yes.

Result - The feature acted as expected and it did soft delete the book in the database, and it reloaded the current page.

![Delete book](static/testing/delete-book.PNG)

### Manage Genres

This shows all genres with display Y in the database and allow includes links for admin to add a new genre or update/delete any current genres in the database. All links work as expected to add, edit or delete a genre.

### Add Genre

This page has a free text field allowing admins to create a new genre name.

Expected - When the user clicks to add a genre this is added to the database and they are taken to the manage genres.

Testing - Tested the feature by adding a new genre.

Result - The feature acted as expected and created the genre in the database and showing it on the website.

![Add genre](static/testing/add-genre.PNG)

### Edit Genre

This page is similar to the add genre page however it pre-populates the genre name as currently in the database.

![Edit genre](static/testing/edit-genre.PNG)

### Delete Genre

Expected - When the user clicks to delete a genre they are asked if they want to proceed, yes or no. I they click no the current page is reloaded. If they click yes, this genre is soft deleted in the database (display changes from Y or N) and the current page is reloaded.

Testing - Tested the feature clicking on a genre to delete and then no.

Result - The feature acted as expected and it did reload the current page.

Testing - Tested the feature clicking on a genre to delete and then yes.

Result - The feature acted as expected and it did soft delete the genre in the database and it reloaded the current page.

![Delete genre](static/testing/delete-genre.PNG)

### Security
* There a security checks so a user cannot gain access to cetrain pages without being logged in or logged in as admin.
  * If a user tries to access a page they are not allowed to some text will be shown like below. <br>
  Try and go to http://bookworm-maya.herokuapp.com/add_review before logging in and you will get the below warning: <br>
  ![Security](static/testing/security.PNG)
  Try and go to http://bookworm-maya.herokuapp.com/get_genres before logging in and you will get the below warning: <br>
  ![Security1](static/testing/security1.PNG)

### Online Validation

* I checked the website loads and responds as expected on Google Chrome and Microsoft Edge browsers. 

* Used chrome developer tools to check responsiveness on mobile, tablet and laptop devices.  
I also checked the website on my HP 15 inch laptop, Philips 20 inch monitor and Sony smartphone.

* Used the [w3c validator](https://validator.w3.org/) to validate my html (for all pages of the website) to check for no errors or warnings. For html there was 1 warning on all pages due to the section for flash messages (shown below).
  ![HTML warning](static/testing/html-warning.PNG) <br>
  There were additionally some extra errors/warnings due to the materializecss being used that the validator did not have access to (see below also). <br>
  ![Other HTML warnings](static/testing/other-html-warnings.png)

* Used the [jigsaw validator](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my style.css file to check for no errors or warnings. 
I did not validate css of the whole website as this included the imported materializecss files.

* Used [Jshint](https://jshint.com/) to validate my js files and ensure no warnings or errors.

* Used [PEP8 Online](http://pep8online.com/) to validate my python files and ensure no warnings or errors.

### Lighthouse Validation

I used [lighthouse](https://developers.google.com/web/tools/lighthouse) in chrome developer tools to check the websites performance in terms of 
performance, accessibility, best practises and SEO.
This was done for all pages of the website and for desktop devices only due to time.
The summary table below shows these metrics.

| Device | Page |  Performance | Accessibility  | Best Practises  | SEO |
|---|---|---|---|---|---|
| Desktop  |  Home | 100% | 97% | 93% | 100% |
| Desktop  |  Login | 99% | 96% | 93% | 100% |
| Desktop  |  Register | 100% | 84% | 100% | 100% |
| Desktop  |  Profile | 100% | 95% | 93% | 100% |
| Desktop  |  New Review | 100% | 84% | 93% | 100% |
| Desktop  |  Edit Review | 100% | 84% | 93% | 100% |
| Desktop  |  Add Book | 100% | 84% | 93% | 100% |
| Desktop  |  Manage Books | 100% | 95% | 93% | 100% |
| Desktop  |  Edit Book | 100% | 84% | 93% | 100% |
| Desktop  |  Manage Genres | 100% | 95% | 93% | 100% |
| Desktop  |  Add Genre | 100% | 96% | 93% | 100% |
| Desktop  |  Edit Genre | 100% | 96% | 93% | 100% |

Full reports can be found below:

* [Desktop Home](static/lighthouse/lighthouse-desktop-home.pdf)
* [Desktop Login](static/lighthouse/lighthouse-desktop-login.pdf)
* [Desktop Register](static/lighthouse/lighthouse-desktop-register.pdf)
* [Desktop Profile](static/lighthouse/lighthouse-desktop-profile.pdf)
* [Desktop New Review](static/lighthouse/lighthouse-desktop-add-review.pdf)
* [Desktop Edit Review](static/lighthouse/lighthouse-desktop-edit-review.pdf)
* [Desktop Add Book](static/lighthouse/lighthouse-desktop-add-book.pdf)
* [Desktop Manage Books](static/lighthouse/lighthouse-desktop-manage-books.pdf)
* [Desktop Edit Book](static/lighthouse/lighthouse-desktop-edit-book.pdf)
* [Desktop Manage Genres](static/lighthouse/lighthouse-desktop-manage-genres.pdf)
* [Desktop Add Genre](static/lighthouse/lighthouse-desktop-add-genre.pdf)
* [Desktop Edit Genre](static/lighthouse/lighthouse-desktop-edit-genre.pdf)

### User Stories from the UX Section

* First Time Visitor Goals  

  * As a first time user,  I want to know the purpose of the site.
    * The site has a clear title Bookworm which is a clear indication the site is about books.
    * There is an image of a person reading by a cliff side which also shows the site is to do with books.
    * Below the image there is text "All Reviews" and a search bar which shows the site will contain information about book reviews.

  * As a first time user,  I want to read reviews registered users have made.
    * When the home page is first loaded users can see the text "All Reviews" and are therefore encouraged to scroll down where they will see the list of genres and books. Each book has some text to tell the user to click to see the reviews.
    * Additioanlly, users can search near the top of the page based on a particular author or book title to narrow thier search.

  * As a first time user,  I want to be able to find a new book that I may like to read.
    * For each book the information of average score out of 5 is shown and also the number of reviews which can also help users pick a new book to read.
    * Users can read the reviews of certain books, authors or genres to get an idea of which books they may like. 
    * For each review the site also shows the age category and gender of the user who made the review, this can help others pick a book as they gain an idea of which books are liked/disliked by different demographics.
    
  * As a first time user, I want to be able to be able to search in the reviews for a certain book title or author.
    * There is a search bar below the image on the home screen with instructions for the user to search based on book title or author with search and reset buttons.

* Returning Visitor Goals

  * As a returning user, I have similar needs of a first time user.
    * See above section.

  * As a returning user, I want to be able to register and login as myself.
    * In the navbar there are clear links to log in and register.
    * The register page has clear instructions for each field on what is expected/allowed and each field is validated through the materializecss library.
    * The log in page allows registered users to log in and if the get the username/password wrong the log in page is reloaded and they are lotified ther attempt was unsuccessful.

  * As a returning user, I want to be able to add new books to the database/site.
    * Logged in users can see the Add Book link in the navbar.
    * Additionally, in the home page there are links to prompt the user to add a new book if there are no books in the database currently for a genre. 
    * The add book page has clear instructions for each field on what is expected/allowed and each field is validated through the materializecss library.
    * Once they have added a book they are notified that this was successful and taken to the home page.

  * As a returning user, I want to be able to add my own reviews to the site, I would also like to update or delete my own reviews.
    * Logged in users can see the My Reviews link in the navbar, from here they can see the current reviews they made. They can also add a review and also update/delete any existing reviews they made.
    * From the home page logged in users can see any reviews they made and next to them will have edit and delete buttons.
    * From the home page users are prompted to add a review for each book if they have read it.
    * The add review page has clear instructions for each field on what is expected/allowed and each field is validated through the materializecss library.
    * Once they have added a review they are notified that this was successful and taken to the home page.
    * There is also a conditonal check before they delete a review to check if are sure.

* Frequent User Goals
    
  * As a frequent user, I have similar needs of a first time and returning user.
    * See above sections.

* Business Goals

  * As a business owner, I want to help users find new books/authors they may enjoy.
    * See above sections for how the site helps users find new books/authors they may like.

  * As a business owner, I want to be able to manage the list of books and genres that are displayed as options to users of the site when adding a new review or book to the database/site.
    * From the navbar admin have access to the manage books and manage genre pages. These pages show all books/genres in the database with display "Y". They additionally have links allowing admin to add a new book/genre to the database or update/delete any existing books/genres.
    * There is also a conditonal check before they delete a book/genre to check if are sure.
    * When the books or genres collections in MongoDB are updated by admin this is automatically updated in pages such as add book (the selection of genre names will be updated dynamically) and add review (the selection of book names will be updated dynamically).

  * As a business owner, I want to be able to manage the reviews and soft delete any that are deemed spam or unacceptable in some way, this will be a soft delete and will remain in the database but not be shown on the site to users.
    * From the home page admin are able to view all reviews and delete a review made by themselves or any user.
    * There is also a conditonal check before they delete a review to check if are sure.
    * If they click delete and then yes they are notified that the review has been deleted and the home page is reloaded.
    * If they click delete and then no the home page is reloaded and the database is not updated.

## Deployment

### Creation

* All code was written in Gitpod and used [this template](https://github.com/Code-Institute-Org/gitpod-full-template) from Code Institute.
* Files were added to the staging area using "git add ."
* Files were committed to the local repository using "git commit -m 'commit message here'".
* Committed changes were pushed to the GitHub repository.

### Heroku

To deploy the project to a live website the below steps were followed:

* Go to Heroku.com and log in (if not registered you must create an account first).
* Make sure your project has a file specifying which applications are needed to run your site, use the below code to automatically generate this
> pip3 freeze --local > requirements.txt
* Also make sure you have a Procfile which tells Heroku which file runs the app (in our case it is app.py), use the below code to generate this. The Procfile may add a blank line which can cause issues so check and remove this if needed.
>  echo web: python app.py > Procfile (note that this has no extension)
* In Heroku click on create a new app. The Heroku app name must be unique and generally uses - instead of spaces and all lowercase letters. Then select the region closest to you and create app.
* To connect our app to Heroku we can setup an automatic deployment from our GitHub repo. Within your Heroku app go to the deployment tab and click on GitHub for the deployment method. Make sure your GitHub profile is displayed below and enter the repository name and search. Make sure your repo is displayed and click connect to this app.
* Before enabling automatic deployment, we still have a couple more steps.
* Click on the settings tab in your app and click on reveal config vars, you can then enter the information that is in the hidden env.py file. Typically, you need to include IP, PORT, SECRET_KEY, MONGO_URI and MONGO_DBNAME.
* Git add, commit and push the changes in your Gitpod (adding the requirements and Procfile files) as epxplained in the above section.
* Go back to your Heroku app and the deployment tab - now click to enable automatic deployment and then click deploy branch.
* Heroku will now receive the code from GitHub and build your app, once it is complete you should see that your app has been successfully deployed.
* Now the deployed site is available and should automatically update whenever changes are pushed to GitHub from Gitpod.

### Local Clone
To make a local copy of a repository on your own GitHub account you can clone it.
This allows others to view the original code and/or make changes to it (on their own local copy).
Changing the code on your local repository will not affect the original code or deployed website.

To clone a repository in GitHub you can follow the steps below:
* Log into GitHub and locate the repository you wish to clone.
* Click on the code button (to the left of the green Gitpod button) and copy the https URL given.
* Open Gitpod (or another editor if you prefer).
* Use the "git clone 'insert copied URL here'" command.
* A clone of the original repository will now be available for you locally 
on your own repository to view/edit as you wish.

### Forking

Forking is another way to  make a local copy of a repository on your own GitHub account to do this follow the below steps:

* Log into GitHub and locate the repository you wish to fork.
* At the top-right of the repository (and top-right of the green Gitpod button), locate the fork button.
* A copy of the original repository will now be available for you locally 
on your own repository to view/edit as you wish.

## Credits

### Code

* The Materializecss library was used to help make this website responsive for different devices and to create the collapsible navbar. 

* The Materializecss library was also used to make the cards on the home page reveal the review details for each book. 

* The Materializecss library was also used to help create the colours and style on the site.

* The Materializecss library was also used to validate user information in the add/edit review forms. 

* Code in the file static/js/script.js was taken from [code institute](https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js) to help validate the select dropdown for add review and add book pages.

* For the reviews I wanted to extract and display the date of each review's creation and most recent update based on the systems datetime, for this I used the code at [w3schools](https://www.w3schools.com/python/python_datetime.asp) to help me extract, format and store the dates as I wanted.

* For the tables in manage books and manage genres pages I wanted to change the colour of the highlight in each row when it is hovered over, by default Materializecss makes this a light grey. I found the below code from [stackoverflow](https://stackoverflow.com/questions/54659023/change-the-highlight-and-striped-colors-in-table-on-materialize-using-a-helper) which helped my achieve my desired result.

> table.highlight>tbody>tr:hover {background-color: rgba(194, 206, 23, 0.5) !important;}

### Content

* For each of the genres I used the genres that are displayed on the popular book site [Waterstones](https://www.waterstones.com/). 

* For each of the books I added books I own to the database and made up my own reviews based on my own thoughts and what others online say about the books.

* For the general layout of the site I had a look at popular sites [Amazon](https://www.amazon.co.uk/) and [Waterstones](https://www.waterstones.com/) to see the layout of how reviews are displayed and get inspiration for style/colour themes. These sites also helped me make up fictional reviews for a range of books to be displayed on the site.

* I used an image from online, information below in the media section.

### Media

* I found the following image online from [pexels](https://www.pexels.com/photo/photo-of-person-sitting-on-cliff-edge-3224344/), this is the file static/images/home-img.jpg. The owner of the image is Ibadah Mimpi and their page on the site is [here](https://www.pexels.com/@ibadah-mimpi-332272). Please not I did some cropping to the original image but no other changes were made.
  
### Acknowledgments

* Code Institute for teaching me the basics of HTML, CSS, Materializecss, JavaScript, jQuery, Python, MongoDB and Flask to allow me to create this website.

* My mentor Antonio Rodriguez who helped provide feedback on this website and improvements that could be made.

* The Slack community for providing support throughout the course so far.  

* Thanks to the fellow students on Slack and my friends who viewed the website and gave feedback on any improvements/changes that could be made. 

* The websites that I used to gain inspiration for creating my own book review site: [Amazon](https://www.amazon.co.uk/) and [Waterstones](https://www.waterstones.com/).