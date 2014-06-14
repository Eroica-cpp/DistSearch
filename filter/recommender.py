"""
recommender that get a list of pages(dictionary) and rearrange them 
according to users' preference
"""
import MySQLdb
import os

def get_history_behavior(uid):
	"""
	return a list of page ids that user once clicked, standing on the
	assumption that users prefer clicked pages.
	"""

	## for safety reason, password has been written in local disk and not
	## under version control
	host = "192.168.31.143"
	password = open("password.txt").read()[:-1]

	conn = MySQLdb.connect(host=host, user='cse', passwd=password, db='cse', port=3306, charset='utf8')
	cur = conn.cursor()

	sql = "show tables;"
	cur.execute(sql)
	content = cur.fetchall()
	print content

	cur.close()
	conn.close()
	
	return []

def rearrange(dict_list, uid):
	
	rearranged_list = []
	return rearranged_list 

if __name__ == "__main__":
	# rearrange()
	get_history_behavior(uid = "")