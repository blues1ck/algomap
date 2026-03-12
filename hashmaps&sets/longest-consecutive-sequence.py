class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        snums = set(nums)
        for num in snums:
            if num - 1 not in snums:
                counter = 1
                for i in range(num + 1, len(snums) + num):
                    if i in snums:
                        counter += 1
                    else:
                        break
                res = max(res, counter)
        return res

a = Solution()
print(a.longestConsecutive([100,150,200,1,2,152,0,3,6,8,4,9,11]))