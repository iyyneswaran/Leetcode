# without inbuild methods
class Solution:
    def gcd(self, mxi, num):
        while num:
            mxi, num = num, mxi % num
        return mxi

    def gcdSum(self, nums: list[int]) -> int:
        mxi = 0
        prefixGcd_val = []
        for num in nums:
            mxi = max(mxi, num)
            prefixGcd = self.gcd(mxi, num)
            prefixGcd_val.append(prefixGcd)
        sum_value = 0
        right = 0
        left = len(prefixGcd_val) - 1
        sorted_prefix_Gcd_val = sorted(prefixGcd_val)
        while right < left:
            sum_value += self.gcd(sorted_prefix_Gcd_val[right], sorted_prefix_Gcd_val[left])
            right += 1
            left -= 1
        return sum_value
    
# or 
# with inbuild methods
from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mxi = 0
        prefixGcd = []
        mxi = 0
        for num in nums:
            mxi = max(mxi, num)
            prefixGcd.append(gcd(mxi, num))

        prefixGcd.sort()

        answer = 0
        left = 0
        right = len(prefixGcd) - 1
        while left < right:
            answer += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        return answer