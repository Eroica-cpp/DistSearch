"""
filter pages from solr, rearrange them and them return a new JSON string stream.
"""
import urllib2
import re
import json
import recommender

def is_valid(url):
	"""
	check if url is valid
	"""
	return url.find("select") >= 0

def refine(tmp_dict):
	"""
	rearrange dictionary, e.g. rearrange keys and values for board pages.
	"""
	new_dict = {}
	new_dict["url"] = tmp_dict["url"]
	new_dict["id"] = tmp_dict["id"]
	raw_content = tmp_dict["content"]
	obj = re.search(r"(.*)(\d{4}-\d+-\d+\s\d+:\d+:\d+)(.*)(\d{4}-\d+-\d+\s\d+:\d+:\d+)(.*)", raw_content)

	tmp1 = obj.group(1).split()
	new_dict["title"] = tmp1[-2]
	new_dict["department"] = tmp1[-1]
	new_dict["date"] = obj.group(2)
	new_dict["content"] = obj.group(3) + obj.group(4) + ")"

	## test code
	# print "="*100	
	# print "\n".join(new_dict.values())
	# print "="*100

	return new_dict

def get_result_list(url, uid = ""):
	"""
	return search results of solr, which is a list of python dictionaries.
	"""
	if not is_valid(url):
		print "ERROR: url is not valid."
		return []
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	solr_result = json.load(response)
	dict_list = solr_result.items()[1][1]["docs"]
	
	## refine content from raw html.
	new_dict_list = []
	for tmp_dict in dict_list:
		## if the html is board page, refine and rearrange it.
		if tmp_dict.get("url").find("board/view.asp") >= 0:
			new_dict_list.append(refine(tmp_dict))

	## return rearrange and recommend results
	if uid != "":
		return recommender.rearrange(new_dict_list, uid)

	return new_dict_list

def get_json(url):
	dict_list = get_result_list(url)
	return json.dumps(dict_list)

def main():
	"""
	test code
	"""
	url = "http://192.168.31.143:8983/solr/collection1/select?q=%E5%85%AC%E6%96%87%E9%80%9A&rows=100&wt=json&indent=true"
	dict_list = get_result_list(url)

	print "len(dict_list) =", len(dict_list)

	print type(get_json(url))
	# print get_json(url)

if __name__ == "__main__":
	main()