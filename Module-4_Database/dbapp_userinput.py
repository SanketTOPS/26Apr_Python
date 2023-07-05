import pymysql

try:
    dbcon=pymysql.connect(host='127.0.0.1',user='root',password='',database='newdata')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

# Table Create
"""tbl=input("Enter your table name:")
tbl_create=f"create table {tbl}(id int primary key auto_increment,name text,sub text)"
try:
    cr.execute(tbl_create)
    print("Table Created!")
except Exception as e:
    print(e)"""


# Insert Data
"""n=int(input("Enter number of students:"))
for i in range(n):
    name=input("Enter Name:")
    sub=input("Enter Subject:")

    insert_data=f"insert into student(name,sub)values('{name}','{sub}')"
    try:
        cr.execute(insert_data)
        dbcon.commit()
        print("Record Inserted!")
    except Exception as e:
        print(e)"""

# Update Data
"""newname=input("Enter new name:")
newsub=input("Enter new subject:")
id=int(input("Enter ID for update:"))
update_data=f"update student set name='{newname}',sub='{newsub}' where id={id}"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""


# Delete data
"""id=int(input("Enter ID for delete:"))
delete_data=f"delete from student where id={id}"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record Deleted")
except Exception as e:
    print(e)"""

# Show data
name=input("Enter your name for search:")
show_data=f"select * from student where name='{name}'"
try:
    cr.execute(show_data)
    x=cr.fetchall()
    print(x)
except Exception as e:
    print(e)