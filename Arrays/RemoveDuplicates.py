class Solution(object):
    def removeDuplicates(self, nums):
        l =1
        for r in range(1,len(nums)):
            if nums[r] != nums[l]:
                nums[l] = nums[r]
                l +=1
        return l
# Testing the function
solution = Solution()
result = solution.removeDuplicates([1,2,3,4,4,4,4,5])
print(result)
