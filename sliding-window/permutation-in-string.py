from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()
        left = 0

        for right, ch in enumerate(s2):
            window[ch] += 1

            # Keep the window size equal to len(s1).
            if right - left + 1 > len(s1):
                left_char = s2[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1

            if right - left + 1 == len(s1) and window == need:
                return True

        return False

s1 = "adc"
s2 = "dcda"
a = Solution()
print(a.checkInclusion(s1, s2))

