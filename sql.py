import sqlite3
#connect to sqlite3
connection=sqlite3.connect("student.db")

cursor=connection.cursor()



table_info="""
Create table student(name varchar(25),class varchar(25),
section varchar(25),marks int);
"""
cursor.execute(table_info)
cursor.execute('''Insert Into student values('David','Data science','A',90)''')
cursor.execute('''Insert Into student values('Rahul','Devops','A',100)''')
cursor.execute('''Insert Into student values('Vamsi','Datascience','B',89)''')
cursor.execute('''Insert Into student values('Bhumi','Devops','A',97)''')
cursor.execute('''Insert Into student values('Shiva','Datascience','B',98)''')


print("inserted students")
data=cursor.execute('''select * from student''')

for row in data:
    print(row)
connection.commit()
connection.close()