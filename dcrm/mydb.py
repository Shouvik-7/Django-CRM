import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Onepunch@7'
)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE djcrmdb")

print("DB Created")