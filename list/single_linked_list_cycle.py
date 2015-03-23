class List:
    class ListNode:
        def __init__(self, val = -1):
            self.val = val
            self.next = None 

    def __init__(self):
        self.head = self.ListNode() # dummy node
        self.head.next = self.head
        self.size = 0

    def insert(self, val):
        # insert reversely
        node = self.ListNode(val)
        node.next = self.head.next
        self.head.next = node

        self.size += 1

    def len(self):
        print self.size

    def dump(self):
        node = self.head.next
        while node != self.head:
            print node.val
            node = node.next

if __name__ == "__main__":
    list = List()

    list.insert(1)
    list.insert(2)
    list.insert(3)

    list.dump()

    list.len()
