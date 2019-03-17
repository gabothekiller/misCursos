n = 120120

p = [2, 3, 5, 7, 11, 13, 17, 19]


def d (n):
	for e in p:
		if n % e == 0:
			return False
	return True


found = False
while (not found):
	n += 1
	if (d(n)):
		found = True

print(n)

