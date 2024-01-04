import mysql.connector
from dbconfig import mysql as cfg

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=cfg["password"]
)


cursor = db.cursor()

cursor.execute("create DATABASE datarepresentation")

db.close()
cursor.close()