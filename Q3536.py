# Optimized code:
class Solution:
    def maxProduct(self, n: int) -> int:
        f_max = 0
        s_max = 0
        while n>0:
            digit = n % 10
            if digit >= f_max:
                s_max = f_max
                f_max = digit
            elif digit > s_max:
                s_max = digit
            n //= 10
            
        return f_max * s_max


# Sorting 
class Solution:
    def maxProduct(self, n: int) -> int:
        nums = [int(num) for num in str(n)]
        nums.sort()
        return nums[-1] * nums[-2]