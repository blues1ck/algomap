class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        itterator = 0
        if len(s) == 0:
            return True
        for i in t:
            if i == s[itterator]:
                itterator += 1
                if itterator == len(s):
                    break
            else:
                pass
        return (len(s) == itterator)


a = Solution()
print(a.isSubsequence("b", "abc"))