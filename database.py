import mysql.connector
db_config={
    "host":"localhost",
    "user":"root",
    "password":"root",
    "database":"employee"
}
def connect_to_database():
    return mysql.connector.connect(**db_config)
conn=connect_to_database()
cursor=conn.cursor()
#cursor.execute("CREATE TABLE empdet2(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255),age INT,salary INT)") 
#cursor.execute("SHOW TABLES")
#for i in cursor:
    #print(i) 
#conn.commit()
#sql="INSERT INTO empdet2(name,address,age,salary) VALUES (%s ,%s ,%s ,%s)"
#val=("Mani","VZG","25","20000")
#cursor.execute(sql,val)
#conn.commit()
#sql="DELETE FROM empdet2 WHERE name='Mani' "
#cursor.execute(sql)
#conn.commit()

