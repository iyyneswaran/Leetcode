class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        length = len(s)
        
        if k > length:
            return []

        result = []

        freqP = {}
        for ch in p:
            freqP[ch] = freqP.get(ch, 0) + 1

        freqS = {}
        init_window = s[:k]
        for ch in init_window:
            freqS[ch] = freqS.get(ch, 0) + 1
        
        if freqP == freqS:
            result.append(0)
        
        for i in range(k, length):
            out_element = s[i - k]
            freqS[out_element] -= 1
            if freqS[out_element] == 0:
                del freqS[out_element]
            
            in_element = s[i]
            freqS[in_element] = freqS.get(in_element, 0) + 1

            if freqS == freqP:
                result.append(i - k + 1)
        
        return result