class Solution(object):
    def generate(self, num):
        output = []
        l=1
        output.append([1])
        for i in range(1,num):
            o = []
            for j in range(i+1):
                if j ==0 or j ==i:
                    o.append(1)
                else:
                    o.append(output[i-1][j-1] + output[i-1][j])
                # o.append(1)
            output.append(o)




        return output
        
# Testing the function
solution = Solution()
result = solution.generate(5)
print(result)
