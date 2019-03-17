
def f(n):
	return sum([int(digit)**4 for digit in str(n)])

l = []
for i in range(1, 10**7 + 1):
	if i == f(i):
		l.append(i)

print(l)
print(len(l))
print(l[-1])