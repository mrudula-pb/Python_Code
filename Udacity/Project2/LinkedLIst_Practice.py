class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList_Practice:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        new_node = Node(value)
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node


linked_list = LinkedList_Practice()

linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next