
# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

class Solution(object):
    def plusOne(self, digits):
        size = len(digits)
        
        # Check if the last digit is 9
        if digits[-1] == 9:
            # If there's more than one digit in the list
            if size > 1:
                count = 0  # Count consecutive 9s from the end of the list
                for i in range(len(digits) - 1, -1, -1):
                    if digits[i] == 9:
                        count += 1
                    else:
                        break  # Stop counting when a non-9 digit is found
                    
                # If all digits are 9, update them accordingly
                if count == size:
                    return [1] + [0] * size
                else:
                    digits[-(count + 1)] += 1  # Increment the digit before the 9s
                    for i in range(count):
                        digits[-(i + 1)] = 0  # Reset the 9s to 0
                
            else:
                return [1, 0]  # Single-digit case, return [1, 0]
        else:
            digits[-1] += 1  # If the last digit is not 9, simply increment it
        
        return digits

      
# Testing the function
solution = Solution()
result = solution.plusOne([9,9])
print(result)
