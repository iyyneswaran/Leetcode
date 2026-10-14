from typing import List

def build_prefix(words: List) -> List:
    vowels = set("aeiou")
    prefix_count = [0] * (len(words) + 1)

    for i, word in enumerate(words):
        qualify_check = word[0] in vowels and word[-1] in vowels
        prefix_count[i + 1] = prefix_count[i] + int(qualify_check)

    return prefix_count

def range_query(prefix_count: List, left: int, right: int) -> int:
    return prefix_count[right + 1] - prefix_count[left]


words = ["aba", "bcb", "ece", "aa", "e"]

prefix_count = build_prefix(words)
print(prefix_count)

print(range_query(prefix_count, 1, 4))
print(range_query(prefix_count, 0, 2))