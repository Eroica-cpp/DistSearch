"""
This script transfers ids to urls.
"""

f = open("../dedicated-crawlers/id_list.txt")
lines = f.read().split("\n")[:-1]
f.close()

f = open("../dedicated-crawlers/url_list.txt", "w")
for line in lines:
	part1 = "http://www.szu.edu.cn/board/view.asp?id="
	iden = line.split(".")[0]
	f.write(part1 + iden + "\n")

f.close()

