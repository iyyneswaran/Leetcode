class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        k = len(numFreq)

        if k == 0:
            return 0

        cFreq = {}
        count, res, l_ptr = 0, 0, 0
        n = len(nums)

        for r_ptr, num in enumerate(nums):
            cFreq[num] = cFreq.get(num, 0) + 1
            if cFreq[num] == 1:
                count += 1

            while count == k:
                res += n - r_ptr

                cFreq[nums[l_ptr]] -= 1
                if cFreq[nums[l_ptr]] == 0:
                    del cFreq[nums[l_ptr]]
                    count -= 1
                    
                l_ptr += 1

        return res