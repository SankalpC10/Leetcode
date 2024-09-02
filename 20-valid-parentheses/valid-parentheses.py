class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complementary_dict = {')':'(','}':'{',']':'['}
        for i in s:
            if i in complementary_dict and len(stack) != 0 :
                if stack[-1]==complementary_dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0

        