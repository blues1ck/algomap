class Solution:
    def reverseString(self, s: list[str]) -> None:
        s[:] = s[::-1]


a = Solution()
s = ["H","a","n","n","a","h"]
print(a.reverseString(s))
print(s)