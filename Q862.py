class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        length = len(nums)
        prefix = [0] * (length + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        dq = deque()
        best_len = float('inf')
        for i in range(length + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                best_len = min(best_len, i - dq[0])
                dq.popleft()
                
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)

        return best_len if best_len != float('inf') else -1