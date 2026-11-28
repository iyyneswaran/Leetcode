class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrence = {}
        for num in arr:
            occurrence[num] = occurrence.get(num, 0) + 1

        seen = set()
        for count in occurrence.values():
            if count in seen:
                return False
            seen.add(count)
        
        return True
