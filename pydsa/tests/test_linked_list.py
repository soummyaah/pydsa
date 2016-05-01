from pydsa import LinkedList

class test_linked_list():

    test_list = LinkedList()

    def steps(self):
        for name in sorted(dir(self)):
            if name.startswith("step"):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self.steps():
            try:
                step()
            except Exception as e:
                self.fail("{} failed ({}: {})".format(step, type(e), e))

    # Test is_empty
    def step1(self):
        assert self.test_list.is_empty() == True

    # Test insert_at_start
    def step2(self):
        self.test_list.insert_at_start(5)
        # print(self.test_list.toString())
        assert self.test_list.head.get_value() == 5
        assert self.test_list.head.get_next() == None
        assert self.test_list.is_empty() == False

    # Test insert_at_end
    def step3(self):
        self.test_list.insert_at_end(6)
        curr = self.test_list.head
        while curr.get_next():
            curr = curr.get_next()
        assert curr.get_value() == 6
        assert curr.get_next() == None

    # Test find
    def step4(self):
        self.test_list.insert_at_start(4)
        assert self.test_list.head == self.test_list.find(4)

    # Test delete
    def step5(self):
        assert self.test_list.find(4) == self.test_list.head
        self.test_list.delete(4)
        self.assertRaises(ValueError, self.test_list.find, 4)

    # Test length function
    def step6(self):
        assert len(self.test_list) == 2
        self.test_list.insert_at_start(3)
        assert len(self.test_list) == 3
        self.test_list.delete(6)
        assert len(self.test_list) == 2
        # def toString(self):
