class Linkedlist:

    def __init__(self, collection=None):
        self.head = None # setting self.head to a default value of None
        if collection: # if collection is true
            for item in reversed(collection): # this will allow for simple data entery eg: [1,2,3] => [1] -> [2] -> [3] -> None
                self.insert(item) # inserts the item into our linked list object

    def __iter__(self):
        
        def value_generator():
            current = self.head # sets current to the head node
            while current: # while current is truthy
                yield current.value # creates a value after each pass through
                current = current.next # sets current to next node
        
        return value_generator()

    def __str__(self):
        string = ""
        for value in self:
            string += f"[ {value} ] -> "
        return string + "None"


    def insert(self, value): # helper function
        self.head = Node(value, self.head) # instantiates the Node

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

