class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        stones_to_remove = 10
        turns = 0
        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            turns += 1
        
        return False if turns % 2 == 0 else True

