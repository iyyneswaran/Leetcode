# Using inbuild index()
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        length = len(nums)

        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))
        
        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)

        bothFront = right + 1
        bothBack = length - left
        bothDirection = (left + 1) + (length - right)
        
        return min(bothFront, bothBack, bothDirection)

# without using inbuilt function 
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxValue, minValue = max(nums), min(nums)
        length = len(nums)
        if length == 1:
            return 1
        minIndex = 0
        maxIndex = 0
        for i in range(length):
            if nums[i] == maxValue:
                maxIndex = i
            if nums[i] == minValue:
                minIndex = i
        left = min(minIndex, maxIndex)
        right = max(minIndex, maxIndex)
        bothFront = right + 1
        bothBack = length - left
        bothDirection = (left + 1) + (length - right)
        return min(bothFront, bothBack, bothDirection)
