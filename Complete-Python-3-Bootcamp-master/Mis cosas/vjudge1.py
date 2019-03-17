#f = open('input.txt')

def myNextLine():
	return input()

def is_taxi(s):
	#print (s)
	for i in range (len(s) - 1):
		if s[i] != s[i+1]:
			return False

	return True

def is_pizza(s):
	for i in range (len(s) - 1):
		if s[i] <= s[i+1]:
			return False

	return True

def getFriend(phones, name):
	taxi = 0
	girls = 0
	pizza = 0
	for i in range (phones):
		s = myNextLine()
		new_s = s.replace('-', '').strip()
		if is_pizza(new_s):
			pizza += 1
		elif is_taxi(new_s):
			taxi += 1
		else:
			girls += 1

	return (taxi, girls, pizza)

n = int(myNextLine())

max_taxi = {"value" : 0, "people" :[]}
max_girls = {"value" : 0, "people" :[]}
max_pizza = {"value" : 0, "people" :[]}

for i in range (n):
	person = myNextLine().split(' ')
	phones = int(person[0])
	name = person[1].strip()
	result = getFriend(phones, name)

	#print (name, result)

	if (max_taxi["value"] < result[0]):
		max_taxi["value"] = result[0]
		max_taxi["people"] = [name]
	elif max_taxi["value"] == result[0]:
		max_taxi["people"].append(name)


	if (max_girls["value"] < result[1]):
		max_girls["value"] = result[1]
		max_girls["people"] = [name]
	elif max_girls["value"] == result[1]:
		max_girls["people"].append(name)


	if (max_pizza["value"] < result[2]):
		max_pizza["value"] = result[2]
		max_pizza["people"] = [name]
	elif max_pizza["value"] == result[2]:
		max_pizza["people"].append(name)


#print (max_taxi, max_pizza, max_girls )

print ("If you want to call a taxi, you should call: " + ", ".join(max_taxi["people"]) + ".")
print ("If you want to order a pizza, you should call: " + ", ".join(max_pizza["people"]) + ".")
print ("If you want to go to a cafe with a wonderful girl, you should call: " + ", ".join(max_girls["people"]) + ".")


#f.close()