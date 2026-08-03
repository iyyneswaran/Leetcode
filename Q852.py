# Two pointer approch
# Approach 1:
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        ans = 0
        while left <= right:
            curr_max = max(arr[left], arr[right])
            if curr_max > ans:
                ans = curr_max
            left += 1
            right -= 1
        return arr.index(ans)

# Approach 2:
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        ans = -1
        index = 0
        while left <= right:
            curr_max = max(arr[left], arr[right])
            if curr_max > ans:
                ans = curr_max
                index = left if arr[left] > arr[right] else right
            left += 1
            right -= 1
        return index


# One liner
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))


# Optimal code 
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

            
        