from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc = dict(Counter(s))
        for i in t:
            if i not in sc:
                return False
            else:
                sc[i] -= 1
            if sc[i] < 0:
                return False
        return True
        


a = Solution()
print(a.isAnagram("anargam", "ganaram"))