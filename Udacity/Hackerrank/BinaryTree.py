class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    ## Task 03: add functions to set and get the value of the node
    def set_value(self,value):
        self.value = value
        print(f'''value: {self.value}''')

    def get_value(self):
        print(f"""value: {node0.value}""")


    # Task 04: add functions that assign a left child, or right child
    # Define a function set_left_child and a function set_right_child. Each function takes in
    # a node that it assigns as the left or right child, respectively. Note that we can assume
    # that this will replace any existing node if it's already assigned as a left or right child.
    #
    # Also, define get_left_child and get_right_child functions.
    def set_left_child(self, node1):
        self.left = node1

    def set_right_child(self, node2):
        self.right = node2

    def get_left_child(self):
        return node0.left.value

    def get_right_child(self):
        return node0.right.value

    # Define functions `has_left_child`, `has_right_child`,
    # so that they return true if the node has left child, or right child respectively.

    def has_left_child(self):
        return self.left != None

        # if self.left != None:
        #   return True
        # return False

    def has_right_child(self):
        return self.right != None

        # if self.right != None:
        #    return True
        # return False

## Task 01: build a node
bt0 = Node()
print(f"""value: {bt0.value} 
left: {bt0.left} 
right: {bt0.right}""")

## Task 02: add a constructor that takes the value as a parameter
node0 = Node("apple")
print(f"""value: {node0.value} 
left: {node0.left} 
right: {node0.right}""")

# bt.set_value("orange")
# bt.get_value()


node1 = Node("banana")
node2 = Node("orange")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"""
node 0: {node0.value}
node 0 left child: {node0.left.value}
node 0 right child: {node0.right.value}
""")

print("left child: ", node0.get_left_child())

print("right child: ", node0.get_right_child())

print(f"has left child? {node0.has_left_child()}")
print(f"has right child? {node0.has_right_child()}")
