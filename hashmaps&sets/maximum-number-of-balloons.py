from typing import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        exemplar = dict(Counter("balloon"))
        counter = len(text)
        d = dict(Counter(text))
        for i in exemplar:
            if i not in d:
                return 0
            else:
                if d[i] < exemplar[i]:
                    return 0
            counter = min(counter, d[i] // exemplar[i])
        return counter


a = Solution()
print(a.maxNumberOfBalloons("baloon"))


