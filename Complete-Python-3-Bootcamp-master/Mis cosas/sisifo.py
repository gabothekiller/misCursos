# <Is>Pathology</Is>
import re

# found: 1234
fin  = open("texto.txt", "r")
fout = open ("out.txt", "w")

for line in fin:
	try:
		found = re.search('<Is>(.+?)</Is>', line).group(1)
		fout.write("{}\n".format(found))
	except AttributeError:
		# AAA, ZZZ not found in the original string
		found = '' # apply your error handling

	

fin.close()
fout.close()

