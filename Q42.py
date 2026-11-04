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