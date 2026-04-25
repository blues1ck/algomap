class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        meeted = set()
        left = 0
        right = 0
        res = 0
        while right < len(s):
            if s[right] not in meeted:
                res = max(res, right - left + 1)
                meeted.add(s[right])
                right += 1
            else:
                while s[left] != s[right]:
                    meeted.remove(s[left])
                    left += 1
                left += 1
                meeted.remove(s[right])
        return res


a = Solution()
print(a.lengthOfLongestSubstring("tmmzuxt"))