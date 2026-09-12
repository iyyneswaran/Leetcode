# My own approach without refering anything
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freqMap = {}
        left = 0
        best = 0
        for right in range(len(s)):
            freqMap[s[right]] = freqMap.get(s[right], 0) + 1
            while freqMap[s[right]] > 1:
                freqMap[s[left]] -= 1
                if freqMap[s[left]] == 0:
                    del freqMap[s[left]]
                left += 1
            best = max(best, right - left + 1)
        
        return best

# Got it from ChatGPT
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right

            max_length = max(max_length, right - left + 1)

        return max_length

# using set [Got it from leetcode, I didn't wrote it]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_ptr = 0
        existing_string = set()
        global_max = 0
        for r_ptr in range(len(s)):
            while s[r_ptr] in existing_string:
                existing_string.remove(s[l_ptr])
                l_ptr += 1
            existing_string.add(s[r_ptr])
            global_max = max(global_max, len(existing_string))
        return global_max