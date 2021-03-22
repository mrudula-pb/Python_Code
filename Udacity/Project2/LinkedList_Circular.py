class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList_Circular:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return


def iscircular(self, linked_list=None):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    # TODO: Write function to check if linked list is circular
    runner_1 = linked_list.head
    runner_2 = linked_list.head

    while runner_2 and runner_2.next:
        runner_1 = runner_1.next
        runner_2 = runner_2.next.next
        if runner_1 == runner_2:
            return True

    return False


list_with_loop = LinkedList_Circular([2, -1, 3, 0, 5])

LinkedList_Circular.iscircular = iscircular

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start

small_loop = LinkedList_Circular([0])

print ("Pass" if iscircular(list_with_loop) else "Fail")                  # Pass
print ("Pass" if iscircular(LinkedList_Circular([-4, 7, 2, 5, -1])) else "Fail")   # Fail
print ("Pass" if iscircular(LinkedList_Circular([1])) else "Fail")                 # Fail
print ("Pass" if iscircular(small_loop) else "Fail")                      # Pass
print ("Pass" if iscircular(LinkedList_Circular([])) else "Fail")                  # Fail