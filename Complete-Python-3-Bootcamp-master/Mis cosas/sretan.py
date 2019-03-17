sumAfter = 0
sumPrev = 0 
count = 0
n = int (input())

def tobin (result, diff):
	for i in range (len(result)-1, -1, -1):
		result[i] = diff % 2
		diff = int (diff / 2)
		if diff == 1:
			result[i-1] = 1
			break
	return result


def printResult (result):
	for e in result:
		if (e == 0):
			print ("4", end="")
		else :
			print ("7", end="")
	print()

while not(n <= sumAfter):
	count += 1 
	sumPrev = sumAfter
	sumAfter += 2**count


#print (str(count) +  "    " +  str(sumAfter) + "    " + str(sumPrev) + "   ")
result = [0] * count
#print (result)
diff = n - sumPrev - 1

result = tobin(result, diff)
printResult(result)



