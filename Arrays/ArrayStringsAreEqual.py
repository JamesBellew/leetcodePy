class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        if ''.join(word1)==''.join(word2):
            return True
        else:
            return False

        # wrd1 = ""
        # wrd2 = ""

        # for i in range(len(word1)):
        #     wrd1 += word1[i]
        #     print(wrd1)
        
        # for j in range(len(word2)):
        #     wrd2 += word2[j]
        #     print(wrd2)

        # if wrd1 == wrd2:
        #     return True
        # else:
        #     return False

        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        

# Testing the function
solution = Solution()
result = solution.arrayStringsAreEqual(["abc", "d", "defg"],["abcddefg"])
print(result)