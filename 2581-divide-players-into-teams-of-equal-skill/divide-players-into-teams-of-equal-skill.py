class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        if n%2 !=0:
            return -1
        total_skills = 0
        target= skill[0]+skill[-1]
        for i in range(n//2):
            if skill[i]+skill[-i-1] != target:
                return -1
            else:
                total_skills += skill[i]*skill[-i-1]
        return total_skills
