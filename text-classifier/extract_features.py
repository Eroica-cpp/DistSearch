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

def save(dict, directory, filename = "data.pickle"):
	f = open(directory + filename, "w")
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

def get_dict_pool(directory = "../data/"):
	files = sorted(os.listdir(directory + "board/"))
	dict_pool = {}
	counter = 0
	for f in files:
		iden = int(f.split(".")[0])
		raw_html = load(directory + "board/" + f)
		plain_text = strip_tags(raw_html)
		freqdist = get_freqdist(plain_text)
		dict_pool[iden] = freqdist
		counter += 1
		print f, "counter =", counter

	print "saving dict_pool..."
	save(dict_pool, directory, filename = "dict_pool.pickle")
	print "saved!"
	
def all_word_freq(directory = "../data/"):
	dict_pool = cPickle.load(directory + "dict_pool.pickle")
	all_words = {}
	for (iden, tmp_dict) in dict_pool.items():
		for (word, counter) in tmp_dict.items():
			if all_words.get(word) is None:
				all_words[word] = counter
			else:
				all_words[word] += counter

	words_num = len(all_words.keys())
	for (word, counter) in all_words.items():
		all_words[word] = float(counter) / words_num

	save(all_words, directory, filename = "all_word_freq.pickle")
	return all_words

def extract_features(directory = "../data/"):
	all_words = cPickle.load(directory + "all_word_freq.pickle")
	dict_pool = cPickle.load(directory + "dict_pool.pickle")

	key_word_dict = {}
	for (iden, word_dict) in dict_pool.items():
		words_num = sum(word_dict.values)
		tmp_list = []
		for (word, counter) in word_dict.items():
			tfidf = float(counter) / (words_num * all_words[word])
			tmp_list.append((word, tfidf))
		## consider words with highest tfidf (ranking first half) as key words
		key_words = sorted(tmp_list, key = lambda x: x[1], reversed = True)[:words_num/2]
		key_word_dict[iden] = key_words

	save(key_word_dict, directory, filename = "key_word_dict.pickle")

def main():
	# iden = 276109
	# path = "../data/board/%d.html" % iden
	pass

if __name__ == "__main__":
	get_dict_pool()

