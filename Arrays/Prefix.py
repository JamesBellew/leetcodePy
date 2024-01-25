
class Solution(object):
    def longestCommonPrefix(self, strs):
         firstWord=list(strs[0])
         p=0


         for i in range(1,len(strs)):
              print(strs[i])
              for r in range(len(strs[i])):
                
                   print('other',strs[i][r])
                   print('base',firstWord[p])
                #    if strs[i][r] == firstWord[p]:
                #         print('good')
                #    else:
                #         print('no')
                        
         return("")
                   
        
      
# Testing the function
solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","floight"])
print(result)
