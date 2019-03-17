# cute

from TreeNode import TreeNode
from Stack import Stack
from Queue import Queue
class MyBST:
	def __init__(self):
		self.size = 0
		self.root = None

	@staticmethod
	def heightNode(node):
		return 0 if node is None else 1 + max(MyBST.heightNode(node.left), MyBST.heightNode(node.right))

	def height(self):
		return self.heightNode(self.root)

	def insertNode(self, node, newNode):
		if node is None:
			return newNode
		elif node.value < newNode.value:
			node.right = self.insertNode(node.right, newNode)
		elif node.value > newNode.value:
			node.left = self.insertNode(node.left, newNode)
		return self.balance(node)


	"""
	# balances a node if needed. Making this an AVL Tree
	"""
	def balance(self, node):
		leftChildHeight = self.heightNode(node.left)
		rightChildHeight = self.heightNode(node.right)
		# LADO DERECHO
		if rightChildHeight - leftChildHeight == 2:
			right_left_height = self.heightNode(node.right.left)
			right_right_height = self.heightNode(node.right.right)

			# LADO DERECHO DERECHO 
			if right_left_height > right_right_height:
				node.right = self.rotateRight(node.right)
			
			return self.rotateLeft(node)
			
		# LADO IZQUIERDO
		elif leftChildHeight - rightChildHeight == 2:
			left_left_height = self.heightNode(node.left.left)
			left_right_height = self.heightNode(node.left.right)

			# LADO IZQUIERDO DERECHO
			if left_right_height > left_left_height:
				node.left = self.rotateLeft(node.left)
			return self.rotateRight(node)
		return node


	def insert(self, element):
		newNode = TreeNode(element)
		self.root = self.insertNode(self.root, newNode)



	def DFS(self):
		s = Stack()
		s.push(self.root)
		while not s.isEmpty():
			node = s.pop()
			if node is None:
				continue

			print (node.value, end = ' ')
			s.push(node.right)
			s.push(node.left)
		print()

	def BFS (self):
		s = Queue()
		s.enqueue(self.root)
		while not s.isEmpty():
			node = s.dequeue()
			if node is None:
				continue

			print (node.value, end = ' ')
			s.enqueue(node.right)
			s.enqueue(node.left)
		print()

		
	def printPreOrderNode(self, node):
		if node is not None:
			print(node.value, end=' ')
			self.printPreOrderNode(node.left)
			self.printPreOrderNode(node.right)

	def printPreOrder(self):
		self.printPreOrderNode(self.root)
		print()

	def rotateRight(self, node):
		leftChild = node.left
		rotatingBranch = leftChild.right
		
		# do rotation to the left
		leftChild.right = node
		node.left = rotatingBranch
		return leftChild

	def rotateLeft(self, node):
		rightChild = node.right
		rotatingBranch = rightChild.left
		
		# do rotation to the right
		rightChild.left = node
		node.right = rotatingBranch
		return rightChild

if __name__ == "__main__":
	bst = MyBST()
	print("height : " + str(bst.height()))
	bst.insert(1)
	print("height : " + str(bst.height()))
	bst.insert(2)
	print ("---")
	bst.insert(3)
	bst.insert(4)
	bst.insert(15)
	bst.insert(12)
	bst.insert(21)
	bst.insert(22)
	bst.insert(60)
	bst.insert(17)
	print("height : " + str(bst.height()))
	bst.printPreOrder()


	bst.DFS()
	bst.BFS()
