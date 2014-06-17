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
			max_num = max(int(iden), int(hist_iden))
			min_num = min(int(iden), int(hist_iden))
			sql = "select sim from sim_doc where id1 = '%d' and id2 = '%d';" % (min_num,max_num)
			cur.execute(sql)
			tmp = cur.fetchall()
			if len(tmp) != 0:
				distance = 1.0 - tmp[0][0]
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
	# print "solr_ids:", solr_ids
	# print "distance_rank:", distance_rank
	index = [solr_ids.index(i) for i in distance_rank]
	return [distance_rank, index]

def hybrid(rank1, rank2):
	"""
	hybrid two ways of ranking results
	"""
	rank_sum = [rank1[i] + rank2[i] for i in range(len(rank1))]
	sorted_list = sorted(rank_sum)
	hybrid_index = [sorted_list.index(i) for i in rank_sum]
	return hybrid_index

def rerank(dict_list, uid):

	history_clicks = get_history_behavior(uid)
	solr_urls = [i["url"] for i in dict_list if i.get("url") is not None]
	solr_ids = [i.split("id=")[1] for i in solr_urls if i.find("id=") >= 0]

	if len(history_clicks) != 0:
		tmp = get_distance_rank(history_clicks, solr_urls)
		distance_rank = tmp[0]
		index = tmp[1]
		# reranked_list = [dict_list[i] for i in index]
	else:
		reranked_list = dict_list
		return reranked_list

	hybrid_index = hybrid(range(1, len(solr_ids) + 1), index)
	reranked_list = [dict_list[i] for i in hybrid_index]
	return reranked_list 

if __name__ == "__main__":
	# rerank()
	# get_history_behavior(uid = "china.litao@163.com")
	get_distance_rank(history_clicks, solr_urls)