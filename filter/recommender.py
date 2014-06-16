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

	sql = "select site_id from click where uid = '%s';" % uid
	#sql = "select site_id from click where uid = 'test@163.com' "
	cur.execute(sql)
	click_pages = [i[0] for i in cur.fetchall()]
	print click_pages

	cur.close()
	conn.close()
	
	history_behavior = click_pages
	return history_behavior

def get_distance_rank(history_clicks, solr_urls):

	## get history_ids and ids of solr results
	history_ids = [i.split("id=")[1] for i in history_clicks if i.find("id=") >= 0]
	solr_ids = [i.split("id=")[1] for i in solr_urls if i.find("id=") >= 0]
	
	## for safety reason, password has been written in local disk and not
	## under version control
	host = "192.168.31.143"
	password = open("password.txt").read()[:-1]

	conn = MySQLdb.connect(host=host, user='cse', passwd=password, db='cse', port=3306, charset='utf8')
	cur = conn.cursor()

	info = {}
	for iden in solr_ids:
		for hist_iden in history_ids:
			# print "iden =", iden, "hist_iden =", hist_iden
			max_num = max(int(iden), int(hist_iden))
			min_num = min(int(iden), int(hist_iden))
			sql = "select sim from sim_doc where id1 = '%d' and id2 = '%d';" % (min_num,max_num)
			cur.execute(sql)
			tmp = cur.fetchall()
			if len(tmp) != 0:
				distance = tmp[0][0]
			else:
				distance = 1.0
			if info.get(iden) is None:
				info[iden] = distance
			else:
				info[iden] += distance

	cur.close()
	conn.close()

	tmp = info.items()
	sorted_tmp = sorted(tmp, key = lambda x: x[1])
	distance_rank = [i[0] for i in sorted_tmp]
	return distance_rank

def rerank(dict_list, uid):

	history_clicks = get_history_behavior(uid)
	solr_urls = [i["url"] for i in dict_list if i.get("url") is not None]

	if len(history_clicks) != 0:
		distance_rank = get_distance_rank(history_clicks, solr_urls)
	
	## test code
	os.system("echo date >> date.txt")

	reranked_list = dict_list
	return reranked_list 

if __name__ == "__main__":
	# rerank()
	# get_history_behavior(uid = "china.litao@163.com")
	get_distance_rank(history_clicks, solr_urls)