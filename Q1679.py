class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        appearance = {}
        opperations = 0
        i = 0
        while i < len(nums):
            need = k - nums[i]
            if need in appearance:
                appearance[need] -= 1
                opperations += 1
                if appearance[need] == 0:
                    del appearance[need]
            else:
                appearance[nums[i]] = appearance.get(nums[i], 0) + 1

            i += 1

        return opperations


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        appearance = {}
        opperations = 0

        for num in nums:
            need = k - num
            if need in appearance:
                opperations += 1
                appearance[need] -= 1
                if appearance[need] == 0:
                    del appearance[need]
            else:
                appearance[num] = appearance.get(num, 0) + 1

        return opperations