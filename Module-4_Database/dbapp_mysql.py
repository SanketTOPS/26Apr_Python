import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='newdata')
    print("Database connected!")
except Exception as e:
    print(e)


cr=dbcon.cursor()

# Table Create
tbl_create='create table studinfo(id int primary key auto_increment,name text,sub text)'
try:
    cr.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)

# Insert Data
"""insert_data="insert into studinfo(name,sub) values('sanket','python'),('mitesh','php'),('sanjay','java'),('nirav','html'),('ashok','c++'),('hitesh','angular')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update studinfo set sub='android' where id=11"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=7"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)
"""


# Show Data
select_data="select * from studinfo"
try:
    cr.execute(select_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        #print(i)
        print(i[1])
except Exception as e:
    print(e)
