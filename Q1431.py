class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        GreatestNumberOfCandies = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= GreatestNumberOfCandies:
                result.append(True)
            else:
                result.append(False)
        
        return result