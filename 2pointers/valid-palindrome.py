class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            a = s[left]
            b = s[right]
            if not(a.isalpha() or a.isalnum()):
                left += 1
                continue
            if not(b.isalpha() or b.isalnum()):
                right -= 1
                continue
            a = a.lower()
            b = b.lower()
            if a != b:
                return False
            left += 1
            right -= 1
        return True


a = Solution()
print(a.isPalindrome("asdf 1u1 - ,,, fdsa"))