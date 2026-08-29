class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        highest_volume = 0
        while left < right:
            length = right - left
            max_height = min(height[left], height[right])
            curr_volume = length * max_height
            highest_volume = max(highest_volume, curr_volume)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return highest_volume