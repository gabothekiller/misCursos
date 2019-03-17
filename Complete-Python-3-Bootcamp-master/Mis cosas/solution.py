import math

rep = int(input())

for i in range(rep):
	stri  =input()
	li = list(map (int, stri.split()))
	a = li[0]
	b = li[1]
	k = li[2]
	res = 0
	if (k % 2 == 0):
		res =((a - b) * k / 2)
	else:
		res = (a - b) * math.floor(k / 2) + a

	print ("%d" % res)





