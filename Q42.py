# Monotonic queue: Top - 55.62%
class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        water_quantity = 0
        
        for current in range(len(height)):
            while stack and height[stack[-1]] < height[current]:
                bottom_idx = stack.pop()
                
                if not stack:
                    break
                
                left_idx = stack[-1]
                
                distance = current - left_idx - 1
                bounded_height = min(height[current], height[left_idx]) - height[bottom_idx]
                
                water_quantity += distance * bounded_height
                
            stack.append(current)
            
        return water_quantity

    
# Two pointers - Top: 96.18%
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_quantity = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_quantity += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_quantity += right_max - height[right]
                right -= 1
                
        return water_quantity