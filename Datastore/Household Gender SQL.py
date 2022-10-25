# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:17:21 2022

@author: al021
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:42:22 2022

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
dbcursor.execute("SELECT table_household.region, table_household.household_id, table_household.gender_M1, table_household.gender_M2, table_household.gender_M3, table_household.gender_M4, table_household.gender_M5, table_household.gender_M6, table_household.gender_M7, table_household.gender_M8, table_household.gender_M9, table_household.gender_M10 FROM table_household")
# selects the multiple columns from the table - table_household

data = []     # variable to store the data collected from the database execution
for i in dbcursor:
    data.append(i)
query = "insert into `table_household_gender`(`region`, `household_id`, `gender_M1`,  `gender_M2`, `gender_M3`, `gender_M4`, `gender_M5`, `gender_M6`, `gender_M7`, `gender_M8`, `gender_M9`, `gender_M10`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
# to insert the given data into the designated table - table_household_gender
dbcursor.executemany(query, data)
# executed the operation to store the data in the variable data into the database
mydb.commit()
# to confirm the changes made into the database
