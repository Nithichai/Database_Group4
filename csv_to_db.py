import sqlite3 as db

class MainTable:
	def __init__(self):
		self.conn = db.connect("gpa.db")

	def select_all(self):
		# return list of all elements
		pass

	def insert(self, data):
		# input : row of main table
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

	def close():
		conn.close()

################
# read csv and insert to db here
################
