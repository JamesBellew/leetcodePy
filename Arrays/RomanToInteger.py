class Solution(object):
   
    def romanToInt(self, s):
        Romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        input_str = list(s)
        total = 0
        pointer = 0
        
        for i in range(len(input_str)):
            current_char = input_str[i]
            
            if input_str[i] == "I" and (i + 1 < len(input_str)) and (input_str[i + 1] == "V" or input_str[i + 1] == "X"):
                pointer += Romans[input_str[i+1]]- Romans[input_str[i]]
            else:
                total += Romans[current_char]
                


        # for items in range(len(input_str)):
            # pointer += items  
            # if input_str[items] in Romans:
            #     if input_str[items] == "I" and (items + 1 < len(input_str)) and (input_str[items + 1] == "X"):                                                             
            #         total += Romans[input_str[items + 1]] - Romans[input_str[items]]
            #     else:
            #         total += Romans[input_str[items]]
                # the input types in by the user is a valid roman numeral
                # if input_str[items] == "I" and (items + 1 < len(input_str)) and (input_str[items + 1] == "V" or input_str[items + 1] == "X"):
                #     # the curent string could potentially  be a special character that requires a equation
                #     total += Romans[input_str[items + 1]] - Romans[input_str[items]]
                #     print(total , "hii")
                # else:
                #     total += Romans[input_str[items]]
                
            # else:
            #     print('Invalid Roman numeral entered')
            #     return None
            print(total)
            print(pointer , "pointer")
        return total
        
# Testing the function
solution = Solution()
result = solution.romanToInt("MCMXCIV")
print(result)
