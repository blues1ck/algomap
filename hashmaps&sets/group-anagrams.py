class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for i in strs:
            a = "".join(sorted(i))
            if a in res:
                res[a].append(i)
            else:
                res[a] = [i]
        print(res)
        return [res[j] for j in res]


a = Solution()
print(a.groupAnagrams(["123", "321", "aaa"]))
