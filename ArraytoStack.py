#!usr/bin/python3
#Implementing array into three stacks

class node:
        def __init__(self, val):
                self.val = val
                self.next = None

class stack:
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

	def print_list(self):
		curr = self.head
		while(curr):
			print curr.val
			curr = curr.next


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
totalLen = len(arr)
divLen = totalLen/3
stackcount=0
i=0
while stackcount<divLen :
	s=stack()
	while (i<totalLen):
		s.add(node(arr[i]))
	 	i+=1
		
		if (i)%divLen==0:
			stackcount+=1
			print("Stack Number:",stackcount)
			s.print_list()
			break
		
		

exit(0)


