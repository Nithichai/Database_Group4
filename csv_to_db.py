import sqlite3 as db
import csv
import sys

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
		con = self.conn
		cur = con.cursor()
		cur.execute("SELECT * FROM main_table")
		return cur.fetchall() 
			


	def insert(self, data):
		# input : row of main table
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("INSERT INTO main_table VALUES (?,?,?,?,?)", data)
				return c.fetchone()
			except Exception as e:
				print (e)
			# return status
		pass

	def update(self, stu_id, cour_code, data):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("UPDATE main_table SET grade = ? where student_id = ? AND course_code = ?", (data, stu_id, cour_code))
			except Exception as e:
				print (e)

	def delete(self, headers, data):
		# input : list of header and data
		# return status
		pass


################
# read csv and insert to db here
################

main_TB = Main_table()
main_TB.update(5801012630050, 10123102, 4)
print main_TB.select_all()

# x=Main_table()
# x.insert(['5801012610075',2015,1,'055012','3.5'])

