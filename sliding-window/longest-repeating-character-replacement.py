class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        counts = {}
        left = 0
        max_freq = 0
        best = 0

        for right, ch in enumerate(s):
            counts[ch] = counts.get(ch, 0) + 1
            max_freq = max(max_freq, counts[ch])

            while (right - left + 1) - max_freq > k:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best