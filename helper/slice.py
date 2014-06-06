
def write(iteration, line):
	f = open("./interation_%d.txt" % iteration, "a")
	f.write(line + "\n")
	f.close()

def main():
	f = open("../SZU_Crawl_1_20140601.out")
	lines = f.read().split("\n")[:-1]
	f.close()

	iteration = 0
	for line in lines:
		if line.find("Iteration") >= 0:
			iteration += 1
		write(iteration, line)

if __name__ == "__main__":
	main()
