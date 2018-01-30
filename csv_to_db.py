import sqlite3 as db
import os
import csv

# Class for manage main table
class MainTable:

	# init by connect to db and set table name
    # parameter : database file name
    # return : none
	def __init__(self, database):
		self.table = "Main"
		self.conn = db.connect(database)

	# select all main table
    # parameter : none
    # return : list of value in main table
	def select_all(self):
		con = self.conn
		cur = con.cursor()
		cur.execute("SELECT * FROM " + self.table)
		return cur.fetchall()

	# show all value from main table
	# parameter : none
	# return : none
	def show_all(self):
		list_main = self.select_all()
		print("==========================")
		for data in list_main:
			print("student_id : %s" % data[0])
			print("year : %s" % data[1])
			print("semester : %s" % data[2])
			print("couser_code : %s" % data[3])
			print("grade_char : %s" % data[4])
			print("==========================")

	# insert value into table
	# parameter : list [student_id, year, semester, course_code, grade]
	# return : none
	def insert(self, data):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("PRAGMA foreign_keys = ON")
				cur.execute("INSERT INTO " + self.table + " VALUES (?,?,?,?,?)", data)
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

	# update value in table that ref by student_id and course_code
	# parameter : list [grade, student_id, course_code]
	# return : none
	def update(self, data):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("UPDATE "+ self.table + " SET grade_char = ? WHERE student_id = ? AND course_code = ?", data)
			except Exception as e:
				print (data)
				print (e)

	# delete value in table that ref by student_id and course_code
	# parameter : list [student_id, course_code]
	# return : none
	def delete(self, data):
		con = self.conn
		with con:
		    cur = con.cursor()
		    try:
		        cur.execute("DELETE FROM " + self.table + " WHERE student_id = ? AND course_code = ? ", data)
		    except Exception as e:
		        print (e)

################
# read csv and insert to db here
################
main_TB = MainTable("KMUTNBdb.db")
main_TB.import_csv()
