# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        flag = False
        input_str = str(x)  # Convert integer to a string
        reversed_str = input_str[::-1]  # Reverse the string

        if reversed_str == input_str:
            flag = True

        return flag

# Testing the function
solution = Solution()
result = solution.isPalindrome(12122)
print(result)

