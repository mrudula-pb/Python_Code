
# this code makes the tree that we'll traverse

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

tree = Tree("APPLE")
print(tree.get_root().value)

tree.get_root().set_left_child(Node("BANANA"))
print(tree.get_root().get_left_child().value)

tree.get_root().get_left_child().set_left_child(Node("DATES"))
print(tree.get_root().get_left_child().get_left_child().value)

tree.get_root().set_right_child(Node('CHERRY'))
print(tree.get_root().get_right_child().value)
