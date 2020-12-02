import sqlite3


conn = sqlite3.connect("cred.db")

cur=conn.cursor()

# cur.execute("insert into credentials values('jaisheel' , 'india')")


cur.execute("create table if not exists credentials(name varchar(100) , password varchar(100))")

conn.commit()