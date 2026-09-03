class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums.sort()
        best_sum = sum(nums[:3])
        for i in range(length - 2):
            left, right = i + 1, length - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum - target) < abs(best_sum - target):
                    best_sum = curr_sum
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return best_sum

# or 
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums.sort()
        best_sum = nums[0] + nums[1] + nums[2]
        for i in range(length - 2):
            left, right = i + 1, length - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum - target) < abs(best_sum - target):
                    best_sum = curr_sum
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return best_sum