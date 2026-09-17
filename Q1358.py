class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {"a": 0, "b": 0, "c": 0}
        left = 0
        result = 0
        length = len(s)
        for right in range(length):
            freq[s[right]] += 1
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                result += (length - right)
                freq[s[left]] -= 1
                left += 1
        return result