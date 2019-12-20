from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == self.capacity:
            if self.current is None:
                self.current = self.storage.tail
            self.current.value = item
            if self.current.prev:
                self.current = self.current.prev
            else: self.current = self.storage.tail
        else: self.storage.add_to_head(item)

    #WORKING ON IT!

    

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
