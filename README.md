# Data Representation
Data Representation Project

## Files in Project
* InitDB.sql contains the sql that I used to set up the database.  The database I used was mysql.
* mysqlconnect.py contains the database connection so that I can access the mysql database in python.
* FilmDAO.py contains the DAO for accessing data from the database using the connection.
* RestServer.py is where the API is set up using Flask.  
* client-script.js contains the javascript used by the html file to access the Flask API using AJAX.
* Client.html contains the html that the user can use to change the data in the database.

## Running the Project
* Navigate to the root folder containing the RestServer.py file.
* Run "python RestServer.py" in the terminal.
* Open "Client.html" using a web browser.
