# Counselings
This code is an HTML page that creates a form to add data to a counseling data portal. It contains a navigation bar, several form fields, and some inline styling. It uses Bootstrap for styling, jQuery for some scripting, and DataTables for a table.

The form includes fields for the counseling name, counseling image, sub-heading, date of counseling, and top college information. The top college information includes the college name, its website, and its rank. The form also has a button to add a new top college field dynamically, and a button to save all the top college data in a table format.

The meta tag defines the character set and the viewport for the web page. The link tags include external stylesheets for Bootstrap and Bootstrap icons. The script tag includes the jQuery library, which is required for some of the scripting.

## Libraries and frameworks
The code uses the following libraries and frameworks:

- jQuery v3.2.1
- Bootstrap v5.2.3
- DataTables v1.13.4 (with Bootstrap integration)
- Bootstrap Icons v1.10.3

## Form fields
The form includes the following fields:

- Counseling Name
- Counseling Header Image Link
- Sub - Heading
- Date of Counseling
- Top College
- Link to Apply

## Additional features
The code includes the following additional features:

- Custom CSS to style certain elements and add a hover effect
- A hidden field to store the data entered in the multiple input field for top colleges
- A button to add more input fields for top colleges
- A button to save the entered data in the multiple input field for top colleges
- An image preview for the header image field

## Functions in Counslings
This code provides a set of JavaScript functions that allow users to dynamically create and remove input fields and then save the values of these fields to a JSON array. It also initializes a DataTable using the DataTables library.

__addNewElem(name)__
- This function takes in a name argument, which is used to identify the type of input field being created (e.g., "link" or "name"). It then creates a new row of input fields with unique IDs using the provided name and an incrementing count variable. The newly created row is appended to the DOM element with an ID of newRow and the provided name. An event listener is also added to the "remove" button in the row so that it can be deleted from the DOM when clicked. Finally, another event listener is added to a "save" button in the row. When clicked, this button calls the joinMultiFields() function (described below) to retrieve the values of all the input fields in the row and store them in a JSON array. The resulting JSON array is then displayed in a div with an ID of ${name}_save, and the array is set as the value of the input field with an ID of the provided name.

__joinMultiFields(parent, output, name)__
- This function takes in three arguments: parent, which is the ID of the DOM element containing the input fields; output, which is the ID of the input field that will receive the resulting JSON array; and name, which is used to identify the type of input field being processed. The function retrieves all the input fields with a class of ${name}_name or ${name}_link and uses a loop to create a JSON object for each pair of input fields where the "name" field is not empty. The resulting JSON objects are then pushed to an array, which is returned by the function.

__$(document).ready(function() {...})__
- This code block initializes a DataTable using the DataTables library. The DataTable is applied to the DOM element with an ID of counselingsDraftTable. The DataTable is set to be responsive and to allow scrolling.




