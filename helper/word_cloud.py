
print "loading file"
f = open("/media/disk/Dropbox/projects/courseRecordAnalysis/data/studentCourseRecord.txt")
lines = f.read().split("\n")[:-1]
f.close()
print "load complete"

length = len(lines)

step = 200
for i in range(5):
	counter = 0
	f = open("../data/wordcloud_subset%d.txt" % i, "w")
	for line in lines:
		if counter % step == 0:
			tmp = line.split("\t")
			course_name = tmp[3]
			teacher = tmp[14]
			f.write(course_name + "\t" + teacher + "\n")
		counter += 1
		if counter % 100000 == 0:
			print "counter =", counter, "done!"

	f.close()