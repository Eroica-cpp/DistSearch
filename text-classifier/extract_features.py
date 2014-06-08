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
import os
import sys
import cPickle

def load(path):
	f = open(path)
	doc = f.read()
	f.close()
	return doc

def save(dict, directory):
	f = open(directory + "data.pickle", "w")
	cPickle.dump(dict, f)
	f.close()
	return

def strip_tags(raw_html):
	plain_text = ""
	try:
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
	except UnicodeDecodeError:
		print "'gbk' codec can't decode bytes in position 6746-6747: illegal multibyte sequence"

	tmp_text = ""
	for i in plain_text:
		if i not in del_list:
			tmp_text += i
		else:
			tmp_text += " "
	plain_text = tmp_text
	return plain_text

def get_freqdist(plain_text):
	words = list(jieba.cut(plain_text))
	freqdist = nltk.FreqDist(words)
	return freqdist

def get_dict_pool(directory = "../data/board/"):
	files = sorted(os.listdir(directory))
	dict_pool = {}
	counter = 0
	for f in files:
		iden = int(f.split(".")[0])
		raw_html = load(directory + f)
		plain_text = strip_tags(raw_html)
		freqdist = get_freqdist(plain_text)
		dict_pool[iden] = freqdist
		counter += 1
		print f, "counter =", counter

	print "saving dict_pool..."
	save(dict_pool, directory)
	print "saved!"
	
def main():
	# iden = 276109
	# path = "../data/board/%d.html" % iden
	pass
	



if __name__ == "__main__":
	get_dict_pool()

