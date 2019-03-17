



def M (n):
	return 2 ** n -1 


def s (n):
	if (n == 1):
		return 4
	else :
		return s(n-1)**2 - 2 

print (M(11))
print (s(10))