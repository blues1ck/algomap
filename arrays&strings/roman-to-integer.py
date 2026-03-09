class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I" : 1,
            "V" : 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        adder = s[-1]
        res = 0
        for i in s[::-1]:
            if symbols[i] == symbols[adder]:
                res += symbols[i]
            elif symbols[i] < symbols[adder]:
                res -= symbols[i]
            else:
                res += symbols[i]
                adder = i
        return res


a = Solution()
print(a.romanToInt("LVIII"))