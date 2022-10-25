# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:57:53 2022

@author: al021
"""

import mysql.connector
# library to import .csv file which needs to be connected with the database

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="", database = "household_db"
)

dbcursor = mydb.cursor()
dbcursor.execute("SELECT table_household.region, table_household.household_id, table_household.priority_groceries, table_household.priority_cooked_food, table_household.priority_education, table_household.priority_house, table_household.priority_health, table_household.priority_transport, table_household.priority_electricity, table_household.priority_water, table_household.priority_sanitation, table_household.priority_waste_collection, table_household.priority_cooking_fuel, table_household.priority_internet, table_household.priority_communication, table_household.priority_loan_repayment, table_household.priority_other FROM table_household")
# selects the multiple columns from the table - table_household

data = []     # variable to store the data collected from the database execution
for i in dbcursor:
    data.append(i)
query = "insert into `table_household_priorities`(`region`, `household_id`, `priority_groceries`,  `priority_cooked_food`, `priority_education`, `priority_house`, `priority_health`, `priority_transport`, `priority_electricity`, `priority_water`, `priority_sanitation`, `priority_waste_collection`, `priority_cooking_fuel`, `priority_internet`, `priority_communication`, `priority_loan_repayment`, `priority_other`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# to insert the given data into the designated table - table_household_priorities
dbcursor.executemany(query, data)
# executed the operation to store the data in the variable data into the database
mydb.commit()
# to confirm the changes made into the database
