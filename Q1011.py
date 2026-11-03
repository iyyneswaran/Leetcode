class Solution:
    def _can_ship(self, weights: list[int], capacity: int, days: int):
        required_days = 1
        current_load = 0
        for weight in weights:
            if current_load + weight > capacity:
                required_days += 1
                current_load = 0
            current_load += weight
        
        return required_days <= days

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if self._can_ship(weights, mid, days):
                right = mid
            else:
                left = mid + 1
            
        return left