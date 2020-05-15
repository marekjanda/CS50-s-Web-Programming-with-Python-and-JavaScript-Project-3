# Project 3

Web Programming with Python and JavaScript

Marek Janda, 20/02/2020

Project 3 

Models

Topping - Pizza topping class according the pinnochio's menu. This class has one attribute name
Pizza - Pizza class is defined with following attributes: pizza_type (sicilian or regular), toppings option (how many toppings), price_small 
        and price_large
Sub - Sub class represents sub menu item and it contains following properties: name, price_small, price_large
Pasta - Pasta class represents pasta menu option
Salad - Represents salad menu option
Platter - Represents platter menu option
OrderItem - Represents any item from above added in the order and it is linked as many to many field to OnlineOrder class. If the item is pizza
            selected toppings are added to the item
Online order - Is Containes order items via many to many relation to OrderItem class. Contains also the customer username, total price, 
               date of order and status of the order


Project's url paths are described in this project with their corresponding views, files and functionalities.

"" - index.html
At index page a pinochio's menu is displayed together with navbar which contains links to login page, register page and home page (to navigate back to index page). View function "index" renderes the page with corresponding data.

"register" - register.html
At register page a user can register by submitting chosen username, first name, last name, email address and selected password. Registration form is created in "forms.py" file. View function "register" handles all requests and rendering of the page as well as registering the user.

"homepage" - homepage.html
After a user is logged in or after the user registers he/she is redirected to homepage where he can see a complete menu and following links in navbar: Order - links to order page, Shoppingcart - links to shopping cart page, Tracker - if user has placed and undelivered order he/she can track the progress here, Logout - log user out. View function "homepage" handles requests and rendering of this page.

"logout"
This view function logs the user out and redirect to "index".

"login" - login.html
A registered user can log in by filling in his username and password and after logging in he is redirected to homepage. View function "login" is handling the requests and rendering.

"order" - order.html
Menu is displayed with added button to each menu item. Clicking on the button will create an OrderItem class object and add it to user's order. If the user has no unplaced order a new OnlineOrder class object is created. Sending menu item data is handled by JavaScript (AJAX) scirpt "order_v2.js". "jquery-3.4.1.js" file contains a JS library required for handling AJAX requests. View function "order_request" handles the request and page rendering.

"add"
This view function handles adding creating an OrderItem class object and adding to respective OnlineOrder class object from data received from AJAX request sent by "order_v2.js". View function "add_request" handles all request and data processing.

"shopping_cart" - shoppingcart.html
User's OnlineOrder, if unplaced, is querried from the databased and displayed (all items and total price). There are two buttons at the page. By clicking these buttons the user can either place the order or discard it. View function "shopping_cart" handles the database querries, request and page rendering.

"tracker" - tracker.html
Personal touch. At the path the user can track the progress of his order. The order can have following statuses: unplaced (can't be seen in tracker page), placed, preparing, cooking, finished and delivered (can't be seen in tracker page). View function "tracker" handles the requests and page rendering.

"staffpage" - staffpage.html
Only a staff member (based of "staff" atribute of user class) can see this page. All OnlineOrder class objects are querried and displayed at this page and sorted by "status" attribtue. Each order is a link to order processing page. View function "staffpage" handles request, database querries and page rendering.

"<int:order_id>/order_process" - orderprocess.html
At this page a staff member can change a status of the order. View function "order_process" takes two arguments: request and order_id. This function handles the POST request to change the order status.

Includes
HTML files containing pinnochio's menu and pizza selection html (included at order page).

styles.css
Contains the css for the page styling.

background_image.jpg
Background image of the page. 

base.html
Base html files containing the general layout of the application.