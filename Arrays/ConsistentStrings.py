class Solution(object):
    def countConsistentStrings(self, allowed, words):
        x = list(allowed)
        output = 0
        for i in range(len(words)):
            print(words[i])
            count =0
            for j in range(len(words[i])):
                print(words[i][j])
                if words[i][j] in x:
                    count +=1
                    if count == len(words[i]):
                        output +=1
        return output
# Testing the function booi
solution = Solution()
result = solution.countConsistentStrings("cad",["cc","acd","b","ba","bac","bad","ac","d"])
print(result)