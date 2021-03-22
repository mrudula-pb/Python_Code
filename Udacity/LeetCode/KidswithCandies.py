
def kidsWithCandies(candies, extraCandies):
    output = []
    for value in range(0, len(candies)):
        #print(candies[value])
        max_value = max(candies)

        total = candies[value] + extraCandies
        #print("TOTAL: ", total)
        if (total >= max_value):
            output.append("true")
        else:
            output.append("false")
    return output


# candies = [4,2,1,1,2]
# candies = [12,1,12]
candies = [2,3,5,1,3]
extraCandies = 3

values = kidsWithCandies(candies, extraCandies)
for value in values:
    print(value)
