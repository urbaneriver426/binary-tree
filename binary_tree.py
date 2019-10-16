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

class BST:

	def __init__(self, node):
		self.Root = node # корень дерева, или None

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
		del_node = self.FindNodeByKey(key)
		if del_node.NodeHasKey is False:
			return False
		if del_node.Node.RightChild is None:
			if del_node.Node.LeftChild is None:
				if del_node.Node.Parent.LeftChild is del_node:
					del_node.Node.Parent.LeftChild = None
				else:
					del_node.Node.Parent.RightChild = None
			else:
				if del_node.Node.Parent.LeftChild is del_node.Node:
					del_node.Node.Parent.LeftChild = del_node.Node.LeftChild
				else:
					del_node.Node.Parent.RightChild = del_node.Node.LeftChild
		else:
			rep_node = self.FinMinMax(del_node.Node.RightChild, False)
			rep_node.LeftChild = None
			if del_node.Node.LeftChild is not None:
				del_node.Node.LeftChild.Parent = rep_node
			if del_node.Node.RightChild is not None:
				del_node.Node.RightChild.Parent = rep_node
			if rep_node is not del_node.Node.LeftChild:
				rep_node.LeftChild = del_node.Node.LeftChild
			if rep_node is not del_node.Node.RightChild:
				rep_node.RightChild = del_node.Node.RightChild
			rep_node.Parent = del_node.Node.Parent
			if rep_node.Parent is not None:
				if del_node.Node.Parent.LeftChild is del_node.Node:
					del_node.Node.Parent.LeftChild = rep_node
				elif del_node.Node.Parent.RightChild is del_node.Node:
					del_node.Node.Parent.RightChild = rep_node
			else:
				self.Root = rep_node


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
