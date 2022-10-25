from flask import Flask, render_template
# Flask imported from library flask to help develop a web interface, render_template imported to call the .html file and pass other reuired values
import mysql.connector
# library mysql.connector imported to connect with the sql databases

app = Flask(__name__)
# app defined to store the name of the application package

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="", database = "household_db"
)
# object - mydb defined to created a connection with the database in the given host, user and password

@app.route("/")     # defines how to access the given page of the application
def home():       # defines the home page of the application
    return render_template("home.html")   # generates the output and passes the parameters to the .html file

@app.route("/householdage")
def household_age():      # defines the household age page of the application
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_age")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household age.html", value = data)      # returns the value generated on to the .html file which further uses Jija2 engine to deliver the page of the application

@app.route("/householdgender")
def household_gender():     # defines the household gender page of the application
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_gender")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household gender.html", value = data)

@app.route("/householdincome")
def household_income():     # defines the household income page of the application
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_income")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household income.html", value = data)

@app.route("/householdexpenditure")
def household_expenditure():      # defines the household expenditure page of the application
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_expenditure")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household expenditure.html", value = data)

@app.route("/householdpriorities")
def household_priorities():       # defines the household priorities page of the application
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_priorities")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household priorities.html", value = data)





if __name__ == "__main__":
    app.run()
# Command to run the application  
