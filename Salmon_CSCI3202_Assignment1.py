# Salmon_Assignment1.py
# Name: Brian Salmon
# Email: brian.salmon@colorado.edu
# Github: bsalmon



# Question 1: Queue

import Queue
q = Queue.Queue()


# Question 2: Stack
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def checkSize(self):
		return len(self.items)

# Question 3: Binary tree

class Node:
	
	def __init__(self, key, left=None, right=None, parent = None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent
	def checkKey(self):
		return self.key
	def checkLeft(self):
		return self.left
	def checkRight(self):
		return self.right
	def checkParent(self):
		return self.parent
		
	def setKey(self,key):
		self.key=key
	def setLeft(self,left):
		self.left=left
	def setRight(self,right):
		self.right=right
	def setParent(self,parent):
		self.parent=parent
		
	def printNode(self):
		print(self.key)
		if self.left != None:
			self.left.printNode()
		if self.right != None:
			self.right.printNode()
	
	
	

class BinaryTree:
	__root=None
	__nl=[]
	def __init__(self, rootNode,nodeList):
		self.root=rootNode
		self.nl=nodeList
	
	def add(self, value, parentValue):
		for nodes in self.nl:
			if (nodes.checkKey()==parentValue):
				if(nodes.checkLeft()==None):
					newNode=Node(value, None, None, nodes)
					self.nl.append(newNode)
					nodes.setLeft(newNode)
					return
				elif(nodes.checkRight()==None):
					newNode=Node(value, None, None, nodes)
					self.nl.append(newNode)
					nodes.setRight(newNode)
					return
				else:
					print("Parent has two children, node not added")
					return
		print("Parent not found")
		return
		
	
	def delete(self, value):
		for nodes in self.nl:
			if (nodes.checkKey() == value):
				if((nodes.checkRight()!=None) or (nodes.checkLeft() != None)):
					print("Node not deleted, has children")
					return
				else:
					if(nodes.checkParent().checkLeft() == nodes):
						nodes.checkParent().setLeft(None)
					else:
						nodes.checkParent().setRight(None)
					self.nl.remove(nodes)
					return
		print("Node not found")
		return
		
	def printTree(self):
		self.root.printNode

# Question 4: Graph

class Graph:
	__vertices={}
	def __init__(self):
		self.vertices={}
	def addVertex(self, value):
		if value not in self.vertices:
			self.vertices[value]=[]
		else:
			print("Vertex already exists.")
			
	def addEdge(self,value1,value2):
		if ((value1 not in self.vertices) or (value2 not in self.vertices)):
			print("One or more vertices not found.")
		elif value1 in self.vertices[value2]:
			print("Edge exists.")
		else:
			self.vertices[value1].append(value2)
			self.vertices[value2].append(value1)
			
	def findVertex(self, value):
		if value in self.vertices:
			print(value,self.vertices[value])
		else:
			print("Value not found.")
			
# Question 5: Test Code

def testQueue():
	#create queue of 10 ints:
	for i in range(11):
		q.put(i)
	#print dequeued ints:
	while not q.empty():
		print q.get()

def testStack():
	#Create Stack:
	s = Stack()
	#Add 15 ints to stack:
	for i in range(15):
		s.push(i) 
	#Print removed items from stack:
	while(s.isEmpty() == False):
		print(s.pop())
	
		
def testBinaryTree():
	#create a root node with key of 1
	test=Node(1,None, None, None)
	#create a binary tree containing only the root node
	tree=BinaryTree(test,[test])
	tree.printTree()
	#add 10 nodes to the tree
	tree.add(2,1)	
	tree.add(8,1)
	tree.add(3,2)	
	tree.add(5,8)
	tree.add(4,2)
	tree.add(17,5)
	tree.add(12,5)
	tree.add(14,12)
	tree.add(19,12)
	tree.add(11,8)
	#print tree
	tree.printTree()
	#delete 2 nodes
	tree.delete(11)
	tree.delete(19)
	#print the tree
	tree.printTree()
	

def testGraph():
	#create a new graph
	testGraph=Graph()
	#add 12 vertices to the graph
	testGraph.addVertex(1)
	testGraph.addVertex(2)
	testGraph.addVertex(3)
	testGraph.addVertex(4)
	testGraph.addVertex(5)
	testGraph.addVertex(6)
	testGraph.addVertex(7)
	testGraph.addVertex(8)
	testGraph.addVertex(9)
	testGraph.addVertex(10)
	testGraph.addVertex(11)
	testGraph.addVertex(12)
	#add 20 edges
	testGraph.addEdge(2,3)
	testGraph.addEdge(2,4)
	testGraph.addEdge(2,5)
	testGraph.addEdge(7,3)
	testGraph.addEdge(6,3)
	testGraph.addEdge(12,10)
	testGraph.addEdge(12,9)
	testGraph.addEdge(11,12)
	testGraph.addEdge(11,3)
	testGraph.addEdge(11,10)
	testGraph.addEdge(10,5)
	testGraph.addEdge(10,3)
	testGraph.addEdge(5,7)
	testGraph.addEdge(1,3)
	testGraph.addEdge(9,5)
	testGraph.addEdge(9,8)
	testGraph.addEdge(1,6)
	testGraph.addEdge(6,7)
	testGraph.addEdge(1,12)
	testGraph.addEdge(6,2)
	#print the graph:
	print "Graph:", (testGraph.vertices)
	#add an edge that already exists:
	testGraph.addEdge(1,3)
	#find 5 vertices:
	testGraph.findVertex(1)
	testGraph.findVertex(2)
	testGraph.findVertex(11)
	testGraph.findVertex(12)
	testGraph.findVertex(7)
	#find a vertex that doesn't exist
	testGraph.findVertex(13)

print "Start queue test:"
testQueue()
print
print "Start stack test:"
testStack()
print
print "Start binary tree test:"
testBinaryTree()
print
print "Start graph test:"
testGraph()
print
print "End tests"



