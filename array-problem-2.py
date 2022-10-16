# Best Time to Buy and Sell Stock II

def maxProfit(prices):
    total = 0
    for i in range(len(prices)-1):
        diff = prices[i+1] - prices[i]
        if diff > 0:
            total += diff
    return total

print(maxProfit([7,1,5,3,6,4]))
