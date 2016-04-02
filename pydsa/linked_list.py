class linked_list_node(object):
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node

	def get_next(self):
		return self.next_node

	def get_value(self):
		return self.value

	def set_next(self, next_node):
		self.next_node = next_node

class linked_list(object):
	def __init__(self, head=None):
		self.head = head

	def is_empty(self):
		return self.head == None

	def insert_at_start(self, value):
		temp_node = linked_list_node(value)
		temp_node.set_next(self.head)
		self.head = temp_node
		return

	def insert_at_end(self, value):
		curr_node = self.head
		while(curr_node.get_next() is not None):
			curr_node = curr_node.get_next()
		temp_node = linked_list_node(value)
		temp_node.set_next(None)
		curr_node.set_next(temp_node)

	def find(self, value):
		found = False
		curr_node = self.head
		while curr_node and found is False:
			if curr_node.get_value() == value:
				found = True
			else:
				curr_node = curr_node.get_next()
		if curr_node is None:
			raise ValueError("Element not found")
		return curr_node
		
	def delete(self, value):
		found = False
		curr_node = self.head
		prev_node = None
		while(curr_node is not None and found is False):
			if curr_node.get_value() == value:
				found = True
			else:
				prev_node = curr_node
				curr_node = curr_node.get_next()
		if curr_node is None:
			raise ValueError("Element not found")
		if prev_node is None:
			self.head = curr_node.get_next()
		else:
			prev_node.set_next(curr_node.get_next())

	def length(self):
		curr_node = self.head
		length = 0
		while curr_node:
			length += 1
			curr_node = curr_node.get_next()
		return length

	def toString(self):
		value_string = ""
		curr_node = self.head
		while curr_node:
			if curr_node == self.head:
				value_string += str(curr_node.get_value())
			else:
				value_string += " " + str(curr_node.get_value())
			curr_node = curr_node.get_next()
		return value_string
