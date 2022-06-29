import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Barathbk29@123",
  database="Employee_detailssample"
)

db = mydb.cursor()

ret = int(input("Enter the value :"))
if ret == 1:


  task = input("Enter the task :")
  if task == "query":
    data = input("Enter which data you need to query :")
    name = input("Enter the name :")
    db.execute(f"SELECT * FROM basic WHERE {data} like {name}")
    a = db.fetchall()
    for i in a:
      print(i)

  if task == "update":
    tablename = input("Enter the Table name :")
    columnname1 = input("Enter the column1 name :")
    columnname2 = input("Enter the column2 name :")
    value1 = input("Enter the data needs to replaced :")
    value2 = input("Enter the name :")
    db.execute(f"UPDATE {tablename} SET {columnname1} = {value1} WHERE {columnname2} ={value2}")
    mydb.commit()
    print(db.rowcount,"record(s) affected")

  if task == "sort":
    ans = input("Enter which order for sorting :")
    if ans == "asc":
      tablename = input("Enter the table name :")
      basedon = input("Enter the Column name")
      db.execute(f"SELECT * FROM {tablename} ORDER BY {basedon}")
      a = db.fetchall()
      for i in a:
        print(i)

    if ans == "desc":
      tablename = input("Enter the table name :")
      basedon = input("Enter the Column name")
      db.execute(f"SELECT * FROM {tablename} ORDER BY {basedon} DESC")
      a = db.fetchall()
      for i in a:
        print(i)