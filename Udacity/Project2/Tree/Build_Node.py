# Task 01: build a node
# on a piece of paper, draw a tree.
# Define a node, what are the three things you'd expect in a node?
# Define class called Node, and define a constructor that takes no arguments, and sets the three instance variables to None.
# Note: coding from a blank cell (or blank piece of paper) is good practice for interviews!

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

# Task 02: add a constructor that takes the value as a parameter
# Copy what you just made, and modify the constructor so that it takes
# in an optional value,
# which it assigns as the node's value. Otherwise, it sets the node's value to None.

# node = Node('apple')
# print(f""" value: {node.value} left: {node.left} right: {node.right} """)


# Task 03: add functions to set and get the value of the node¶
# Add functions get_value and set_value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

# Task 04: add functions that assign a left child, or right child
# Define a function set_left_child and a function set_right_child. Each function
# takes in a node that it assigns as the left or right child, respectively. Note that we can assume
# that this will replace any existing node if it's already assigned as a left or right child.
# Also, define get_left_child and get_right_child functions.

    def set_left_child(self, node1):
        self.left = node1

    def set_right_child(self, node2):
        self.right = node2

    def get_left_child(self):
        return node0.left.value

    def get_right_child(self):
        return node0.right.value

# Task 05: check if left or right child exists
# Define functions has_left_child, has_right_child,
# so that they return true if the node has left child, or right child respectively.

    def has_left_child(self):
        return node0.left != None

    def has_right_child(self):
        return node0.right != None

# Task 06: Create a binary tree¶
# Create a class called Tree that has a "root" instance variable of type Node.
#
# Also define a get_root method that returns the root node.
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def get_root(self):
#         return self.root

# Task 07: setting root node in constructor
# Let's modify the Tree constructor so that it takes an input that initializes the root node.
# Choose between one of two options: 1) the constructor takes a Node object
# 2) the constructor takes a value, then creates a new Node object using that value.
#
# Which do you think is better?

class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

tree = Tree("APPLE")
print(tree.get_root().value)

node0 = Node()
print(f""" value: {node0.value} left: {node0.left} right: {node0.right} """)

node0.set_value("APPLE")
print(f""" value: {node0.get_value()} """)

print(f""" Has left child: {node0.has_left_child()}""")

print(f""" Has right child: {node0.has_right_child()}""")

node1 = Node("BANANA")
node0.set_left_child(node1)
print(f""" left: {node0.left.value}""")

node2 = Node("CHERRY")
node0.set_right_child(node2)
print(f"""  right: {node0.right.value}""")

print(f""" Has left child: {node0.has_left_child()}""")

print(f""" Has right child: {node0.has_right_child()}""")



