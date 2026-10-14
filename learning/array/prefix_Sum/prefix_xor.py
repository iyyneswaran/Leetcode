from typing import List

def build_prefix(nums: List) -> List:
    prefix = [0] * (len(nums) + 1)

    for i, num in enumerate(nums):
        prefix[i + 1] = prefix[i] ^ num

    return prefix

def range_xor(prefix_XOR: List, left: int, right: int) -> int:
    return prefix_XOR[right + 1] ^ prefix_XOR[left]


nums = list(map(int, input().split()))
prefix_XOR = build_prefix(nums)
print(prefix_XOR)
print(range_xor(prefix_XOR, 1, 3))