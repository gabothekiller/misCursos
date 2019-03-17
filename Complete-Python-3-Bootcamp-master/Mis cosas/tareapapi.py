from openpyxl import Workbook




f = open("papis.txt", "r", errors="ignore") 
out = open("salida.txt", "w")
COLUMS = 6
count = 0
while True:
	line = f.readline()
	if line == "":
		break


	if "]" in line:
		for i in range(0, 5):
			f.readline()
		continue

	out.write(line.rstrip('\n'))
	out.write("\t")
	count += 1
	if (count == COLUMS):
		out.write("\n")
		count = 0

	


f.close()
out.close()
