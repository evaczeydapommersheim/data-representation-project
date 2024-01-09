# This is a project for:
# **ATU Course **- Higher Diploma in Science in Data Analytics
## **Module**- 23-24: 4682 -- DATA REPRESENTATION
## **Lecture** - Andrew Beatty
---
##  Prepared by Eva Czeyda-Pommersheim
---
### **Project Requirements, Execution and reference to content of this repository:**

The purpose of the project is to demonstrate an understanding of creating and consuming RESTful APIs with below guidance instructions as a minimum requirement:<br>

1. Create a Flask server that has a RESTful API Reference server.py.<br><br>
*This server was created in a virtual environment using Flask. ***Reference requirements.txt*** *file for the applications that need to be installed on a machine/virtual environment before runnning this code.*<br>

2. Test CRUD (Create, Update, Delete) operations.<br><br>
***Reference comments for each CRUD operation in commented sections of server.py.***<br>

3. Create a database and a table.<br><br>
*MySQL and MySQL connector python was installed and used to create a database manually (datarepresentation database) and used python code to create a table called "movie" and to populate the table with data. A configuration file was created to be used an authentication when connecting to mySQL on local machine. In order to connect to MySQL on the online hosting platform a different dbconfig.py file was created.*
***Reference updateDBTable.py, dbconfig.py***<br><br>
The movieDAO.py file was created as a Data Access Object file to establish the CRUD operations via functions between the database and its server. the testing of these codes were completed in the updateDBTable.py file.<br>

4. Use AJAX calls to perform the CRUD operations.<br><br>
*A stand alone file was created to contain all CRUD operation related code and link to the web application.* ***Reference ajaxcalls.js.***<br>

5. Create Web Application which represents the data in a nice way.<br><br>
*A web application was created and designed to represent the data and the create, update, delete functionality of the application by running the server in a virtual environment.* ***Reference movieViewer.html file and a lnked image movie.jpeg*** *as part of the formatting of the web application.*

#### The project included in this repository is a Type A project as described above. 

This project is hosted online in Pythonanywhere under the following [link](http://evaczeydapommersheim.pythonanywhere.com/movieViewer.html). [http://evaczeydapommersheim.pythonanywhere.com/movieViewer.html]