a = 15
b = 12

def mcd (a, b):
	if b == 0:
		return a
	elif a == 0:
		return b

	if a > b:
		return mcd(b, a%b)
	else:
		return mcd (a, b%a)


def mcm(a, b):
	return a*b / mcd(a, b)

print (mcm(a, b))

print (mcd(a, b))
