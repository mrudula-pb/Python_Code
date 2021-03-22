# TODO: Write your recursive string reverser solution here

class reverse_string:
    def reverse_string(self, input):
        reverse_str = []
        str_length = len(input)
        while str_length > 0:
            reverse_str += input[str_length-1]
            str_length -= 1
        print(reverse_str)

    def reverse_str(self, input):
        reverse_str = input[::-1]
        print(reverse_str)

solution = reverse_string()
input = "Hello World"
solution.reverse_string(input)
solution.reverse_str(input)
#print("Reverse of String: " + str(value))



#         input_new = [None]* 11
#         for index in range(length-1):
#             temp = input[index]
#             input_new[index] = input[length-index-1]
#             input_new[length-index-1] = temp