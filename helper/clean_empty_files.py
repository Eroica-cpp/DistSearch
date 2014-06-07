"""
clean empty files in certain directory
"""
import os

def main():
	path = "../dedicated-crawlers/raw_html/"
	files = os.listdir(path)
	
	counter = 0
	for i in files:
		## check if a file is empty
		## if so, delete the file
		if os.stat(path + i)[6] == 0:
			os.system("rm %s" % (path + i) )
			counter += 1
			print "clean empty file:", i, "counter =", counter

if __name__ == "__main__":
	main()