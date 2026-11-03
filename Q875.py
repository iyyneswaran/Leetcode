class Solution:
    def total_hours_cal(self, piles: list[int], speed: int) -> int:
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / speed)

        return total_hours
        
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            total_hours = self.total_hours_cal(piles, mid)

            if total_hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans