numbers = [4, 3, 6, 7, 1]
numbers_length = len(numbers)
sums = [0]
count = 0

listg = [0, 4, 3, 6, 7, 1, 7, 13, 20, 21, 14, 14, 15, 8, 10, 17, 18, 11, 11, 12, 5, 9, 16, 17, 10, 10, 11, 4, 13, 14, 7, 8]

def search_rec(prev_sum, pos, numbers, numbers_length, result):
	count = 1
	s = prev_sum + numbers[pos]
	result.append(s)
	for i in range (pos + 1, numbers_length):
		count += search_rec(s, i, numbers, numbers_length, result)
	return count


def search(numbers):
	count = 0
	result = [0]
	numbers_length = len (numbers)
	for i in range (0, numbers_length):
		count += search_rec(0, i, numbers, numbers_length, result)
	return (count, result)


c = search(number)
print(sums)
print(listg)
print(c)




