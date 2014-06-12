"""
filter pages from solr, rearrange them and them return a new JSON string stream.
"""
import urllib2
import simplejson

def is_valid(url):
	"""
	check if url is valid
	"""
	return url.find("select") >= 0

def get_result_list(url):
	"""
	return search results of solr, which is a list of python dictionaries.
	"""
	if not is_valid(url):
		print "ERROR: url is not valid."
		return []
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	solr_result = simplejson.load(response)
	dict_list = solr_result.items()[1][1]["docs"]
	return dict_list

def get_json(url):
	dict_list = get_result_list(url)
	return simplejson.dumps(dict_list)

def main():
	"""
	test code
	"""
	url = "http://192.168.31.143:8983/solr/collection1/select?q=%E9%AB%98%E6%80%A7%E8%83%BD%E8%AE%A1%E7%AE%97&rows=10&wt=json&indent=true"
	dict_list = get_result_list(url)

	print "len(dict_list) =", len(dict_list)

	print type(get_json(url))

if __name__ == "__main__":
	main()