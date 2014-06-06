"""
This script is used to crawl board pages.
"""
import sys
import urllib2

def get_raw_html(iden):
	
	url = "http://www.szu.edu.cn/board/view.asp?id=%d" % iden
	doc = urllib2.urlopen(url)
	
	## check if swift
	if doc.url == url:
		raw_html = doc.read()
	else:
		raw_html = ""
	
	doc.close()
	return raw_html

def save(iden, raw_html):
	f = open("./raw_html/%d.html" % iden, "w")
	f.write(raw_html)
	f.close()

def main():
	# start = 105558 # last break point
	start = int(sys.argv[1])
	end = int(sys.argv[2])
	id_list = range(start, end+1)

	for iden in id_list:
		raw_html = get_raw_html(iden)
		if raw_html != "":
			save(iden, raw_html)
			print "id: %d, done!" % iden

if __name__ == "__main__":
	main()