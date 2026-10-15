class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        difference_array = [0] * 101
        for birth, death in logs:
            difference_array[birth - 1950] += 1
            difference_array[death - 1950] -= 1
        
        max_population = 0
        current_population = 0
        max_year = 1950

        for i in range(len(difference_array)):
            current_population += difference_array[i]

            max_population, max_year = (current_population, 1950 + i) if current_population > max_population else (max_population, max_year)

        
        return max_year