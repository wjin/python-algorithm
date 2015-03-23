class List:
    class ListNode:
        def __init__(self, val = -1):
            self.val = val
            self.next = None 
            self.prev = None 

    def __init__(self):
        self.head = self.ListNode() # dummy node
        self.tail = self.head
        self.size = 0

    def insert(self, val):
        # insert reversely
        node = self.ListNode(val)

        if (self.head.next):
            self.head.next.prev = node
        else:
            self.tail = node

        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

        self.size += 1

    def len(self):
        print self.size

    def dump(self):
        node = self.head.next
        while node:
            print node.val
            node = node.next

        # dump by prev
        node = self.tail
        while node != self.head:
            print node.val
            node = node.prev

if __name__ == "__main__":
    list = List()

    list.insert(1)
    list.insert(2)
    list.insert(3)

    list.dump()

    list.len()
