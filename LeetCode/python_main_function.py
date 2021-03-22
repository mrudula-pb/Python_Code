print("Hello")

print("__name__ value: ", __name__)


def main():
    print("python main function")


if __name__ == '__main__':
    main()


    class Solution(object):
        def maxSubArray(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            sum = 0
            result = 6
            first4 = nums[:4]
            for n in first4:
                sum = sum + n
            print
            sum
            if sum is result:
                return sum

            page = 'current page'
            per_page = 10
            total = 10
            total_pages = 100

            PARAMS = {'page':, 'per_page':, 'total':, 'total_pages':, 'data': []}


            