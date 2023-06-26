# Data collection portal
This portal will be used to collect data from the interns.

# College Data Collection App

This documentation is intended to help new and existing developers to understand the different functions of the code. Below are the functions of the code:

- dashboard(): This function is called when the route /dashboard is called. It will render the HTML file located in ./Dashboard/dashboard.html.
- a(): This function is called when the route /index is called with the methods GET or POST. It contains a form that needs to be submitted before creating a new document in the database.

- delete_user(sno): This function is called when the route /delete_user/<int:sno> is called. The function accepts the parameter sno which is an integer. The function will delete a MongoDB document based on the sno passed as a parameter.

- update(sno): This function is called when the route /update/<int:sno> is called. It accepts the parameter sno which is an integer. This function will update a MongoDB document based on the sno parameter passed.

__Note__:
- The code seems to be a part of a larger project since some of the variables and functions in this code depend on other parts of the project.

- This Flask application provides a platform for users to collect data on colleges, which can be used for comparison purposes. The application allows users to create, update, and delete college data. The dashboard function displays a user-friendly interface that allows for easy navigation and data visualization.

- The application is built on Flask, a Python-based web framework that is lightweight and easy to use. The MongoDB database is used to store the college data, and the PyMongo library is used to interact with the database. The application uses Jinja2 templating to render HTML pages dynamically.

- The purpose of this application is to provide a platform for users to collect and compare data on colleges. It is particularly useful for students who are looking to apply to college and need to compare different options. It can also be used by educators, researchers, and policymakers who need to analyze trends in college data.

- The application has a number of features that make it user-friendly and accessible. The dashboard provides an overview of the college data, and users can easily navigate to different sections of the application using the navigation menu. The application also includes a search function that allows users to filter college data based on specific criteria.

- Overall, this Flask application provides a simple, user-friendly way to collect, organize, and compare college data. It can be easily customized to fit the needs of different users and is a valuable tool for anyone who needs to analyze college data.


## Project Structure

The code given above is a part of a Flask web application project. Below is the basic structure of the project:

### Flask Web Application

- app.py: The main file of the Flask web application that defines the application and includes all the routes and views.

- templates/: The directory that includes all the HTML templates used in the application.

- static/: The directory that includes all the static files used in the application such as CSS, JS, images, etc.

### College Functions

- index(): This function is a route for the College Data Collection Index. It handles GET and POST requests to fetch and add college data.

- delete_user(sno): This function is a route for deleting a college entry with a given serial number.

- update(sno): This function is a route for updating an existing college entry with a given serial number.

### Dashboard

- dashboard(): This function is a route for the dashboard page of the web application. It renders the HTML template for the dashboard page.
The project structure may also include other directories and files depending on the project requirements. The Flask web application may include additional routes, views, models, and controllers to handle different functionalities of the application. Additionally, the project may include a configuration file, requirements file, and other files necessary to run the application.

# Approve.html

## Introduction
This code is for an Admin Portal to approve or delete draft colleges and view the list of approved colleges along with the comments on them. It uses Flask, a Python web framework, and Bootstrap 5 for front-end styling. The data is stored in a SQLite database.

## File Structure
The main file is app.py which contains the Flask application code. The templates folder contains the HTML templates for the web pages, while the static folder contains the static files (CSS, JS, and images) used in the templates. The database file college.db is stored in the main folder.

## Dependencies
This project requires the following dependencies:

- Flask
- Flask-WTF
- WTForms
- SQLite3
- Bootstrap 5
- jQuery
- DataTables (jQuery plugin)

## Parts
The Admin Portal has three sections:

- Draft Colleges: A page to view and approve or delete draft colleges. It shows a table of all draft colleges, their names, and actions that can be taken on them. It displays a list of colleges that have been submitted for approval but have not yet been approved. If there are no pending colleges, it displays a message saying so. Otherwise, it shows a table with the college's name, along with three buttons: Delete, Approve, and Preview. The "Delete" button permanently deletes the college data, the "Approve" button approves the college, and the "Preview" button opens a new tab to preview the college's page. There is also a button to add comments to the college.

- Approved Colleges: A page to view the list of approved colleges. It shows a table of all approved colleges, their names, and the number of comments on them. It displays a list of colleges that have been approved. It shows a table with the college's name, along with two buttons: Delete and Preview. The "Delete" button permanently deletes the college data, and the "Preview" button opens a new tab to preview the college's page.

- Comments: A page to view all comments on approved colleges. It shows a table of all comments, along with the name of the college and the name of the commenter. It displays a list of comments that have been added to the colleges. It shows a table with the college's name, along with the comments added to it.

## Features
The features of the Admin Portal are:

- Authentication: The portal is protected by a simple username and password authentication system. The username and password are hardcoded into the code for simplicity.
- View draft colleges: The Draft Colleges page shows all the draft colleges, along with their names and actions that can be taken on them.
- Approve draft colleges: The Draft Colleges page allows the admin to approve a draft college, which moves it to the Approved Colleges list.
- Delete draft colleges: The Draft Colleges page allows the admin to delete a draft college, which removes it permanently from the database.
- View approved colleges: The Approved Colleges page shows all the approved colleges, along with their names and the number of comments on them.
- View comments: The Comments page shows all the comments on approved colleges, along with the name of the college and the name of the commenter.
- Add comments: The Draft Colleges page allows the admin to add a comment to an approved college.

## Database Schema
The SQLite database has two tables:

- colleges table: This table stores the information of all colleges. The columns are:
- sno (integer): A unique identifier for the college.
- college_uuid (text): A unique identifier generated for the college that is used in the URL to view the college details.
- college_name (text): The name of the college.
- college_desc (text): A brief description of the college.
- college_courses (text): A comma-separated list of courses offered by the college.
- college_fee (integer): The fee charged by the college.
- college_rating (integer): The rating of the college (out of 5).
- college_approved (integer): A flag indicating whether the college is approved (1) or not (0).
- comments table: This table stores the comments on the approved colleges.

# Update.html
This code seems to be a snippet of HTML, specifically a form for adding and editing information about a college. Here is a breakdown of the different sections of the form:

- State selection dropdown: This section generates a dropdown menu to select the state where the college is located. The states are defined in the states variable, which is a list of strings. If a state is already selected for the college, it will be marked as selected in the dropdown.
- Header photo input: This section includes a text input to add a link for the header photo of the college, and an image tag that shows a preview of the photo. When the user enters a link in the input, the preview image will update automatically using jQuery.
- Exams input: This section allows the user to add a list of exams that are required for the college. There is an "Add Row" button that will create a new input field for each additional exam. When the user is finished adding exams, they can click the "Save" button to submit the data.
- Railway connectivity input: This section allows the user to add a list of railway stations that are connected to the college. Each railway station requires a name and a distance from the college, which are entered using two separate input fields. There is an "Add Row" button that will create a new set of input fields for each additional railway station. When the user is finished adding railway stations, they can click the "Save" button to submit the data.
- The form includes JavaScript functions that are triggered by clicking the "Add Row" and "Save" buttons. These functions use jQuery to add and remove input fields, and to save the data to the form. The code seems to be using the Bootstrap CSS framework, as it includes classes like "form-control", "btn", and "alert".
- Another input field is used to capture a list of exams that are required for admission to the college. The input field is a text box, and the user can input a comma-separated list of exam names. Additionally, the input field contains a button that allows the user to add new rows dynamically to the form. When the user clicks the button, a new row is added to the form, and the user can input a new exam name. The form also includes a save button that allows the user to save the list of exams.
- Another input field is used to capture information about the college's connectivity. The input field is divided into four sub-fields, one for each mode of transportation - railway, bus, metro, and airport. Each sub-field is used to capture information about the connectivity of the college via the respective mode of transportation. The sub-fields are implemented using input boxes, and the user can input the name of the station/airport and the distance from the college to the station/airport. Additionally, the input fields contain a button that allows the user to add new rows dynamically to the form. When the user clicks the button, a new row is added to the form, and the user can input information about a new station/airport. The form also includes a save button that allows the user to save the information about the connectivity.

# Index.html

- 