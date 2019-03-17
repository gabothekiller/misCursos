class Node:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev

class Queue:
	size = 0
	start = None
	end = None

	def __init__(self):
		self.start = Node(0)
		self.end = Node(0)
		self.start.next = self.end
		self.end.prev = self.start

	def inqueue (self, n):
		n = Node(n, self.end, self.end.prev)
		self.end.prev.next = n
		self.end.prev = n
		self.size += 1

	def dequeue (self):
		if (self.size == 0):
			raise IndexError("Queue empty")

		self.size -= 1
		n = self.start.next
		self.start.next = n.next
		n.next.prev = self.start
		return n.value

q = Queue()
q.inqueue(5)
q.inqueue(10)
q.inqueue(15)

print(q.dequeue())

print(q.dequeue())

print(q.size)

print(q.dequeue())
