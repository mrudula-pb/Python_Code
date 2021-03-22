class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def to_list(self):
        my_list = []

        node = self.head
        while node:
            my_list.append(node.value)
            node = node.next
        return my_list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

node = linked_list.head

linked_list.to_list()


print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")