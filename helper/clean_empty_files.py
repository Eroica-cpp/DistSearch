"""
clean empty files in certain directory
"""
import os

def main():
	path = "../dedicated-crawlers/raw_html/"
	files = os.listdir(path)
	
	for i in files:
		## check if a file is empty
		## if so, delete the file
		if os.stat(path + i)[6] == 0:
			os.system("rm %s" % (path + i) )

if __name__ == "__main__":
	main()