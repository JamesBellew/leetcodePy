
class Solution(object):
    def findWordsContaining(self, words, x):
        output = []
        for i in range(len(words)):
            if x in words[i]:
                output.append(i)
        return output
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        


# Testing the function
solution = Solution()
result = solution.findWordsContaining(["abc","bcd","aaaa","cbc"],"a")
print(result)