import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_showbiz"
)

dbcursor = mydb.cursor()

sql = "INSERT INTO profesi (nama_profesi) VALUES (%s)"
val = ("Girlband",)
dbcursor.execute(sql, val)
mydb.commit()

print(dbcursor.rowcount, "data inserted.")

dbcursor.execute("SELECT * FROM profesi")
myresult = dbcursor.fetchall()

for x in myresult:
    print(x)

dbcursor = mydb.cursor()
sql = "DELETE FROM profesi WHERE id_profesi = '9'"
dbcursor.execute(sql)
mydb.commit()

print(dbcursor.rowcount, "data(s) deleted.")