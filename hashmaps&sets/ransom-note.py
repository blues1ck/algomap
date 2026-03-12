# from collections import Counter


# class Solution():
#   def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#     ransomFreqs = Counter(ransomNote)
#     magazineFreqs = Counter(magazine)
#     for ransomKey in ransomFreqs.keys():
#       ransomFreq = ransomFreqs[ransomKey]
#       if ransomKey not in magazineFreqs.keys():
#         return False
#       elif ransomFreq > magazineFreqs[ransomKey]:
#         return False
#     return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = dict()
        for i in magazine:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        for j in ransomNote:
            if j not in letters:
                return False
            else:
                letters[j] -= 1
            if letters[j] < 0:
                return False
        return True