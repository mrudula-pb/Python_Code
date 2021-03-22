class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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
    node.value = self.head
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


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend
LinkedList.append = append


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
linked_list.prepend(23)
linked_list.prepend('a')
linked_list.prepend(42)
linked_list.prepend("X")
linked_list.append('the')
linked_list.append('end')

# print ("Pass" if  (linked_list.to_list() == [1, 23, 'a', 42, 'X', 'the', 'end']) else "Fail")

assert linked_list.to_list() == [1, 23, 'a', 42, 'X', 'the', 'end'], f"list contents: {linked_list.to_list()}"
