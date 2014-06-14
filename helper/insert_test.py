"""
test code of inserting records into MySQL database
"""
import MySQLdb
import sys

password = sys.argv[1]

conn = MySQLdb.connect(host='192.168.31.143', user='cse', passwd=password, db='cse', port=3306, charset='utf8')
cur = conn.cursor()

f = open("../data/simDoc_realID.txt")
counter = 0
for line in f:
	tmp = line.split()
	id1 = tmp[0]
	id2 = tmp[1]
	sim = tmp[2]

	sql = "insert into sim_doc values (%s, %s, %s)" % (id1, id2, sim)
	cur.execute(sql)

	counter += 1
	if counter % 100000 == 0:
		conn.commit()
		print "counter =", counter

f.close()

conn.commit()
cur.close()
conn.close()