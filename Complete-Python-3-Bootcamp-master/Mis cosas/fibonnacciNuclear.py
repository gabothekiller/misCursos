import math

def f ():


n = 10**10
prev = 1
current = 1
l = [1]
while (current < n):

	temp = current
	current = current + prev
	prev = temp
	l.append(prev)
	

print(current)
print (l)


sum = 0
indices = [len(l) -1]
while (True):












