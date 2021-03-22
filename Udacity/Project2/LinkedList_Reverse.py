class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # print method for the linked list
    def printLL(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

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


def reverse(self, list):

    # TODO: Write your function to reverse linked lists here
    previous = None
    current = list.head
    following = current.next

    while current:
        current.next = previous
        previous = current
        current = following
        if following:
            following = following.next

    list.head = previous

# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend
LinkedList.append = append
LinkedList.reverse = reverse

# Test prepend
linked_list = LinkedList()
linked_list.prepend('X')
linked_list.prepend(42)
linked_list.prepend('a')
linked_list.prepend(23)
linked_list.prepend(1)
linked_list.append('the')
linked_list.append('end')

linked_list.reverse(linked_list)

linked_list.printLL()