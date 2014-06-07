 # -*- coding: utf-8 -*
"""
This script extracts feature from raw html files
Step 1: parse raw html files by to structured ones
Step 2: chinese tokenizing
Step 3: extract features
"""
from stripHTMLTags import stripHTMLTags
import re
import jieba
import nltk
import string

def load(path):
	f = open(path)
	doc = f.read()
	f.close()
	return doc

def strip_tags(raw_html):
	## strip html tags
	no_html = stripHTMLTags(raw_html.decode("gbk"))
	## strip javascript tags
	no_js = re.sub(r"[A-Za-z\(\)_\s;]*{.*}[A-Za-z\(\)_\s;]*", " ", no_html)
	## strip multiple spaces, 
	plain_text = re.sub(r"\s+", " ", no_js)
	## strip punctuation
	delEStr = list(string.punctuation + string.digits)
	delCStr = list("《》——（）&%￥#@！【】。，；“”：".decode("utf-8"))
	del_list = delEStr + delCStr

	plain_text = "".join([i for i in plain_text if i not in del_list])
	return plain_text

def extract_features(plain_text):
	words = list(jieba.cut(plain_text))
	freqdist = nltk.FreqDist(words)
	
	for (word, freq) in freqdist.items():
		if word != " ":
			print word, freq
	#print " ".join(jieba.cut(plain_text))
	return ""

def main():
	iden = 276109
	path = "../data/board/%d.html" % iden

	raw_html = load(path)
	plain_text = strip_tags(raw_html)
	features = extract_features(plain_text)

if __name__ == "__main__":
	main()

