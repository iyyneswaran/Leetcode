class Solution:

  def closeStrings(self, word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
      return False

    word1_hash = {}
    word2_hash = {}

    for word in word1:
      word1_hash[word] = word1_hash.get(word, 0) + 1

    for word in word2:
      word2_hash[word] = word2_hash.get(word, 0) + 1

    return word1_hash.keys() == word2_hash.keys() and sorted(
        word1_hash.values()
    ) == sorted(word2_hash.values())

# or 
class Solution:

  def closeStrings(self, word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
      return False

    freq1 = [0] * 26
    freq2 = [0] * 26

    for ch in word1:
      freq1[ord(ch) - ord('a')] += 1

    for ch in word2:
      freq2[ord(ch) - ord('a')] += 1

    for i in range(26):
      if (freq1[i] == 0) != (freq2[i] == 0):
        return False

    return sorted(freq1) == sorted(freq2)