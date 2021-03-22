
#Part 3: Iterate through the given dictionary to print out the name (key)
# and whichparty they belong to (value)#For example: print out 'Name: Steve'
# on one line and 'Party: Bride' on the next (for each name in the dictionary)
# my_dict = {'Steve': 'Bride', 'Tony': 'Groom', 'Peter': 'Bride', 'Josh': 'Bride',
# 'Clara': 'Groom', 'Martha': 'Groom','Charlotte': 'Bride'}

class Solution:
    def print_dict(self, dict):
        for key, value in dict.items():
            print("Name: " + str(key))
            print("Party: " + str(value))

solution = Solution()
my_dict = {'Steve': 'Bride', 'Tony': 'Groom', 'Peter': 'Bride', 'Josh': 'Bride', 'Clara': 'Groom', 'Martha': 'Groom','Charlotte': 'Bride'}
solution.print_dict(my_dict)