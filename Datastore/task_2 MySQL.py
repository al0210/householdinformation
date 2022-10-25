# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:51:25 2022

@author: al021
"""

import csv
import MySQLdb

mydb = MySQLdb.connect(host="127.0.0.1", user = "root", password = "", database="household_db")

with open('task_2_data.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter =',')
    table_value = []
    for row in csvfile:
        row_value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                     row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
                     row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38],
                     row[39], row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49], row[50], row[51],
                     row[52], row[53], row[54], row[55], row[56], row[57])
        table_value.append(row_value)
        
query = "insert into `table_household`(`region`, `household_id`, `age_M1`, `age_M2`, `age_M3`, `age_M4`, `age_M5`, `age_M6`, `age_M7`, `age_M8`, `age_M9`, `age_M10`, `gender_M1`, `gender_M2`, `gender_M3`, `gender_M4`, `gender_M5`, `gender_M6`, `gender_M7`, `gender_M8`, `gender_M9`, `gender_M10`, `income_M1`, `income_M2`, `income_M3`, `income_M4`, `income_M5`, `income_M6`, `income_M7`, `income_M8`, `income_M9`, `income_M10`, `expenditure_cooked_food`, `expenditure_house`, `expenditure_electricity`, `expenditure_water`, `expenditure_sanitation`, `expenditure_waste_collection`, `expenditure_cooking_fuel`, `expenditure_internet`, `expenditure_communication`, `expenditure_other`, `expenditure_transport`, `priority_groceries`, `priority_cooked_food`, `priority_education`, `priority_house`, `priority_health`, `priority_transport`, `priority_electricity`, `priority_water`, `priority_sanitation`, `priority_waste_collection`, `priority_cooking_fuel`, `priority_internet`, `priority_communication`, `priority_loan_repayment`, `priority_other`) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

mycursor = mydb.cursor()
mycursor.executemany(query, table_value)
mydb.commit()