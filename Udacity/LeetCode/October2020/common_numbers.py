# Given two arrays, write a function to compute their intersection.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
import itertools


def computeIntersection(nums1, nums2):
    # common_elements = []
    # sorted_nums1 = sorted(nums1)
    # print(sorted_nums1) # [1,1,2,2]
    #
    # length_nums1 = len(nums1)
    # length_nums2 = len(nums2)
    #
    # for element_nums1 in range(length_nums1):
    #     for element_nums2 in range(length_nums2):
    #         if nums1[element_nums1] == nums2[element_nums2]:
    #             common_elements.append(nums1[element_nums1])
    #         continue

    common_elements = []
    sorted_nums1 = sorted(nums1)
    print(sorted_nums1) # [1,1,2,2]

    for val1 in nums1:
        if val1 in nums2:
            common_elements.append(val1)

    return common_elements

nums1 = [1,2,2,1]
nums2 = [2,2]
intersection_values = computeIntersection(nums1, nums2)
print(intersection_values)
