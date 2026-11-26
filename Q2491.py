class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        n = len(skill)
        num_teams = n // 2
        total_skill = sum(skill)

        if total_skill % num_teams != 0:
            return -1
        
        target = total_skill // num_teams
        skill.sort()
        left, right = 0, n - 1
        result = 0
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            result += skill[left] * skill[right]
            left += 1
            right -= 1

        return result