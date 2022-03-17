class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
    def empty(self):
        return self.front is None

    def push(self,value):
        if not self.front:
            self.front = Node(value,None)
            return
        node = self.front
        while node.next:
            node = node.next

        node.next = Node(value,None)
