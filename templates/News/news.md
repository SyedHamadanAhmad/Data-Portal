This code creates a web page that allows users to add news articles to a data portal. The page contains a form with various input fields that users can fill out to create a news article entry in the database. The form is built using HTML and styled with Bootstrap.

The page includes a navbar at the top of the page, with a logo and a toggle button that collapses the menu on smaller screens. The main content of the page is contained within a container div, which contains a form for adding news articles.

The form has several input fields:

Heading Text: This is a required field for the title of the news article. Users must enter a heading to create a news article entry.

Sub Heading Text: This is an optional field for a subheading of the news article. Users can leave this field blank if they wish.

Icon: This field allows users to add a logo for the news article. The input is a text field, and when the user types in a link, the image tag below it gets updated to show the image. The image's width and height are set to 850px and 500px, respectively.

Header Image: This field allows users to add a header image for the news article. The input is a text field, and when the user types in a link, the image tag below it gets updated to show the image. The image's width and height are set to 850px and 500px, respectively.

Date: This field allows users to add a date for the news article. The input type is datetime-local, which allows users to select a date and time using a date picker.

Link to Article: This field allows users to add a link to the news article. The input is a text field, and when the user types in a link, the iframe tag below it gets updated to show the linked page. The iframe is set to a height of 80vh.

Below the form, there is a small text field to indicate what happens if the links are broken.

Finally, the page includes several CSS styles to format the page and its elements. The hide class collapses an element and sets its scale to 0.5, making it effectively invisible. The mb-3 class sets a margin-bottom of 1rem and adds a border with a light gray color and a border radius of 1rem. The label class sets the font size of the label to 1.3rem.



