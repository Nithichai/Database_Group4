import sqlite3 as db
import os
import csv

class Main_table:
	def __init__(self):
		self.conn = db.connect("gpa.db")

	def create_table(self):
		# create table
		c = self.conn
		with c:
			c = con.cursor()
			c.execute('''
				CREATE TABLE `main` (
					`student_id`	TEXT NOT NULL,
					`year`	INTEGER NOT NULL,
					`semester`	INTEGER NOT NULL,
					`course_code`	TEXT NOT NULL,
					`grade`	TEXT NOT NULL
				);
			''')

	def select_all(self):
		# return list of all elements
		pass

	def insert(self, data):
		# input : row of main table
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("INSERT INTO main_table VALUES (?,?,?,?,?)", data)
			except Exception as e:
				print (e)
			# return status
		pass

	def update(self, headers, data):
		# input : list of header and data
		# return status
		pass

	def delete(self, headers, data):
		# input : list of header and data
		# return status
		pass


################
# read csv and insert to db here
################

main_TB = Main_table()

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
                        main_TB.insert(row)

# x=Main_table()
# x.insert(['5801012610075',2015,1,'055012','3.5'])

