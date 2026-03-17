class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res = []
        for x in operations:
            if x.lstrip('-').isdigit():
                res.append(int(x))
            elif x == '+':
                res.append(res[-1] + res[-2])
            elif x == 'C':
                res.pop(-1)
            elif x == 'D':
                res.append(2 * res[-1])
        return sum(res)
        

a = Solution()
print(a.calPoints(["5","-2","4","C","D","9","+","+"]))

print("-2".lstrip('-').isdigit())