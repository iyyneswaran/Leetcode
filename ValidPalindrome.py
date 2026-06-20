class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True
    

# or 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().translate(
            str.maketrans('', '', """:.,/@#!~`$%^&*()-_=+{}[]'"<>|;?\ """)
        )

        if len(s) == 1 or len(s) == 0:
            return True
        
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        
        return True