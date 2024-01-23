
class Solution(object):
    def longestCommonPrefix(self, strs):
         firstWord=list(strs[0])
         prefix = strs[0]
         l=0
         for i in range(1, len(strs)):
             print(firstWord[l])
             print(strs[i])
             if(firstWord[l]==strs[i][l]):
                 print('good')
                 l+=1

         s=0
         t=0
         if len(strs)==1:
            return ""   
            

        
        # secondWord=list(strs[1])
        # thirdWord=list(strs[2])
        # pointers
      
       
       
         

        # for lets in firstWord:
            # if(lets==secondWord[s] and lets==thirdWord[t]):
            #     prefix.append(lets)
            #     s+=1
            #     t+=1
            # else:
            #     return ''.join(prefix)
            # print(lets)
         return("")
        
      
# Testing the function
solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","floight"])
print(result)
