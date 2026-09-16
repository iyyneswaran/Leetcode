class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        best_len = float('inf')
        best_start = 0

        freqT =  {}
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1

        freqS = {}
        need, got = len(freqT), 0
        l_ptr = 0

        for r_ptr in range(len(s)):
            in_element = s[r_ptr]
            if in_element in freqT:
                freqS[in_element] = freqS.get(in_element, 0) + 1
                if freqS[in_element] == freqT[in_element]:
                    got += 1

            while got == need:
                window_size = r_ptr - l_ptr + 1
                if (window_size) < best_len:
                    best_len = window_size
                    best_start = l_ptr

                out_element = s[l_ptr]
                if out_element in freqT:
                    freqS[out_element] -= 1
                    if freqS[out_element] < freqT[out_element]:
                        got -= 1

                l_ptr += 1
                
        return "" if best_len == float('inf') else s[best_start: best_start + best_len]