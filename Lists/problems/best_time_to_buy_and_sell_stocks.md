# Problem
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
* 1 <= prices.length <= 105
* 0 <= prices[i] <= 104

# Brainstorm
Input: List of Intergers, representing price of stock
Output: An interger, which represents the maximum profit

* Notice that the best case is when the price constantly increases from when you buy it (i.e biggest difference)
* We should keep track of the maximum difference or profit as we iterate through
* We should keep track of the smallest number

# Algorithm
* Intialize a variable for the maximum profit (0) and the previous smallest number seen so far (104 as maximum)
* Iterate through the list
    * Set the smallest number seen so far as the smaller of the two: the last previous smalles tnumber 
    * Set the differences as the value of the current index by the previous smallest number seen so far
    * Set the maximum profit as the bigger of the two: current maximum profit or difference found previously
* Return the maximum profit  

# Code
```
def maxProfit(self, prices: List[int]) -> int:
    maxDifference = 0   
    prevSmallest = float('inf')     # could also be 104
    
    for i in range(len(prices)):   
        prevSmallest = min(prevSmallest, prices[i])   
        difference = prices[i] - prevSmallest   
        
        maxDifference = max(maxDifference, difference)
            
    return maxDifference
```

# Test Cases
* List of Length 1
* List containing 0
* List with length of 105
* Case where it's ascending only
* Case where it's descending only

# Analysis 
Time Complexity: O(n) -> need to iterate through entire list regardless
Space Complexity: O(1) -> only need to store integers 