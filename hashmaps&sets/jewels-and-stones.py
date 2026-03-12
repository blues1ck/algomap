class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        for i in stones:
            for j in jewels:
                if i == j:
                    counter += 1
                    break
        return counter
        