class Solution(object):
    def maxProfit(self, nums):
        if not nums:
            return 0

        # Initialize minimum price and maximum profit
        min_price = nums[0]
        max_profit = 0

        for price in nums:
            # Update min_price if a lower price is found
            if price < min_price:
                min_price = price
            # Calculate the current profit and update max_profit if it's higher
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

# Testing the function
solution = Solution()
result = solution.maxProfit([7, 6, 4, 3, 1])
print(result)  # Expected output: 0 since no profit is possible
