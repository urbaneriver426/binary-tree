class BSTNode:
	
	def __init__(self, key, val, parent):
		self.NodeKey = key # ключ узла
		self.NodeValue = val # значение в узле
		self.Parent = parent # родитель или None для корня
		self.LeftChild = None # левый потомок
		self.RightChild = None # правый потомок

class BSTFind: # промежуточный результат поиска

	def __init__(self):
		self.Node = None # None если 
		# в дереве вообще нету узлов

		self.NodeHasKey = False # True если узел найден
		self.ToLeft = False # True, если родительскому узлу надо 
		# добавить новый узел левым потомком

	def test(self):
		if self.NodeHasKey == True:
			return True
		else:
			return False

class BST:

	def __init__(self, node):
		self.Root = node

	def FindNodeByKey(self, key):
		result = BSTFind()
		if self.Root is None:
			return result
		else:
			result.Node = self.Root
		while True:
			if result.Node.NodeKey == key:
				result.NodeHasKey = True
				return result
			else:
				if result.Node.NodeKey > key:
					result.ToLeft = True
					if result.Node.LeftChild is None:
						return result
					else:
						result.Node = result.Node.LeftChild
				else:
					result.ToLeft = False
					if result.Node.RightChild is None:
						return result
					else:
						result.Node = result.Node.RightChild

	def AddKeyValue(self, key, val):
		node = self.FindNodeByKey(key)
		if node.NodeHasKey is True:
			return False
		if node.Node is None:
			self.Root = BSTNode(key, val, None)
		else:
			if node.ToLeft is True:
				node.Node.LeftChild = BSTNode(key, val, node.Node)
			else:
				node.Node.RightChild = BSTNode(key, val, node.Node)
			return True
  
	def FinMinMax(self, FromNode, FindMax):
		if self.Root is not None:
			if FindMax == True:
				while True:
					if FromNode.RightChild is not None:
						FromNode = FromNode.RightChild
					else:
						return FromNode
			else:
				while True:
					if FromNode.LeftChild is not None:
						FromNode = FromNode.LeftChild
					else:
						return FromNode
		return None
	
	def DeleteNodeByKey(self, key):
		d_node = self.FindNodeByKey(key).Node
		if self.FindNodeByKey(key).NodeHasKey is False:
			return False
		if d_node.RightChild is None:
			if d_node.LeftChild is None: 
				if d_node is self.Root:
					self.Root = None
				elif d_node is d_node.Parent.LeftChild:
					d_node.Parent.LeftChild = None
				else:
					d_node.Parent.RightChild = None
			else:
				if d_node is d_node.Parent.LeftChild: 
					d_node.Parent.LeftChild = d_node.LeftChild 
				else:											
					d_node.Parent.RightChild = d_node.LeftChild 	
		else:
			r_node = self.FinMinMax(d_node.RightChild, False)
			
			r_node.Parent = d_node.Parent
			if r_node.Parent is not None:
				if d_node.Parent.LeftChild is d_node:
					d_node.Parent.LeftChild = r_node
				elif d_node.Parent.RightChild is d_node:
					d_node.Parent.RightChild = r_node
			else:
				self.Root = r_node
			if d_node.LeftChild is not None:
				r_node.LeftChild = d_node.LeftChild
				r_node.LeftChild.Parent = r_node
			if d_node.RightChild is not r_node:
				if r_node.RightChild is not None:
					d_node.RightChild.Parent = self.FinMinMax(r_node.RightChild, True)
					self.FinMinMax(r_node.RightChild, True).RightChild = d_node.RightChild
				else: 
					r_node.RightChild = d_node.RightChild
		return True

	def Count(self, node = None):
		count = 0
		if node is None:
			if self.Root is None:
				return count
			else:
				node = self.Root
				if node.RightChild is None and node.LeftChild is None:
					return 1
		if node.LeftChild is not None and node.RightChild is not None:
			count = 2
			if node is self.Root:
				count += 1
			return count +self.Count(node.LeftChild)+self.Count(node.RightChild)
		elif node.LeftChild is not None:
			count = 1
			if node is self.Root:
				count += 1
			return count + self.Count(node.LeftChild)
		elif node.RightChild is not None:
			count = 1
			if node is self.Root:
				count += 1
			return count + self.Count(node.RightChild)
		else:
			return 0
