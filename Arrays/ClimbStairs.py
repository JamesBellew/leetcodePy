class Solution(object):
    def climbStairs(self, n):
         steps=0

         if n ==1:
            return 1
         
         if n ==2:
            return 2
         else:
            # print('in here')
            one_step_back=2
            two_steps_back=1

           
            for i in range(2,n):
                # print(i)
                # print('1 step back', one_step_back)
                # print('2 steps back', two_steps_back)
                # print('steps',one_step_back + two_steps_back)
                steps = one_step_back + two_steps_back
                two_steps_back = one_step_back
                one_step_back = steps
                
            return steps

        
       
solution = Solution()
result = solution.climbStairs(4)
print(result)