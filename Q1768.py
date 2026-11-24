class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []       
        p1, p2 = len(word1), len(word2)
        
        for i in range(max(p1, p2)):
            if i < p1:
                ans.append(word1[i])
            
            if i < p2:
                ans.append(word2[i])
        
        return "".join(ans)