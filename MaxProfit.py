class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window 
        left, right = 0, 1 
        max_price = 0 
        
        while right < len(prices): # 
            
            if prices[left] < prices[right]: 
                profit = prices[right] - prices[left]
                max_price = max(max_price, profit)
            else: 
                left += right 
                
            right += 1 
             
                
        return max_price 
            