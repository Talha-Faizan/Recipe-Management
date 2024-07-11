import mysql.connector as mycon

con1 = mycon.connect(host='127.0.0.1', user="root", password="root", database="RECIPE_DB")
if con1.is_connected():
    print("connection established")
mycur=con1.cursor()
mycur.execute("show tables;")

for i in mycur:
    print(i)