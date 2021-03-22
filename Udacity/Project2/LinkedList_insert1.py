class Node:
    def __init__(self, value, next = None):
        self.next = next
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Define a function outside of the class
# Takes O(1)
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head is None:
        self.head = Node(value)
        return
    node = Node(value)
    node.next = self.head
    self.head = node
    return


def append(self, value):
    if self.head is None:
        self.head = Node(value)
        return

    node = self.head
    while node.next:
        node = node.next

    node.next = Node(value)
    return


# def insert(self, head, value, pos):
#     """ Insert value at pos position in the list. If pos is larger than the
#     length of the list, append to the end of the list. """
#
#     # TODO: Write function to insert here
def insertNodeAtPosition(self, value, pos):
    if pos == 0:
        self.head = Node(value, self.head)
        return

    node = self.head
    while pos > 1:
        node = node.next
        pos -= 1
    node.next = Node(value, node.next)


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend
LinkedList.append = append

LinkedList.insertNodeAtPosition = insertNodeAtPosition

# Test prepend
linked_list = LinkedList()

linked_list.prepend('a')
linked_list.prepend(23)
linked_list.prepend(1)

linked_list.insertNodeAtPosition(5, 1)
linked_list.insertNodeAtPosition(10, 3)


print("Pass" if (linked_list.to_list() == [1, 5, 23, 10, 'a']) else "Fail")