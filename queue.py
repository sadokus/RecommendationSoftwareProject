from node import DoublyLinkedList, Node
class Queue:
    def __init__(self, max_size = None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
    
    def dequeue(self, value):
        if self.has_space():
            item_to_add = Node(value)

            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("no more room")