'''
Great, the push method seems to be working fine! But we know that it's not done yet.
If we keep pushing items onto the stack, eventually we will run out of room in the array.
Currently, that will cause an Index out of range error. In order to avoid a stack overflow,
we need to check the capacity of the array before pushing an item to the stack.
And if the array is full, we need to increase the array size before pushing the new element.

'''
class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def handle_stack_capacity_full(self, data):
        self.arr_new = [0 for _ in range( 2* len(self.arr))]
        self.arr.extend(self.arr_new)
        self.push(data)

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    # TODO Add the push method
    def push(self, data):
        if self.next_index == len(self.arr):
            print("Index out of bound - Stack overflow")
            self.handle_stack_capacity_full(data)
        else:
            self.arr[self.next_index] = data
            self.next_index += 1
            self.num_elements += 1

    def pop(self):

        pass


foo = Stack()
print(foo.size()) # Should return 0
print(foo.is_empty()) # Should return True
foo.push("Test") # Let's push an item onto the stack and check again
print(foo.size()) # Should return 1
print(foo.is_empty()) # Should return False