from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="", database = "household_db"
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/householdage")
def household_age():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_age")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household age.html", value = data)

@app.route("/householdgender")
def household_gender():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_gender")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household gender.html", value = data)

@app.route("/householdincome")
def household_income():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_income")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household income.html", value = data)

@app.route("/householdexpenditure")
def household_expenditure():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_expenditure")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household expenditure.html", value = data)

@app.route("/householdpriorities")
def household_priorities():
    dbcursor = mydb.cursor()
    dbcursor.execute("SELECT * FROM table_household_priorities")
    data = dbcursor.fetchall()
    dbcursor.close()
    return render_template("household priorities.html", value = data)





if __name__ == "__main__":
    app.run()
