import io

f = io.open("inmuebles.txt", "r", encoding="utf-8")
out = open ("inmuebles_res.txt", "w")

table_head = "sector	2010-I	2010-II	2010-III	2010-IV	2011-I	2011-II	2011-III	2011-IV	2012-I	2012-II	2012-III	2012-IV	2014-I	2014-II	2014-III	2014-IV	2015-I	2015-II	2015-III	2015-IV	2016-I	2016-II	2016-III	2016-IV	2017-I	2017-II	2017-III	2017-IV	2018-I	2018-II	2018-III	2018-IV\n" 

out.write(table_head)


for table in range(0, 26):
	# reading headings 
	sector = f.readline().replace("\t", "").replace("\n", "")
	trash = f.readline()

	print (sector)
	print (trash)

	out.write(sector + "\t")

	data = []
	for quarter in range(0, 4):
		# reading 
		data.append(f.readline().split("\t"))
		
	for col in range (1, len(data[0])):	
		for row in range(0, len(data)):
			out.write(data[row][col].replace("\n", "") + "\t")		

	#writing
	out.write("\n")

	
f.close()
out.close()