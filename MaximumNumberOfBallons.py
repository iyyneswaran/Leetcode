class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)
        need = 'balloon'
        for ch in text:
            if ch in need:
                freq[ch] += 1
        
        if any(ch not in freq for ch in need):
            return 0
        else:
            return min(freq['b'] // 1, freq['a'] // 1, freq['l'] // 2, freq['o'] // 2, freq['n'] // 1)