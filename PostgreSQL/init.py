import psycopg2
import os
import csv

# Class for manage main table
class Transcript:

    # init by connect to db and set table name
    # parameter : database name, username, host, password, table name
    # return : none
    def __init__(self, dbname, user, host, password, table):
        try:
            self.conn = psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='" + host + "' password='" + password + "'")
            self.table = table
            self.cur = self.conn.cursor()
        except Exception as e:
            print("You have error : '%s'" %(str(e)))

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
        try:
            self.conn = psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='" + host + "' password='" + password + "'")
            self.table = table
            self.cur = self.conn.cursor()
        except Exception as e:
            print("You have error : '%s'" %(str(e)))

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
def list_from_table(dbname, user, host, password, table, col):
    conn = psycopg2.connect("dbname='" + dbname + "' user='" + user + "' host='" + host + "' password='" + password + "'")
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

grade = list_from_table('postgres', 'postgres', 'localhost', 'qa987654', 'public."grade"', 'grade_char')
student = list_from_table('postgres', 'postgres', 'localhost', 'qa987654', 'public."student"', 'student_id')
subject = list_from_table('postgres', 'postgres', 'localhost', 'qa987654', 'public."subject"', 'course_code')
year = [2015, 2016, 2017]
semester = [1, 2]
transcript = Transcript('postgres', 'postgres', 'localhost', 'qa987654', 'public."transcript"')
file = open("time_insert.txt", "a+")
n = input("Number of data : ")

start_t = time.time()

for i in range(int(n)):
    transcript.insert([random.choice(student), random.choice(year), random.choice(semester), random.choice(subject), random.choice(grade)])
    if i % 1000 == 0:
        print("at %s use time %s" % (str(i), str(time.time() - start_t)))
    if i % 1000000 == 0: 
        file.write("Size : %s, Time : %s" % (i, str(time.time() - start_t)))
transcript.commit()

diff_t = time.time() - start_t
print("at %s use time %s" % (str(n), str(diff_t)))
file.write("Size : %s, Time : %s" % (n, str(diff_t)))

transcript.close()
file.close()
