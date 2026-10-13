class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m_nums = []
        for num in nums:
            if num == 0:
                m_nums.append(-1)
            else:
                m_nums.append(num)

        prefixSum = 0
        freqLen = {0: -1}
        maxLen = 0
        for i, num in enumerate(m_nums):
            prefixSum += num
            
            if prefixSum in freqLen:
                maxLen = max(maxLen, i - freqLen[prefixSum])
            
            if prefixSum not in freqLen:
                freqLen[prefixSum] = i
        
        return maxLen
