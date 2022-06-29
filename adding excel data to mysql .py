import mysql.connector
import xlrd3
from mysql.connector import  errors



book = xlrd3.open_workbook("D:/pythonfiles/payscale.xlsx")




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#your password",
  database="Employee_detailssample"
)

db = mydb.cursor()

try:
    try:
        db.execute("CREATE DATABASE Employee_detailssample")
    except mysql.connector.errors.DatabaseError:
        print("Database already created")

  # ##CREATIN
    # G TABLES::
    try:
        db.execute("CREATE TABLE Basic(S_No INT(5),Employee_code INT NOT NULL PRIMARY KEY, Employee_Name VARCHAR(255),Qualification VARCHAR(255), DOJ VARCHAR(255),New_Grade VARCHAR(255),Experience VARCHAR(255),Gender VARCHAR(255), Age INT(5))")

        db.execute("CREATE TABLE Salary_Details(Employee_code INT NOT NULL PRIMARY KEY, Employee_Name VARCHAR(255), Basic VARCHAR(255), FDA VARCHAR(255), VDA VARCHAR(255), DA VARCHAR(255), HRA VARCHAR(255), CON VARCHAR(255), Washing_Allowance VARCHAR(255), Other_Allowance VARCHAR(255), Special_Allowance VARCHAR(255), Total VARCHAR(255))")

        db.execute("CREATE TABLE Skilled(S_No INT(5),Employee_code INT NOT NULL PRIMARY KEY, Employee_Name VARCHAR(255),Qualification VARCHAR(255), DOJ VARCHAR(255),New_Grade VARCHAR(255),Experience VARCHAR(255),Gender VARCHAR(255), Age INT(5))")
        db.execute("CREATE TABLE semi_skilled(S_No INT(5),Employee_code INT NOT NULL PRIMARY KEY, Employee_Name VARCHAR(255),Qualification VARCHAR(255), DOJ VARCHAR(255),New_Grade VARCHAR(255),Experience VARCHAR(255),Gender VARCHAR(255), Age INT(5))")
        db.execute("CREATE TABLE Highly_skilled(S_No INT(5),Employee_code INT NOT NULL PRIMARY KEY, Employee_Name VARCHAR(255),Qualification VARCHAR(255), DOJ VARCHAR(255),New_Grade VARCHAR(255),Experience VARCHAR(255),Gender VARCHAR(255), Age INT(5))")
    except mysql.connector.errors.DatabaseError:
        print("Table already created")

  ##INSERTING DATA::
  ##Table 1 - Basic:
    try:
        sheet = book.sheet_by_name("2022jan")
        for r in range(2, sheet.nrows):
            S_No= str(sheet.cell(r,0).value)
            Employee_code= sheet.cell(r,1).value
            Employee_Name = sheet.cell(r,2).value
            Qualification= sheet.cell(r,3).value
            DOJ= sheet.cell(r,4).value
            New_Grade = sheet.cell(r, 5).value
            Experience = int(sheet.cell(r,6).value)
            Gender = str(sheet.cell(r,8).value)
            Age= sheet.cell(r,9).value
            query = "INSERT INTO basic(S_No, Employee_code, Employee_Name, Qualification, DOJ,New_Grade, Experience,Gender, Age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (S_No, Employee_code, Employee_Name, Qualification, DOJ, New_Grade, Experience, Gender, Age)
            db.execute(query,values)
            mydb.commit()
            if (Experience >= 1) and (Experience <=5):
              values = (S_No, Employee_code, Employee_Name, Qualification, DOJ, New_Grade, Experience, Gender, Age)

              query3 = "INSERT INTO semi_Skilled(S_No, Employee_code, Employee_Name, Qualification, DOJ,New_Grade, Experience,Gender, Age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
              db.execute(query3,values)
              mydb.commit()
            if (Experience >= 6) and (Experience <=10):
              values = (S_No, Employee_code, Employee_Name, Qualification, DOJ, New_Grade, Experience, Gender, Age)

              query3 = "INSERT INTO Skilled(S_No, Employee_code, Employee_Name, Qualification, DOJ,New_Grade, Experience,Gender, Age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
              db.execute(query3,values)
              mydb.commit()
            if (Experience >=11) :
              values = (S_No, Employee_code, Employee_Name, Qualification, DOJ, New_Grade, Experience, Gender, Age)

              query3 = "INSERT INTO Highly_skilled(S_No, Employee_code, Employee_Name, Qualification, DOJ,New_Grade, Experience,Gender, Age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
              db.execute(query3,values)
              mydb.commit()


      # ##Table 2 - Salary_Details:

        sheet1 = book.sheet_by_name("2022jan")
        query1 = "INSERT INTO Salary_Details(Employee_code, Employee_Name, Basic, FDA, VDA, DA, HRA, CON, Washing_Allowance, Other_Allowance, Special_Allowance, Total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"



        for x in range(2, sheet1.nrows):
            Employee_code = sheet1.cell(x, 1).value
            Employee_Name = sheet1.cell(x,2).value
            Basic = sheet1.cell(x,10).value
            FDA = sheet1.cell(x,11).value
            VDA = sheet1.cell(x,12).value
            DA = sheet1.cell(x,13).value
            HRA = sheet1.cell(x,14).value
            CON = sheet1.cell(x,15).value
            Washing_Allowance = sheet1.cell(x,16).value
            Other_Allowance = sheet1.cell(x,17).value
            Special_Allowance = sheet1.cell(x,18).value
            Total = sheet1.cell(x,19).value
            # print(Total)

            values1 = (Employee_code, Employee_Name, Basic, FDA, VDA, DA, HRA, CON, Washing_Allowance, Other_Allowance, Special_Allowance, Total)
            db.execute(query1, values1)
    except mysql.connector.errors.DataError:
        print("Data already Inserted")

except:
    print("Unknown Error")

mydb.commit()
db.close()

