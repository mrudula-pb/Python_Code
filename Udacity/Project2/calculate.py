
def calculate_child_nodes(p):
    value_1 = (2 * p) + 1
    value_2 = (2 * p) + 2
    print(value_1, value_2)

def calculate_parent_node(p):
    value_parent = (p-1)//2
    print(value_parent)

p = 3
calculate_child_nodes(p)
calculate_parent_node(p)
#print(value)
