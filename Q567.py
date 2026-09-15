class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        freqS1 = {}
        for ch in s1:
            freqS1[ch] = freqS1.get(ch, 0) + 1
        
        freqS2 = {}

        init_window = s2[:k]
        for ch in init_window:
            freqS2[ch] = freqS2.get(ch, 0) + 1

        if freqS1 == freqS2:
            return True
        
        for j in range(k, len(s2)):
            out_element = s2[j - k]
            freqS2[out_element] -= 1
            if freqS2[out_element] == 0:
                del freqS2[out_element]
            
            in_element = s2[j]
            freqS2[in_element] = freqS2.get(in_element, 0) + 1
            
            if freqS1 == freqS2:
                return True
        
        return False
