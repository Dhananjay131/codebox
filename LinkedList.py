#!usr/bin/python3

class node:
	def __init__(self, val):
		self.val = val
		self.next = None
class queue:
	def __init__(self):
		self.head = None
	
	def add(self, ln):
		if not self.head:
			self.head = ln
			return

		curr = self.head
		while(curr.next):
			curr = curr.next
		curr.next = ln

	def delete(self):
		if not self.head:
			return
		
		temp = self.head
		self.head = self.head.next
		del(temp)
	
	def print_list(self):
		curr = self.head
		while(curr):
			print curr.val
			curr = curr.next

class stack:
	def __init__(self):
		self.head = None

	def add(self, ln):
		if not self.head:
			self.head=ln
			return

		curr = self.head
		while(curr.next):
			curr = curr.next
		curr.next = ln
	
	def delete(self):
		if not self.head:
			return

		temp = self.head
		while temp.next:
			curr = temp
			temp = temp.next
		
		curr.next = None
		del(temp)
	
	def print_list(self):
		curr = self.head
		while(curr):
			print curr.val
			curr = curr.next

	def find_min(self):
		curr = self.head
		minimum = curr.val
		while(curr):
			if minimum > curr.val:
				minimum = curr.val
				curr = curr.next

			else:
				curr = curr.next
				continue

		print minimum



n = node(10)
q = stack()
#q = queue()
q.add(n)
q.add(node(20))
q.add(node(30))
q.add(node(40))
q.add(node(40))
q.add(node(70))
q.add(node(7))
q.add(node(100))
q.print_list()
#q.delete()
#q.print_list()
print("The min value in the stack is: ")
q.find_min()

