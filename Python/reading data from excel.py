import xlrd3

book = xlrd3.open_workbook("D:/pythonfiles/payscale.xlsx")
sheet = book.sheet_by_name("jan2022")



for r in range(2, sheet.nrows):

  S_No= sheet.cell(r,0).value
  Employee_code= sheet.cell(r,1).value
  Employee_Name = sheet.cell(r,2).value
  Qualification= sheet.cell(r,3).value
  DOJ= sheet.cell(r,4).value
  New_Grade = sheet.cell(r, 5).value
  Experience = sheet.cell(r,6).value
  Age= int(sheet.cell(r,7).value)

  print(Employee_Name)
