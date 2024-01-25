class Solution(object):
    def finalValueAfterOperations(self, operations):
        output = 0
        ops={
            "--X":-1,
            "X--":-1,
            "++X":1,
            "X++":1
        }
        for cmds in operations:
            output += ops[cmds]

        return output




# Testing the function
solution = Solution()
result = solution.finalValueAfterOperations(["++X","++X","X++"])
print(result)