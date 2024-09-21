#!/usr/bin/python3
"""
0. Change comes from within
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a large value (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total of 0

    # Iterate through each coin
    for coin in coins:
        # Update dp array for each amount from coin to total
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, return -1 (total cannot be met)
    return dp[total] if dp[total] != float('inf') else -1
