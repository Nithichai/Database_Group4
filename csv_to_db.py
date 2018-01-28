import sqlite3 as db
import os
import csv

class MainTable:
	def __init__(self, database):
		self.conn = db.connect(database)
		self.table = "Main"

	def select_all(self):
		con = self.conn
		cur = con.cursor()
		cur.execute("SELECT * FROM main_table")
		return cur.fetchall()

	def insert(self, data):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("PRAGMA foreign_keys = ON")
				cur.execute("INSERT INTO " + self.table + " VALUES (?,?,?,?,?)",data)
			except Exception as e:
				print (data)
				print (e)

	def update(self, data):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("UPDATE main_table SET grade = ? where student_id = ? AND course_code = ?", (data, stu_id, cour_code))
			except Exception as e:
				print (data)
				print (e)

	def delete(self, data):
		# input : list of header and data
		# return status
		pass

################
# read csv and insert to db here
################
main_TB = MainTable("KMUTNBdb.db")
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
