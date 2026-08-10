class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        answer = prices[:]
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                answer[idx] -= prices[i]
            stack.append(i)
        return answer
