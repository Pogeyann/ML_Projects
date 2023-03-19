import sqlite3

conn = sqlite3.connect('/home/mush/Documents/family.sqlite3')
curr = conn.cursor() #Initiatiing the sql operations in python
#Which will be used to execute sql commands
#.3 executing sql scripts in python
curr.executescript(''' CREATE TABLE fam (name TEXT, age INT);''')
conn.commit()
conn.close()