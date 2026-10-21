from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
        prefix_RC = [0] * (len(runningCosts) + 1)
        for i, num in enumerate(runningCosts):
            prefix_RC[i + 1] = prefix_RC[i] + num
        
        max_robots = 0
        l_ptr = 0
        max_ChargeTimes = deque()

        for r_ptr, num in enumerate(chargeTimes):
            while max_ChargeTimes and chargeTimes[max_ChargeTimes[-1]] < num:
                max_ChargeTimes.pop()
            max_ChargeTimes.append(r_ptr)

            k = r_ptr - l_ptr + 1
            sumValue = prefix_RC[r_ptr + 1] - prefix_RC[l_ptr]

            while max_ChargeTimes and (chargeTimes[max_ChargeTimes[0]] + k * sumValue) > budget:
                if max_ChargeTimes[0] == l_ptr:
                    max_ChargeTimes.popleft()
                    
                l_ptr += 1
                k = r_ptr - l_ptr + 1
                sumValue = prefix_RC[r_ptr + 1] - prefix_RC[l_ptr]

            max_robots = max(max_robots, r_ptr - l_ptr + 1)
        
        return max_robots