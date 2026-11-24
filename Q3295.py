# Optimal approach:
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWordsHash = set()

        for bannedWord in bannedWords:
            bannedWordsHash.add(bannedWord) 

        count = 0
        for word in message:
            if word in bannedWordsHash:
                count += 1
                if count == 2:
                    return True

        return False


# Brute force: => TLE
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        occurenceTable = {}
        for word in message:
            if word in bannedWords:
                occurenceTable[word] = occurenceTable.get(word, 0) + 1
            
                if occurenceTable[word] >= 2:
                    return True
            
            if len(occurenceTable) >= 2:
                return True
        
        return len(occurenceTable) >= 2


# Brute force => TLE:
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        
        for word in message:
            if word in bannedWords:
                count += 1
                if count == 2:
                    return True

        return False