# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:42:22 2022

@author: al021
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="", database = "household_db"
)

dbcursor = mydb.cursor()
dbcursor.execute("SELECT table_household.region, table_household.household_id, table_household.age_M1, table_household.age_M2, table_household.age_M3, table_household.age_M4, table_household.age_M5, table_household.age_M6, table_household.age_M7, table_household.age_M8, table_household.age_M9, table_household.age_M10 FROM table_household")


data = []
for i in dbcursor:
    data.append(i)
query = "insert into `table_household_age`(`region`, `household_id`, `age_M1`,  `age_M2`, `age_M3`, `age_M4`, `age_M5`, `age_M6`, `age_M7`, `age_M8`, `age_M9`, `age_M10`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
dbcursor.executemany(query, data)
mydb.commit()