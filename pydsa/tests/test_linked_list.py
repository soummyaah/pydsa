from pydsa import linked_list

def test_linked_list():
	def __init__(self):
		self.test_list = linked_list()

	def test_is_empty(self):
		self.assertTrue(self.test_list.is_empty() == True)
		
	def test_insert_at_start(self):
		self.test_list.insert_at_start(5)
		self.assertTrue(self.test_list.head.get_value() == 5)
		self.assertTrue(self.test_list.head.get_next() == None)
		self.assertTrue(self.test_list.is_empty() == False)

	def test_insert_at_end(self, value):
		self.test_list.insert_at_end(10)
		curr = self.test_list.head
		while curr.get_next():
			curr = curr.get_next()
		self.assertTrue(curr.get_value() == 10)
		self.assertTrue(curr.get_next() == None)		

	# def test_find(self, value):
		
	# def delete(self, value):

	# def length(self):

	# def toString(self):
