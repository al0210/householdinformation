# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:37:41 2022

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
dbcursor.execute("SELECT table_household.region, table_household.household_id, table_household.expenditure_cooked_food, table_household.expenditure_house, table_household.expenditure_electricity, table_household.expenditure_water, table_household.expenditure_sanitation, table_household.expenditure_waste_collection, table_household.expenditure_cooking_fuel, table_household.expenditure_internet, table_household.expenditure_communication, table_household.expenditure_other, table_household.expenditure_transport, (table_household.expenditure_cooked_food + table_household.expenditure_house + table_household.expenditure_electricity + table_household.expenditure_water + table_household.expenditure_sanitation + table_household.expenditure_waste_collection + table_household.expenditure_cooking_fuel + table_household.expenditure_internet + table_household.expenditure_communication + table_household.expenditure_other + table_household.expenditure_transport) as total_expenditure FROM table_household")
# selects the multiple columns from the table - table_household

data = []     # variable to store the data collected from the database execution
for i in dbcursor:
    data.append(i)
query = "insert into `table_household_expenditure`(`region`, `household_id`, `expenditure_cooked_food`,  `expenditure_house`, `expenditure_electricity`, `expenditure_water`, `expenditure_sanitation`, `expenditure_waste_collection`, `expenditure_cooking_fuel`, `expenditure_internet`, `expenditure_communication`, `expenditure_other`, `expenditure_transport`, `total_expenditure`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# to insert the given data into the designated table - table_household_expenditure
dbcursor.executemany(query, data)
# executed the operation to store the data in the variable data into the database
mydb.commit()
# to confirm the changes made into the database
