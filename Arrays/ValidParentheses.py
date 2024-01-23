class Solution(object):
    def isValid(self, s):
       stack = []

         # Lookup dictionary to match opening and closing brackets
       lookup = {
            "}": "{",
            "]": "[",
            ")": "("
        }

# Test the solution
solution = Solution()
result = solution.isValid("([])")
print(result)  # Output: True

