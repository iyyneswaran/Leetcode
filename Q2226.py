class Solution:
    def _candies_check(self, candies: list[int], count: int, k) -> int:
        total_piles = 0
        for candy in candies:
            total_piles += candy // count
        
        return total_piles >= k


    def maximumCandies(self, candies: list[int], k: int) -> int:
        total_candies = sum(candies)
        if total_candies < k:
            return 0

        left = 1
        right = total_candies // k

        while left < right:
            mid = (left + right + 1) // 2

            if self._candies_check(candies, mid, k):
                left = mid
            else:
                right = mid - 1
        
        return left