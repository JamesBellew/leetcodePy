class Solution(object):
    def restoreString(self, s, indices):
        output = ['']* len(s)
        for i in range(len(indices)):
               output[indices[i]] = s[i]
        return ''.join(output) 
     
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

# Testing the function
solution = Solution()
result = solution.restoreString("codeleet",[4,5,6,7,0,2,1,3])
print(result)