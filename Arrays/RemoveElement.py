class Solution(object):
    def removeElement(self, nums, val):
        k =0
        for num in nums:      
            if num != val:
                nums[k] = num
                k +=1
        return k
    
# Testing the function
solution = Solution()
result = solution.removeElement([3,2,2,3],3)
print(result)
