# brute force, Time complexity - O(n2)
# def maxProfit(prices):
#     profit = 0
#     for i in range(0,len(prices)-1):
#         max_profit = 0
#         for j in range(i+1, len(prices)):
#             this_profit = prices[j] - prices[i]
#             if this_profit > max_profit:
#                 max_profit = this_profit

#         if max_profit > profit:
#             profit = max_profit

#     return profit
       
# OPtimized Time Complexity - O(n)
def maxProfit(prices):

    cheapest = float('inf')
    profit = 0

    for i in range(0,len(prices)):

        if prices[i] < cheapest:
            cheapest = prices[i]
            print(f"Cheapest becomes : {cheapest}")

        this_profit = prices[i] - cheapest
        print(f"This profit becomes : {this_profit}")

        if(this_profit > profit):
            profit = this_profit    


    return profit

prices = [10,1,5,6,7,1]

result = maxProfit(prices)
print(result)