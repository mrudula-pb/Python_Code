# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


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


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """

    # TODO: Write your function to reverse linked lists here
    previous = None
    current = linked_list.head
    following = current.next

    while current:
        current.next = previous
        previous = current
        current = following
        if following:
            following = following.next

    linked_list.head = previous


# This is the way to add a function to a class after it has been defined
# LinkedList.prepend = prepend
# LinkedList.append = append
LinkedList.reverse = reverse

# Test prepend
linked_list = LinkedList()
# linked_list.prepend('X')
# linked_list.prepend(42)
# linked_list.prepend('a')
# linked_list.prepend(23)
# linked_list.prepend(1)
# linked_list.append('the')
# linked_list.append('end')
# linked_list.remove(23)
# value = linked_list.getIndex(1)
# print(value)


# linked_list.reverse(linked_list)

# llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    linked_list.append(value)

flipped = reverse(linked_list)

is_correct = linked_list.to_list() == list(['end', 'the', 'X', 42, 'a', 23, 1])
print("Pass" if is_correct else "Fail")

# linked_list.printLL()
