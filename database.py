import sqlite3 as db

class Database:

	def __init__(self,database):
		self.conn = db.connect(database)

	def select(self,sql):
		pass

	def insert(self,sql):
		con=self.conn
		with con:
			cur = con.cursor()
			cur.execute(sql)

	def delete(self):
		pass

	def update(self):
		pass

	def create_table(self):
		pass

a = Database('GPAdatabase.db')
a.insert("INSERT INTO Grade VALUES (3.5,'B+')")
