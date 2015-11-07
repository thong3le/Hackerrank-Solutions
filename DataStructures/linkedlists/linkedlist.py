class Node(object):
	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next = next_node

class SingleList(object):
	head = None
	tail = None

	def append(self, data):
		node = Node(data, None)
		if self.head is None:
			self.head = self.tail = node
		else:
			self.tail.next = node
		
		self.tail = node

	def show(self):
		current = self.head
		while current.next is not None:
			print current.data, "->",
			current = current.next
		print current.data, "-> None"

	def remove(self, data):
		current = self.head
		previous = None
		while current is not None:
			if current.data == data:
				if previous is not None:
					previous.next = current.next
				else:
					head = current.next
			previous = current
			current = current.next


a = SingleList()
a.append(12)
a.append(10)
a.append(2)
a.append(13)
a.append(19)
a.append(2)
a.show()

a.remove(2)
a.show()
