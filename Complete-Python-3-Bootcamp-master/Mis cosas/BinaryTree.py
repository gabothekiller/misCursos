class BinaryNode:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

class BiaryTree:
	def __init__(self):
		root = None

	def insert(self, new):
		if self.root is None:
			self.root = BinaryNode(new)
			
