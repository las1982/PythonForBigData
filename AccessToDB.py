import sys
sys.path.append("C:\Python Libs")
import pymssql
import pandas

FilePath = r"C:\Users\dhql\Documents\3_Phishing\ISA dev.sql"
with open(FilePath, 'r') as f:
    sql = f.read() 

conn = pymssql.connect(
	server='GMWCNSQLV00070',
	database='CSRMAR_D'
	)
cursor = conn.cursor()
cursor.execute(sql)

ColNames = []
for i in cursor.description:
	ColNames.append(i[0]) 

row = cursor.fetchone()
tbl = []
while row:
    tbl.append(row)   
    row = cursor.fetchone()
df = pandas.DataFrame(tbl, columns = ColNames)
print df
