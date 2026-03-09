class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter = 0
        res = ""
        while counter < min(len(word1), len(word2)):
            res += (word1[counter] + word2[counter])
            counter += 1
        res += word1[counter:]
        res += word2[counter:]
        return res