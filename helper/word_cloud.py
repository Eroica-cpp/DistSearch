
print "loading file"
f = open("/media/disk/Dropbox/projects/courseRecordAnalysis/data/studentCourseRecord.txt")
lines = f.read().split("\n")[:-1]
f.close()
print "load complete"

length = len(lines)

step = 1000
counter = 4
f = open("../data/wordcloud_subset5.txt", "w")
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