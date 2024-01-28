
class Solution(object):
    def truncateSentence(self, s, k):
        words = s.split()
        truncated = words[:k]  # Take the first k words
        return ' '.join(truncated)


        """
        :type s: str
        :type k: int
        :rtype: str
        """
        

# Testing the function
solution = Solution()
result = solution.truncateSentence("Hello how are you James",4)
print(result)