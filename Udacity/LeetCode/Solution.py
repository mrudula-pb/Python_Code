# Example 1:
# Input:
# ["9001 discuss.leetcode.com"]
# Output:
# ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
# Explanation:
# We only have one website domain: "discuss.leetcode.com". As discussed
# above, the subdomain "leetcode.com" and "com" will also be visited.
# So they will all be visited 9001 times.
from collections import defaultdict


class Solution(object):
    def subdomainVisits(self, cpdomains):
        tally = defaultdict(int)
        for element in cpdomains:
            elements = element.split()
            print('SPLIT: ', elements)

            count, domain = int(elements[0]), elements[1].split('.')
            print("COUNT: ", count)
            print('DOMAIN: ', domain)

            print('length of domain: ', len(domain))

            for i in range(len(domain)): # 0,1,2
                print('.'.join(domain[i:]))
                tally['.'.join(domain[i:])] += count
            print(tally)

        return ['%d ' % c + d for d, c in tally.items()]

sol = Solution()
value = []
value = sol.subdomainVisits(["9001 discuss.leetcode.com"])
print(value)