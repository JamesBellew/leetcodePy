class Solution(object):
    def mostWordsFound(self, sentences):
        return max(len(sentence.split()) for sentence in sentences)
        # x=" "
        # output=[]
        # for words in sentences:
        #      print(words)
        #      count=1
        #      for i in range(len(words)):
        #                 if x == words[i].lower():
        #                       count+=1
        #      print(count)
        #      output.append(count)
        # return(max(output))
                   

           
        """
        :type sentences: List[str]
        :rtype: int
        """

# Testing the function
solution = Solution()
result = solution.mostWordsFound(["hi how are you","very good thanks","what is your plan today","nothing much just going to chill"])
print(result)