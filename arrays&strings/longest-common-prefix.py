class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        lens = map(len, strs)
        for i in range(min(lens)):
            flag = True
            current = strs[0][i]
            for j in strs:
                if j[i] != current:
                    flag = False
                    break
            if flag == True:
                res += current
            else:
                break
        return res