# householdinformation

**Project Description**

This project is about developing a web interface tool - a table - to display household information with pagination, searchability and filters. Python programming, HTML, CSS and a bit of Javascript were all used in developing the tool. A summary of household information of different households containing information about the age, gender, income, expenditure and priorities of expenditure of both rural and urban regions is shown in the table.

The process included reading data using csv and writing it into an SQL database. Futher, multiple data tables were created in the database by breaking down the table read from the .csv file. The next step was to display the tables in a web interface tool to show a summary of the household data. The python library flask was used to build the web interface and jquery and css templates were taken from https://datatables.net/ to make the tables paginated and searchable. A feature was built to filter the data by categories. The data tool is both searchable and filterable. 

An extra column was added in the tables - table_household_age, table_household_gender, table_household_income, and table_household_expenditure. The table_household_age is used to categorise the families into single parent/grandparent family, nuclear family, childless family and single member family. The table_household_gender is used to find out whether the lead member of the family is a female or a male (assuming the first member of the family is the lead member). The table_household_income is used to categorise the data based on households below poverty line and above poverty line. The table_household_expenditure was used to find out which families lie below the poverty line for expenditure based on two measdures - International Poverty Line (IPL) and Tendulkar Committee Poverty Libe (TPL). 

The home page of the application contains a brief description of the website and the links for each of the other pages. There are five other pages - each for displaying the summary of data on a table for household age, household gender, household income, household expenditure and household priorities for expenditure. Overall, the web interface tool was a good tool to build and there is a scope to add a lot more features to make it more dynamic.


**Directory Structure**

The directory contains four folders with all the project documents and one README file which contains the guide to the project. The following is a brief description of each component in the directory.

1. _**Database**_ - This folder contains a .sql file - household_db.sql - containing all the databases developed and used during the course of the project.

2. _**Datastore**_ - This folder contains 7 files in all - 6 .py files and 1 .csv file. The .py files contain the codes which were developed to write the data into the database schema. The .csv file is the one from where the data was taken to enter into the database. 

i) _Household Age SQL.py_ - Contains the code which was used to develop the database table - table_household_age

ii) _Household Expenditure SQL.py_ - Contains the code which was used to develop the database table - table_household_expenditure

iii) _Household Gender SQL.py_ - Contains the code which was used to develop the database table - table_household_gender

iv) _Household Income SQL.py_ - Contains the code which was used to develop the database table - table_household_income

v) _Household Priorities SQL.py_ - Contains the code which was used to develop the database table - table_household_priorities

vi) _task_2 MySQL.py_ - Contains the code which was used to develop the database table - table_household

vii) _task_2_data.csv_ - Contains the data from which the household information was extracted

3. _**Web Interface Tool**_ - This folder contains Tool Code.py file which has the code for the development of the web interface tool.

4. _**templates**_ - This folder contains 6 .html files and 4 .js files which were used to develop the web interace and tool with features.

i) _filterage.js_ - Contains the code run to develop the filter features for the web page household age.html

ii) _filterexpenditure.js_ - Contains the code run to develop the filter features for the web page household expenditure.html

iii) _filtergender.js_ - Contains the code run to develop the filter features for the web page household gender.html

iv) _filterincome.js_ - Contains the code run to develop the filter features for the web page household income.html

v) _home.html_ - Contains the code run to develop the page containing information about the home page of the web interface tool.

vi) _household age.html_ - Contains the code run to develop the page containing household age information.

vii) _household expenditure.html_ - Contains the code run to develop the page containing household expenditure information.

viii) _household gender.html_ - Contains the code run to develop the page containing household gender information.

ix) _household income.html_ - Contains the code run to develop the page containing household income information.

x) _household priorities.html_ - Contains the code run to develop the page containing household prioritioes of expenditure information.


**Build Instructions**

This section contains the instructions that one needs to follow in order to run this programs successfully.

  1. To access the project in your system, please go to command prompt and run the command "git clone https://github.com/al0210/householdinformation.git"

  2. To run the codes, first of all, one must require to have python installed and need to run all the given codes in a suitable IDE to develop the project.

  3. MySQL is another pre requisite to have in order to store the data scraped into databses and further use them to show information in the web interfaces.

  4. All the libraries listed in the next sextion - list of dependencies - need to be installed in python before running the respective programs

  5. The files being called and accessed like the .csv, .js and .html files need to be present in the required location in order to be accessed while programming. Csv      files need to be present in the same folder as the .py files which contain reading from or writing to the .csv. .js and .html files need to be present in the          folder 'templates' which Jinja2 Engine needs to process and develop the requirements for the web application.

  6. To run the web application, open the python file 'Tool Code.py' and run the program. When you run the program you, on the console, you will see a link -                'http://127.0.0.1:5000/'. Copy this link (don't press ctrl+c but copy it by right clicking. clicking on ctrl+c will lead to quitting the console and the link          would not have copied) and paste it on your browser. Access the other pages of the web interface by clicking on the links provided in the home page.
  7. The resultant database needed some modification to help develop the desired tool. The following SQL queries were executed in the database schema. 
     
     1. The gender given in the csv was in binary numbers - 1 for female, 0 for male. This caused an ambiguity because the gender of the members with age = 0 (meaning 
        that there is no more members in that household) was also 0 while the male data was assigned to 0. The following SQL code will erase the ambiguity.
          UPDATE `table_household` SET `gender_M1` = '-' WHERE `age_M1` = '0' 
        This command must be repeated for each column corresponding to the gender of the 10 household members.
     2. To help filter the data, an extra column was added in each of the tables - table_household_age, table_household_gender, table_household_income, 
        and table_household_expenditure. To update this column based on the values of the other column/s, the following codes are necessary:
     i) For table_household_age, add a new column to the database and name the column by a name of your choice. I named it Status. Give it VARCHAR datatype with length         400. 
        Once the column is created, run the following commands: 
          UPDATE `table_household_age` SET `Status` = 'Single Parent/Grandparent' WHERE `age_M1` - `age_M2` >= '18' (18 was taken because it is the legal age to bear a           child in India.)
          UPDATE `table_household_age` SET `Status` = 'Nuclear Family' WHERE `age_M1` - `age_M2` < '18'
          UPDATE `table_household_age` SET `Status` = 'Childless Family' WHERE `age_M3` = '0'
          UPDATE `table_household_age` SET `Status` = 'Single Member' WHERE `age_M2` = '0'
    ii) For table_household_gender, add a new column to the database and name the column by a name of your choice. I named it lead_member. Give it VARCHAR datatype             with length 400. 
        Once the column is created, run the following commands:
          UPDATE `table_household_gender` SET `lead_member` = `F` WHERE `gender_M1` = '1'
          UPDATE `table_household_gender` SET `lead_member` = `M` WHERE `gender_M1` = '0'
   iii) For table_household_income, add a new column to the database and name the column by a name of your choice. I named it below_poverty_line. Give it VARCHAR               datatype with length 400. 
        Once the column is created, run the following commands:
         UPDATE `table_household_income` SET `below_poverty_line` = 'Y' WHERE `total_income` < '2092.25'
         UPDATE `table_household_income` SET `below_poverty_line` = 'N' WHERE `total_income` >= '2092.25'
    iv) For table_household_expenditure, add a new column to the database and name the column by a name of your choice. I named it below_poverty_line. Give it VARCHAR         datatype with length 400. 
        Once the column is created, run the following commands:
          UPDATE `table_household_expenditure` SET `below_poverty_line` = 'Y' WHERE (`total_expenditure` < 1766.5) AND (`region` = 'PHH')
          UPDATE `table_household_expenditure` SET `below_poverty_line` = 'Y' WHERE (`total_expenditure` < 1441.5) AND (`region` = 'CHH' OR `region` = 'KHH`)
          UPDATE `table_household_expenditure` SET `below_poverty_line` = 'N' WHERE (`total_expenditure` >= 1766.5) AND (`region` = 'PHH')
          UPDATE `table_household_expenditure` SET `below_poverty_line` = 'Y' WHERE (`total_expenditure` >= 1441.5) AND (`region` = 'CHH' OR `region` = 'KHH`)
 
 
**List of Dependencies**

1. MySQLdb or mysql.connector

2. Flask

3. csv (library)
