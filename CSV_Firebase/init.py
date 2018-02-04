from firebase import firebase
import os
import csv

# Class for manage main table
class MainTable:

	# init by connect to db and set table name
	# parameter : database file name
	# return : none
	def __init__(self, database):
		self.fb = firebase.FirebaseApplication('https://nithichaisoftwareengkmutnb.firebaseio.com/', None)
		self.index = 0

	# insert value into table
	# parameter : uri, list [student_id, year, semester, course_code, grade]
	# return : none
	def insert(self, uri, data):
		data_set = {
			"student_id" : data[0],
			"year" : data[1],
			"semester" : data[2],
			"course_code" : data[3],
			"grade_char" : data[4]
		}
		try:
			result = self.fb.put(url=uri, name=self.index, data=data_set)
		except Exception as e:
			print(e)

	# import all csv file in folder into table
	# parameter : none
	# return : none
	def import_csv(self, uri):
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
					self.insert(uri, row)
					self.index += 1

################
# read csv and insert to db here
################
main_TB = MainTable("KMUTNBdb.db")
main_TB.import_csv('/main')
