"""
filter pages from solr, rearrange them and them return a new JSON string stream.
"""
import urllib2
import simplejson



def get_pages(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	solr_result = simplejson.load(response)
	return dict_list

def main():
	dict_list = get_pages("http://192.168.31.143:8983/solr/collection1/select?q=%E9%AB%98%E6%80%A7%E8%83%BD%E8%AE%A1%E7%AE%97&rows=10&wt=json&indent=true")

	

if __name__ == "__main__":
	main()