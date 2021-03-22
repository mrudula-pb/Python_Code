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


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    node = self.head

    while node:
        if node.value == value:
            return node.value
        node = node.next


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """

    # TODO: Write function to insert here
    countIndex = 0
    node = self.head
    while node:
        countIndex += 1
        if countIndex == pos:
            node = Node(value)
            node.next = self.head
            self.head = node
            return
        elif pos > getSize(self) and node.next == None:
            node = Node(value)
            node.next = self.head
            self.head = node
            return
        node = node.next




def getIndex(self, value):
    """get Index of value"""
    countIndex = 0
    node = self.head
    while node:
        countIndex += 1
        if node.value == value:
            return countIndex
        node = node.next

def getSize(self):
    node = self.head
    count = 0
    while node:
        count += 1
        print(node.value)
        node = node.next
    return count





# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend
LinkedList.append = append
LinkedList.remove = remove
LinkedList.search = search
LinkedList.insert = insert
LinkedList.getIndex = getIndex
LinkedList.getSize = getSize

# Test prepend
linked_list = LinkedList()
# linked_list.prepend('X')
# linked_list.prepend(42)
linked_list.prepend('a')
linked_list.prepend(23)
linked_list.prepend(1)
# linked_list.append('the')
# linked_list.append('end')
# linked_list.remove(23)
# value = linked_list.getIndex(1)
# print(value)

# value = linked_list.getSize()
# print(value)
#linked_list.insert(5, 1)


# print ("Pass" if  (linked_list.to_list() == [1, 23, 'a', 42, 'X', 'the', 'end']) else "Fail")

# print ("Pass" if  (linked_list.to_list() == [1, 23, 'a', 42, 'X', 'the', 'end']) else "Fail")
# print("Pass" if (linked_list.to_list() == [5, 1, 23, 'a']) else "Fail")

# print("Pass" if (linked_list.search('a') == 'a') else "Fail")


# print("Pass" if (linked_list.to_list(5, 0) == [0, 1, 23, 'a']) else "Fail")

# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
