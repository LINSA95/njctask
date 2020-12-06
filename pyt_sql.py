import mysql.connector as m
def getConnection():
    connection=m.connect(host="localhost",user="root",password="linsa",database="task_student")
    return connection
getConnection()

con=getConnection()
cursor=con.cursor()
cursor.execute("insert into student values(%s,%s,%s)",("4","SREEVIDHYA","26"))
con.commit()
con.close()

con=getConnection()
cursor=con.cursor()
cursor.execute("select * from student")
details=cursor.fetchall()
for i in details:
    print(i)
con.commit()
con.close()

con=getConnection()
cursor=con.cursor()
cursor.execute("delete from student where Rollnumber=4")
con.commit()
con.close()



