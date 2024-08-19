class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count =0
        for i in details:
            for j in range(len(i)):
                if i[j].isalpha():
                    age = int(i[j+1:j+3])
                    if age > 60:
                        count += 1
        return count