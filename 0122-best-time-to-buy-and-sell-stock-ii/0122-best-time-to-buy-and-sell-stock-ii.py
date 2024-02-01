class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        direction = [0] * len(prices)
        
        direction[0] = -1
        for i in range(1, len(prices)):
            direction[i] = 1 if prices[i] > prices[i - 1] else -1
        
        answer = 0
        
        for i in range(0, len(prices) - 1):
            if direction[i] == -1 and direction[i + 1] == 1:
                lower = prices[i]
            elif direction[i] == 1 and direction[i + 1] == -1:
                higher = prices[i]
                answer = answer + higher - lower
            else:
                continue
        if direction[-1] == 1:
            answer = answer + prices[-1] - lower
        return answer