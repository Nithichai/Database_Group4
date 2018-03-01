import sqlite3 as db
import csv
import time
import random

class Transcript:

    # init by connect to db and set table name
    # parameter : database file name, table name
    # return : none
    def __init__(self, database, table):
        self.conn = db.connect(database)
        self.table = table
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")
        self.commit()

    # close connection
    # parameter : none
    # return : none
    def close(self):
        self.conn.close()

    # commit execution
    # parameter : none
    # return : none
    def commit(self):
        self.conn.commit()

    # import transcript from csv to database
    # parameter : list [student_id, year, semester, course_code, grade]
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

    # insert value into table
    # parameter : list [student_id, year, semester, course_code, grade]
    # return : none
    def insert(self, data):
        try:
            self.cur.execute("INSERT INTO " + self.table + "(student_id, year, semester, course_code, grade_char) VALUES (?,?,?,?,?)", data)
        except Exception as e:
            print("You have error : '%s' : %s" %(str(e), str(data)))

    # reconnect to db and set table name
    # parameter : database file name, table name
    # return : none
    def reconnect(self, database, table):
        self.conn = db.connect(database)
        self.table = table
        self.cur = self.conn.cursor()

    # select all main table
    # parameter : none
    # return : list of value in main table
    def select_all(self):
        self.cur.execute("SELECT * FROM " + self.table)
        return self.cur.fetchall()

    # select some column
    # parameter : none
    # return : list of value in main table
    def select_column(self, col):
        self.cur.execute("SELECT " + col + " FROM " + self.table)
        return self.cur.fetchall()


# dump table in database into list
# parameter : database file name, table name, column
# return : list of data
def list_from_table(database, table, col):
    conn = db.connect(database)
    ls = []
    with conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT " + col + " FROM " + table)
            ls = cur.fetchall()
        except Exception as e:
            print("You have error : '%s'" % str(e))
    new_ls = []
    for l in ls:
        new_ls.append(l[0])
    conn.close()
    return new_ls

grade = list_from_table("Transcript.db", "Grade", "grade_char")
student = list_from_table("Transcript.db", "Student", "student_id")
subject = list_from_table("Transcript.db", "Subject", "course_code")
year = [2015, 2016, 2017]
semester = [1, 2]

transcript = Transcript("Transcript.db", "Transcript")
n = input("Number of data : ")

start_t = time.time()

for i in range(int(n)):
    transcript.insert([random.choice(student), random.choice(year), random.choice(semester), random.choice(subject), random.choice(grade)])
    if i % 1000 == 0:
        transcript.commit()
        print("at %s use time %s" % (str(i), str(time.time() - start_t)))
transcript.commit()

diff_t = time.time() - start_t
transcript.close()

file = open("time_insert.txt", "w+")
file.write("Size : %s, Time : %s" % (n, str(diff_t)))
file.close()
print("at %s use time %s" % (str(n), str(time.time() - start_t)))