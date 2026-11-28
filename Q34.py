class Solution:
    def _find_position(self, nums: list[int], target: int, first: bool) -> int:
        f_pos = float(inf)
        s_pos = float(-inf)

        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target and first:
                right = mid - 1
                f_pos = min(f_pos, mid)

            elif nums[mid] == target and not first:
                left = mid + 1
                s_pos = max(s_pos, mid)

            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        if left == right and nums[left] == target:
            if first:
                f_pos = min(f_pos, left)
            else:
                s_pos = max(s_pos, left)

        if first:
            return f_pos if f_pos != float(inf) else -1

        if not first:
            return s_pos if s_pos != float(-inf) else -1 
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_pos = self._find_position(nums, target, True)
        second_pos = self._find_position(nums, target, False)

        return [-1, -1] if first_pos == -1 or second_pos == -1 else [first_pos, second_pos]