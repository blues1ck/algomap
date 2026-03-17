from inspect import stack


class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in s:
            if len(a) == 0:
                a.append(i)
            elif i == '}':
                if a[-1] == '{':
                    a.pop(-1)
                else:
                    a.append(i)
            elif i == ')':
                if a[-1] == '(':
                    a.pop(-1)
                else:
                    a.append(i)
            elif i == ']':
                if a[-1] == '[':
                    a.pop(-1)
                else:
                    a.append(i)
            else:
                a.append(i)
        return (len(a) == 0)


a = Solution()
print(a.isValid("(]"))