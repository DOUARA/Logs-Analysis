# Description
Reporting tool that prints out reports (in plain text) based on the data in a database.
An example of the output of this program can be found in output.txt file. 

# Requirements 
This reporting tool is a Python program that uses psycopg2 module to connect to a database, install:
- python( Any version of python )
- PostgreSQL [(How to install PostgreSQL?)](https://www.postgresql.org/docs/9.3/static/tutorial-install.html)

# Preparation
- First clone the repository to your machine: 
```
  git clone https://github.com/DOUARA/Logs-Analysis.git Logs-Analysis
```
- Create a new database called **news**:
```
psql
CREATE DATABASE news;
```

- Populate your database with data using the command: 
```
  psql -d news -f newsdata.sql
```
> Download newsdata.sql from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

# Runing the program 
from within Logs-Analysis folder run script.py file:
```
python script.py
```
