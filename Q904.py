class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, best = 0, 0
        fruitCount = {}
        for right in range(len(fruits)):
            fruitCount[fruits[right]] = fruitCount.get(fruits[right], 0) + 1
            while len(fruitCount) > 2:
                fruitCount[fruits[left]] -= 1
                if fruitCount[fruits[left]] == 0:
                    del fruitCount[fruits[left]]
                left += 1
            best = max(best, right - left + 1)
            
        return best