class Solution:
    def checkDivisibility(self, n: int) -> bool:
        product = 1
        sumValue = 0
        if n < 10:
            return True if n % (n + n) == 0 else False 
        for digit in str(n):
            product *= int(digit)
            sumValue += int(digit)
        requiredSum = product + sumValue
        return True if n % requiredSum == 0 else False