class Queue:
	def __init__(self):
		self.queue = list()
		self.size = 0

	def enqueue(self, element):
		self.queue.insert(0, element)
		self.size += 1

	def dequeue (self):
		self.size -= 1
		return self.queue.pop()

	def isEmpty(self):
		return self.size == 0