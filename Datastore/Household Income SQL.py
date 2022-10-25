# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:23:00 2022

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
dbcursor.execute("SELECT table_household.region, table_household.household_id, table_household.income_M1, table_household.income_M2, table_household.income_M3, table_household.income_M4, table_household.income_M5, table_household.income_M6, table_household.income_M7, table_household.income_M8, table_household.income_M9, table_household.income_M10, (table_household.income_M1 + table_household.income_M2 + table_household.income_M3 + table_household.income_M4 + table_household.income_M5 + table_household.income_M6 + table_household.income_M7 + table_household.income_M8 + table_household.income_M9 + table_household.income_M10) as total_income FROM table_household")
# selects the multiple columns from the table - table_household

data = []     # variable to store the data collected from the database execution
for i in dbcursor:
    data.append(i)
query = "insert into `table_household_income`(`region`, `household_id`, `income_M1`,  `income_M2`, `income_M3`, `income_M4`, `income_M5`, `income_M6`, `income_M7`, `income_M8`, `income_M9`, `income_M10`, `total_income`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# to insert the given data into the designated table - table_household_income
dbcursor.executemany(query, data)
# executed the operation to store the data in the variable data into the database
mydb.commit()
# to confirm the changes made into the database
