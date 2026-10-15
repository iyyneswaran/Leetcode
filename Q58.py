class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_List = s.split()
        return len(s_List[len(s_List) - 1])