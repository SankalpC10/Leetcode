class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                five -= 1
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return "false"
        return "true"

s = Solution()
with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"{s.lemonadeChange(case)}\n")
exit(0)