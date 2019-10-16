# glossier_etl
This project was created to help imaginary business analysts look at different analytics coming from certain data files. 
Data files have been extracted as JSON files and stores in DATA directory. This is an ETL pipeline to a posgreSQL db where tables are created with a specific schema.

Prerequisites
=============

All libraries you need to install:
>>pip3 install <library>

psycopg2
ipython-sql
pandas

Starting Pipeline
=================
 #start database connection and run
 
>>python create_tables.py

#tables have now been created and schema has been stored

>>python etl.py

#Start ETL pipeline by running ETL.py script this will then load data into respective schemas following order selected
