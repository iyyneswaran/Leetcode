class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = n * n
        sum_even = n * (n + 1)
        cf = []
        for i in range(1, min(sum_odd,sum_even)+1):
            if sum_odd % i == 0 and sum_even % i == 0:
                cf.append(i)
        return cf[-1]
    

# or
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n