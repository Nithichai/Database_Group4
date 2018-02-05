import csv
import mysql.connector

def insert(data):
	cnx = mysql.connector.connect(user='root', password='tt054202249',host='localhost',database='kmutnbdb')
	try:
		cursor = cnx.cursor()
		cursor.execute('INSERT INTO kmutnbdb.main_transcrip VALUES (%s,%s,%s,%s,%s)',data)
	except Exception as e:
		print (data)
		print (e)
	cnx.commit()
	cnx.close()
def sql_cmd(sql):
	cnx = mysql.connector.connect(user='root', password='tt054202249',host='localhost',database='kmutnbdb')
	try:
		cursor = cnx.cursor()
		cursor.execute(sql)
	except Exception as e:
		print (data)
		print (e)
	data = cursor.fetchall()
	cnx.close()
	return data

def file(location):
	i=0
	with open(location, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			i += 1
			print(i)
			insert(row)

# file("csv/transaction/Fhox.csv")

sql = '''
SELECT std.std_id, std.std_fname, std.std_lname, SUM(sub.credit* g.grade_id)/ SUM(sub.credit)
FROM main_transcrip m
INNER JOIN student std ON m.std_id = std.std_id
INNER JOIN subject sub ON m.sub_id = sub.sub_id
INNER JOIN grade g ON m.grade_char = g.grade_char
where std.std_id = "5801012620020"
'''

print(sql_cmd(sql))