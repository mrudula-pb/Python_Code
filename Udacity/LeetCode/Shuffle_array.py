
def shuffle(nums, n):
    #output = []
    first_part = []
    second_part = []
    half_nums = len(nums)//2

    for i in nums[0:half_nums]:
        first_part.append(i)
    #print(first_part)

    for j in nums[half_nums:len(nums)]:
        second_part.append(j)
    #print(second_part)

    return [b for a in zip(first_part, second_part) for b in a]

nums = [2,5,1,3,4,7]
n = 3
shuffle(nums, n)
