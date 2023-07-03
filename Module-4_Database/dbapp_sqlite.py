import sqlite3

try:
    dbcon=sqlite3.connect("testdb.db")
    print("Database connected!")
except Exception as e:
    print(e) 
    

# Table Create
tbl_create="create table studinfo(id integer primary key autoincrement, name text, sub text)"
try:
    dbcon.execute(tbl_create)
    print("Table created")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo(name,sub)values('sanket','python'),('mitesh','ui'),('nirav','java'),('pratik','php'),('meet','ios')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""


# Update Data
"""update_data="update studinfo set sub='react' where sub='php'"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""


# Delete Data
"""delete_data="delete from studinfo where name='meet'"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""


# Show Data
fetch=dbcon.cursor()

show_data="select * from studinfo"
try:
    fetch.execute(show_data)
    data=fetch.fetchall()
    #data=fetch.fetchmany(4)
    #data=fetch.fetchone()
    #print(data)
    for i in data:
        print(i[1])

except Exception as e:
    print(e)
