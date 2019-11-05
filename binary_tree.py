class BSTNode:
	
	def __init__(self, key, val, parent):
		self.NodeKey = key 
		self.NodeValue = val 
		self.Parent = parent 
		self.LeftChild = None 
		self.RightChild = None 

	def GetLeftChild(self):
		return node.LeftChild

	def GetRightChild(self):
		return self.RightChild

	def GetValue(self):
		return self.NodeValue

	def GetKey(self):
		return self.NodeKey

class BSTFind:

	def __init__(self):
		self.Node = None
		

		self.NodeHasKey = False 
		self.ToLeft = False

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
					d_node.LeftChild.Parent = d_node.Parent
				else:											
					d_node.Parent.RightChild = d_node.LeftChild
					d_node.LeftChild.Parent = d_node.Parent 	
		else:
			r_node = self.FinMinMax(d_node.RightChild, False)
			if r_node is r_node.Parent.LeftChild:
				r_node.Parent.LeftChild = None
			else:
				r_node.Parent.RightChild = None
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

	def Count(self):
		return len(self.WideAllNodes())

	def WideAllNodes(self):
		queue = []
		result = tuple()
		if self.Root is not None:
			queue.append(self.Root)
		while len(queue) > 0:
			if queue[0].LeftChild:
				queue.append(queue[0].LeftChild)
			if queue[0].RightChild:
				queue.append(queue[0].RightChild)
			result += (queue.pop(0), )			
		return result

	def InOrder(self, node):
		if node is None:
			return tuple()
		return self.InOrder(node.LeftChild) + (node,) + self.InOrder(node.RightChild)

	def PreOrder(self, node):
		if node is None:
			return tuple()
		return (node,) + self.PreOrder(node.LeftChild) +  self.PreOrder(node.RightChild)

	def PostOrder(self, node):
		if node is None:
			return tuple()
		return self.PostOrder(node.LeftChild) +  self.PostOrder(node.RightChild) + (node,)

	def DeepAllNodes(self, order):
		if order == 0:
			return self.InOrder(self.Root)
		if order == 1:
			return self.PostOrder(self.Root)
		if order == 2:
			return self.PreOrder(self.Root)
