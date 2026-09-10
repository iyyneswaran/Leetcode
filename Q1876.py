class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        check_map = {}
        k = 3
        if len(s) < k:
            return 0
        for i in range(k):
            check_map[s[i]] = check_map.get(s[i], 0) + 1
        
        if len(check_map) == k:
            count += 1

        for i in range(k, len(s)):
            out_value = s[i-k]
            check_map[out_value] -= 1
            if check_map[out_value] == 0:
                del check_map[out_value]
            in_value = s[i]
            check_map[in_value] = check_map.get(in_value, 0) + 1
            if len(check_map) == k:
                count += 1
        
        return count