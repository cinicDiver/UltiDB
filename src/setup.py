import sqlite3
import numpy as np
import pandas as pd

#Holds the particular name of the databese according to the user input at setup.
dbname='../{}DB.db'.format('ulti')

#Represents the database while the table creation is executed.
db = sqlite3.Connection(':memory:')
#Stablishes the cursor which whill act uppon the database for command executions. 
cursor = db.cursor()

#Creates th table for relationship management.
cursor.execute('''CREATE TABLE IF NOT EXISTS relation(
    relation_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    relation_name TEXT NULL
    );''')

#Commits table creation to database.
db.commit()

#Creates the table for realted people management.
cursor.execute('''CREATE TABLE IF NOT EXISTS related (
    related_id TEXT PRIMARY KEY UNIQUE,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    relation TEXT NOT NULL,
    player_num INTEGER UNIQUE,
    status INTEGER NOT NULL
    );''')

#Commits table creation to database.
db.commit()

#Creates the table for money transaction types.
cursor.execute('''CREATE TABLE IF NOT EXISTS move_types(
    move_type_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    move_type_name TEXT NOT NULL,
    move_type_income INTEGER DEFAULT 1
    );''')


#Commits table creation to database.
db.commit()

#Creates the table for money transaction management.
cursor.execute('''CREATE TABLE IF NOT EXISTS movements(
    move_id TEXT PRIMARY KEY UNIQUE,
    move_type_id INTEGER NOT NULL ,
    move_value REAL NOT NULL,
    move_report_date REAL NOT NULL,
    move_confirm_date REAL NOT NULL,
    move_related_id TEXT NOT NULL,
    move_notes TEXT,
    FOREIGN KEY(move_type_id) REFERENCES move_types(move_type_id),
    FOREIGN KEY(move_related_id) REFERENCES related(related_id)
    );''')

#Commits table creation to database.
db.commit()

#Temporary checks.
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print('Table names:')
for table_name in tables:
    print(table_name[0])
print('--End of table names--')
#Closes both connections.
cursor.close()
db.close()