class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        length = len(nums)
        answer = [-1] * length
        for i in range(2 * length):
            curr_idx = i % length
            while stack and nums[stack[-1]] < nums[curr_idx]:
                answer[stack.pop()] = nums[curr_idx]
            if i < length:
                stack.append(curr_idx)
        return answer