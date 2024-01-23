# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 
class Solution(object):
    def containsDuplicate(self, nums):
        flag = False
        for l in range(len(nums)-1):
            for r in range(l+1 ,len(nums)):
                if nums[l] == nums[r]:
                    return True 
        return False


# Testing the function
solution = Solution()
result = solution.containsDuplicate([1,2,3,3,4,5,6,7])
print(result)
