class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # [-5, 1, 5, 0, -7] = 1
        length = len(gain)
        altitudes = [0] * (length + 1)
        altitudes[0] = 0

        for  i in range(length):
            altitudes[i + 1] = altitudes[i] + gain[i]

        return max(altitudes)
