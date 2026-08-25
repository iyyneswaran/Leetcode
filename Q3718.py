class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hashTable = set(nums)
        multiple = k
        while multiple in hashTable:
            multiple += k
        return multiple