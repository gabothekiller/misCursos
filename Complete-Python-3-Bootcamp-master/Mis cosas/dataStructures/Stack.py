class Stack:
	def __init__(self):
		self.stack = list()
		self.size = 0

	def push(self, element):
		self.size += 1
		self.stack.append(element)

	def pop(self):
		self.size -= 1
		return self.stack.pop()

	def isEmpty(self):
		return self.size == 0