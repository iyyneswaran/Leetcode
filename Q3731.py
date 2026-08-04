# sorting
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        temp = 0
        for i in range(nums[0], nums[-1], 1):
            if nums[temp] != i:
                res.append(i)
            else:
                temp += 1
        return res

# without sorting
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max_value, min_value = max(nums), min(nums)
        res = []
        for i in range(min_value + 1, max_value, 1):
            if i not in nums:
                res.append(i)
        return res