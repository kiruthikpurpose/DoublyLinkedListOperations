class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_middle(self, data, position):
        new_node = DoublyNode(data)
        if position == 0:
            self.insert_at_start(data)
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of bounds")
            temp = temp.next
        new_node.next = temp.next
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    def delete_at_start(self):
        if not self.head:
            print("List is empty")
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_at_middle(self, position):
        if position == 0:
            self.delete_at_start()
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None or temp.next is None:
                print("Position out of bounds")
            temp = temp.next
        temp.next = temp.next.next
        if temp.next:
            temp.next.prev = temp

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=' <-> ')
            last_node = temp
            temp = temp.next
        print('None')

        while last_node != self.head:
            print(last_node.data, end=' <-> ')
            last_node = last_node.prev
        print(last_node.data)

dll = DoublyLinkedList()
dll.insert_at_start(1)
dll.insert_at_start(2)
dll.insert_at_start(3)
dll.insert_at_start(4)
dll.insert_at_start(5)

# dll.insert_at_start(10)
# dll.insert_at_end(2)
# dll.insert_at_middle(3, 1)
# dll.delete_at_start()
# dll.delete_at_end()
# dll.delete_at_middle(0)

print(dll.traverse())
