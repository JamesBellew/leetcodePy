# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
class Solution(object):
    def twoSum( nums, target):
        output = []
        for index in range(len(nums)):
            for j in range(index + 1, len(nums)):
                if nums[index] + nums[j] == target:
                    output.append(index)
                    output.append(j)
                    return output
    result = twoSum([2,7,11,15],9)
    print(result)
                



# nums = [3,3]
# output = []
# target = 6


