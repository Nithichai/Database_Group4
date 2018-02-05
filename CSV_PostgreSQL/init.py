import psycopg2
import os
import csv

# Class for manage main table
class MainTable:

	# init by connect to db and set table name
	# parameter : database file name
	# return : none
	def __init__(self, dbname, user, host, password, table):
		self.table = table
		try:
		    self.conn = psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='" + host + "' password='" + password + "'")
		except Exception as e:
		    print(e)

	# insert value into table
	# parameter : list [student_id, year, semester, course_code, grade]
	# return : none
	def insert(self, data):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				# cur.execute("INSERT INTO " + \
				# 	 self.table + \
				# 	 " (student_id, year, semester, course_code, grade_char) VALUES ('" + \
				# 	 str(data[0]) + "','" + \
				# 	 str(data[1]) + "','" + \
				# 	 str(data[2]) + "','" + \
				# 	 str(data[3]) + "','" + \
				# 	 str(data[4]) + "');")
				cur.execute("INSERT INTO " + \
					 self.table + \
					 " (student_id, year, semester, course_code, grade_char) VALUES (%s,%s,%s,%s,%s)", data)
			except Exception as e:
				print (data)
				print (e)


	# import all csv file in folder into table
	# parameter : none
	# return : none
	def import_csv(self):
		file_list = []
		for (dirpath, dirnames, filenames) in os.walk('.'):
			file_list.extend(filenames)
			break
		csv_file_list = [file for file in file_list if file.endswith('.csv')]
		for file in csv_file_list:
			print('reading file:', file)
			with open(file, 'r') as csv_file:
				csv_reader = csv.reader(csv_file, delimiter=',')
				for row in csv_reader:
					self.insert(row)

################
# read csv and insert to db here
################
main_TB = MainTable('KMUTNB_DB', 'postgres', 'localhost', 'qa987654', 'public.main')
# main_TB.insert(['5801012620071', 2015, 1, '010123101', 'A'])
main_TB.import_csv()
