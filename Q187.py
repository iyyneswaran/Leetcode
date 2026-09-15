# Fixed sliding window + freq map: beats 16.47%
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        freq = {}
        result = []

        length = len(s)
        if length < 10:
            return []

        window = s[:10]
        freq[window] = 1

        for i in range(10,length):
            window = s[i-10+1: i+1]
            freq[window] = freq.get(window, 0) + 1
            if freq[window] == 2:
                result.append(window)
            
        return result

# Same as above but initial window is calculated in a single loop inside of explicitily declaring it: Beats 26.98%
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        freq = {}
        result = []

        length = len(s)
        if length < 10:
            return []

        for i in range(len(s) - 9):
            window = s[i:i+10]
            freq[window] = freq.get(window, 0) + 1
            if freq[window] == 2:
                result.append(window)
            
        return result

# Two set approach: Beat 42.03%
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen, result = set(), set()

        for i in range(len(s) - 9):
            window = s[i:i+10]
            if window in seen:
                result.add(window)
            else:
                seen.add(window)
            
        return list(result)
