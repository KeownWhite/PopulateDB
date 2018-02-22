import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook("ITCHS_2012.xls")    #open the excel file
sheet = book.sheet_by_name("ITCHS")        #name of the sheet


# Establish a MySQL connection
database = MySQLdb.connect (host="hostname", user = "username", passwd = "pwd", db = "batabase")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()


# Create the INSERT INTO sql query
query = """INSERT INTO final4 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
  itc=sheet.cell(r,0).value
  description = sheet.cell(r,1).value
  hs4   = sheet.cell(r,2).value
  hs5   = sheet.cell(r,3).value
  hs6  = sheet.cell(r,4).value
  hs8 = sheet.cell(r,5).value
  policy  = sheet.cell(r,6).value
  conditions=sheet.cell(r,7).value
  # Assign values from each row
  values =(itc,description,hs4,hs5,hs6,hs8,policy,conditions)
  # Execute sql Query
  try:
      cursor.execute(query, values)
  except:
      pass



# Close the cursor
cursor.close()


# Commit the transaction
database.commit()

# Close the database connection
database.close()
