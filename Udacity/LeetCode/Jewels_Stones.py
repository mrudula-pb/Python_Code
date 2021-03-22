def numJewelsInStones(J, S):
    jewelCount = 0
    for char in S:
        if char in J:
            jewelCount += 1
    return jewelCount

J = "aA"
S = "aAAbbbb"
value = numJewelsInStones(J, S)
print(value)