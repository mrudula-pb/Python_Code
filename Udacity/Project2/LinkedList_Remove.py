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


def remove(self, value):
    node = self.head

    # If head node itself holds the key to be deleted

    if node is not None:
        if node.value == value:
            self.head = node.next
            temp = None
            return

    # Search for the key to be deleted, keep track of the
    # previous node as we need to change 'prev.next'
    while node is not None:
        if node.value == value:
            break
        prev = node
        node = node.next

    # if value was not present in linked list
    if node == None:
        return

    # Unlink the node from linked list
    prev.next = node.next

    node = None


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend
LinkedList.append = append
LinkedList.remove = remove

# Test prepend
linked_list = LinkedList()
# linked_list.prepend('X')
# linked_list.prepend(42)
linked_list.prepend('a')
linked_list.prepend(23)
linked_list.prepend(1)
# linked_list.append('the')
# linked_list.append('end')
linked_list.remove(23)

# print ("Pass" if  (linked_list.to_list() == [1, 23, 'a', 42, 'X', 'the', 'end']) else "Fail")

# print ("Pass" if  (linked_list.to_list() == [1, 23, 'a', 42, 'X', 'the', 'end']) else "Fail")
print("Pass" if (linked_list.to_list() == [1, 'a']) else "Fail")

# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
