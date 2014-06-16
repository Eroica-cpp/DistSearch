"""
recommender that get a list of pages(dictionary) and rearrange them 
according to users' preference
"""
import MySQLdb

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

	sql = "select site_id from click where uid = '%s';" % uid
	#sql = "select site_id from click where uid = 'test@163.com' "
	cur.execute(sql)
	content = cur.fetchall()
	print content

	cur.close()
	conn.close()
	
	return []

def rerank(dict_list, uid):

	reranked_list = []
	return reranked_list 

if __name__ == "__main__":
	# rerank()
	get_history_behavior(uid = "test@163.com")