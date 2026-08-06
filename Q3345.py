# Recursion:
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        product = 1
        for digit in str(n):
            product *= int(digit)
        if (product == 0) or (product % t == 0):
            return n
        else:
            return self.smallestNumber(n + 1, t)
        

# Optimized - O(1):
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            product = 1
            while temp > 0:
                product *= temp % 10
                temp //= 10
                if product == 0:
                    break
            if product % t == 0:
                return n
            n += 1