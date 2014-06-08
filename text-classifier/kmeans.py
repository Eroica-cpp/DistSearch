"""
Reference: http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_iris.html
"""

import numpy as np
from sklearn.cluster import KMeans
import cPickle

X = np.array([[1,1], [2, 2], [3, 3], [1, 1]])
est = KMeans(k=3, n_init=1, init='random')
est.fit(X)

def load(path):
	f = open(path)
	key_word_dict = cPickle.load(f)
	f.close()
	return key_word_dict

def get_feature_matrix(key_word_dict):
	bag_of_words = []
	for word_list in key_word_dict.values():
		bag_of_words += word_list

	bag_of_words = sorted(list(set(bag_of_words)))
	dimension = len(bag_of_words)
	
	id_list = sorted(key_word_dict.keys())
	id_num = len(id_list)

	feature_list = []
	for (iden, words) in key_word_dict.items()[:10]:
		# feature = [0] * dimension
		# for word in words:
		# 	feature[bag_of_words.index(word)] += 1
		feature = [words.count(word) for word in bag_of_words]
		feature_list.append(feature)
		print "id:", iden


def main():
	key_word_dict = load("../data/key_word_dict.pickle")

if __name__ == "__main__":
	main()