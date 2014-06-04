"""
This script is used to crawl board pages.
"""
import urllib2

def get_raw_html(iden):
	
	url = "http://www.szu.edu.cn/board/view.asp?id=%d" % iden
	doc = urllib2.urlopen(url)
	
	## check if swift
	if doc.url == url:
		raw_html = doc.read() #.decode("gbk")
	else:
		raw_html = ""
	
	doc.close()
	return raw_html

def save(iden, raw_html):
	f = open("./raw_html/%d.html" % iden, "w")
	f.write(raw_html)
	f.close()

def main():
	
	id_list = [100, 1000, 279207]

	for iden in id_list:
		raw_html = get_raw_html(iden)
		save(iden, raw_html)

if __name__ == "__main__":
	main()