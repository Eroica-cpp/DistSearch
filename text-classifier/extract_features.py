"""
This script extracts feature from raw html files
Step 1: parse raw html files by to structured ones
Step 2: chinese tokenizing
Step 3: extract features
"""
from stripHTMLTags import stripHTMLTags
import re

def load(path):
	f = open(path)
	doc = f.read()
	f.close()
	return doc

def strip_tags(raw_html):
	## strip html tags
	not_html = stripHTMLTags(raw_html.decode("gbk"))
	## strip javascript tags
	not_js = re.sub(r"[A-Za-z\(\)_\s;]*{.*}[A-Za-z\(\)_\s;]*", " ", not_html)
	
	plain_text = not_js
	return plain_text

def extract_features(plain_text):
	return ""

def main():
	iden = 276109
	path = "../data/board/%d.html" % iden

	raw_html = load(path)
	plain_text = strip_tags(raw_html)
	print plain_text
	features = extract_features(plain_text)


if __name__ == "__main__":
	main()

