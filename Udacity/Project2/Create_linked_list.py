def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    tail = None

    for value in input_list:
        if head == None:
            head = Node(value)
            tail = head  # when we only have 1 node. head and tail refer to same node
        else:
            tail.next = Node(value)  # attach the new node to the `next` of tail
            tail = tail.next  # update the tail

    return head


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



def nodes_of_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

head = Node(2)
head.next = Node(1)

head.next.next = Node(4)

head.next.next.next = Node(3)

head.next.next.next.next = Node(5)

head.next.next.next.next.next = None

nodes_of_list(head)


input_list = [1, 2, 3, 4, 5, 6]
k = create_linked_list(input_list)
