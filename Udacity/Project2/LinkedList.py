# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         if self.head is None:
#             self.head = Node(value)
#             return
#
#         node = self.head
#         while node.next:
#             node = node.next
#
#         node.next = Node(value)
#         return
#
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(4)
#
# node = linked_list.head
#
# while node:
#     print(node.value)
#     node = node.next


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        return total

    def display(self):
        display_list = []

        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            display_list.append(current_node.data)
        print(display_list)

    def get(self, index):
        if index >= linked_list.length():
            print("Error: Get index out of range")
            return None
        current_index = 0
        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next
            if current_index == index: return current_node.data
            current_index += 1

linked_list = LinkedList()

linked_list.display()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.display()

print("element at 3rd node:" + str(linked_list.get(3)))