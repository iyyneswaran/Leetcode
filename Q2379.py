class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        length = len(blocks)

        if length < k:
            return 0

        min_count = float('inf')
        curr_count = 0

        for i in range(k):
            if blocks[i] == 'W':
                curr_count += 1
        
        min_count = min(min_count, curr_count)

        for i in range(k, length):
            if blocks[i - k] == 'W':
                curr_count -= 1
            if blocks[i] == 'W':
                curr_count += 1
            min_count = min(curr_count, min_count)

        return min_count