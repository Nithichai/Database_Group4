import sqlite3 as db
import csv

class Database:

	def __init__(self,filedb,table):
		self.table = table
		self.conn = db.connect(filedb)

			# CREATE TABLE `Student` (
			# 	`student_id`	TEXT NOT NULL,
			# 	`firstname`	TEXT NOT NULL,
			# 	`lastname`	TEXT NOT NULL,
			# 	`email`	TEXT NOT NULL,
			# 	`phone`	TEXT NOT NULL,
			# 	PRIMARY KEY(`student_id`)
			# );

			# CREATE TABLE `Subject` (
			# 	`course_code`	TEXT NOT NULL,
			# 	`title`	TEXT NOT NULL,
			# 	`credit`	INTEGER NOT NULL,
			# 	PRIMARY KEY(`course_code`)
			# );

			# CREATE TABLE `Main` (
			# 	`student_id`	TEXT NOT NULL,
			# 	`year`	INTEGER NOT NULL,
			# 	`semester`	INTEGER NOT NULL,
			# 	`course_code`	TEXT NOT NULL,
			# 	`grade_id`	TEXT NOT NULL,
			# 	FOREIGN KEY(`student_id`) REFERENCES `Student`(`student_id`),
			# 	FOREIGN KEY(`course_code`) REFERENCES `Subject`(`course_code`),
			#   FOREIGN KEY(`grade`) REFERENCES `Grade`(`grade_id`)
			# );

			# CREATE TABLE `Grade` (
			# 	`grade_id`	TEXT NOT NULL,
			# 	`grade_char`	TEXT NOT NULL,
			# 	PRIMARY KEY(`grade_id`)
			# );

	def insert(self,data):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("PRAGMA foreign_keys = ON")
				cur.execute("INSERT INTO "+self.table+" VALUES (?,?,?,?,?)",data)
			except Exception as e:
				print (data)
				print (e)

	def selectall(self):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("SELECT * FROM "+self.table)
			except Exception as e:
				print (e)

			data = cur.fetchall()
			for i in range(0,len(data)):
				print(data[i])

	def update(self,column,condition):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute("UPDATE "+self.table+" SET "+column+" WHERE "+condition)
			except Exception as e:
				print (e)

	def delete(self,data):
		con = self.conn
		with con:
		    cur = con.cursor()
		    try:
		        cur.execute("DELETE FROM Main WHERE student_id = ? AND course_code = ? ",data)
		    except Exception as e:
		        print (e)

# dataSTD = [["5801012610091","PUNTAKRN","KUTPARB","a5810091a@gmail.com","0639344400"],
# 		   ["5801012610032","NUTAKRIT","KUTPARB","a5810032a@gmail.com","0639344400"],
# 		   ["5801012610075","SUMKRIT","JERAWAT","JERAWAT@gmail.com","0907598935"],
# 		   ["5801012620256","JIRAWUT","HEWTONG","JIRAWUT@gmail.com","0882583769"],
# 		   ["5801012620088","SONGKARN","LEEMO","KORN@gmail.com","021952826"]]

# x = Database("KMUTNBdb.db","Subject")
# for i in range(0,len(dataSTD)):
# 	x.insert(dataSTD[i])
# x.selectall()
# x.update("phone = '0639344400',email = 'db5810032@gmail.com'","student_id = '5801012610032'")

# y = Database("KMUTNBdb.db","Subject")
# with open("subjects.csv",'r') as csvfile: 
# 	csv_reader = csv.reader(csvfile)
# 	for element in csv_reader: 
# 		y.insert(element)

# ###################### INSERT Main ########################
# z = Database("KMUTNBdb.db","Main")
# with open("transactionTop.csv",'r') as csvfile: 
# 	csv_reader = csv.reader(csvfile)
# 	for element in csv_reader: 
# 		z.insert(element)

z = Database("KMUTNBdb.db","Main")
# z.insert(['5801012620020',2016,1,'010123107','2.3'])
z.delete(['5801012620046','040203111'])

# SELECT std.student_id ,std.firstname,std.lastname,m.course_code,sub.title,g.grade_char
# FROM Main m
# JOIN Student std ON m.student_id = std.student_id
# JOIN Subject sub ON m.course_code = sub.course_code
# JOIN Grade g ON m.grade_id = g.grade_id
# WHERE m.student_id = 5801012610091