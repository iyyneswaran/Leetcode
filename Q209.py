# brute force
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = []
        window = arr[:k]
        for i in range(k, len(nums)):
            for num in window:
                if num < 0:
                    result.append(nums[j])
                    break
            window.popleft()
            window.append(nums[i])

        return 0

# optimal solution using deque:
