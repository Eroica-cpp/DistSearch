"""
multi-process approach
"""
import os

def main():
	process_num = 10
	maximum = 300000
	division = int(float(maximum) / process_num)

	for i in range(process_num):
		start = division * i + 1
		end = division * (i + 1)
		print "process id:", i+1
		os.system("python board_crawler.py %d %d &" % (start, end))
		#print start, end

if __name__ == "__main__":
	main()