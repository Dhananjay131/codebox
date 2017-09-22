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
		curr = temp
                while temp.next:
                        curr = temp
                        temp = temp.next

                curr.next = None
		return temp


        def print_list(self):
                curr = self.head
                while(curr):
                        print curr.val
                        curr = curr.next
			

s1 = stack()
s2 = stack()
s1.add(node(1))
s1.add(node(2))
s1.add(node(3))
s1.add(node(4))
s1.add(node(5))
s1.add(node(6))
s1.add(node(7))
s1.add(node(8))

print("Printing Stack 2")
s1.print_list()

s2.add(s1.delete())
s2.add(s1.delete())
s2.add(s1.delete())
s2.add(s1.delete())
s2.add(s1.delete())
s2.add(s1.delete())
s2.add(s1.delete())
s2.add(s1.delete())

print("Placing Stack1 values in  Stack2")
s2.print_list()

q = queue()
q.add(s2.delete())
q.add(s2.delete())
q.add(s2.delete())
q.add(s2.delete())
q.add(s2.delete())
q.add(s2.delete())
q.add(s2.delete())
q.add(s2.delete())

print("Printing queue")
q.print_list()
