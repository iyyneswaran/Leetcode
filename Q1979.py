from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        return gcd(smallest, largest)


# or 
from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return gcd(nums[0], nums[len(nums)-1])