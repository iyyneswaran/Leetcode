class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for numPassengers, from_km, to_km in trips:
            diff[from_km] += numPassengers
            diff[to_km] -= numPassengers
        
        check = 0
        for i in range(len(diff)):
            check += diff[i]
            if check > capacity:
                return False
        
        return True