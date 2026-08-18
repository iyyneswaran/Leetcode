# Built-in - Optimal 
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Brute force
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqMap = {}
        for i, ch in enumerate(s):
            if ch not in freqMap:
                freqMap[ch] = 1
            else:
                freqMap[ch] += 1
        
        for i, ch in enumerate(t):
            if ch not in freqMap:
                return False
            else:
                freqMap[ch] -= 1
                if freqMap[ch] < 0:
                    return False
        return True