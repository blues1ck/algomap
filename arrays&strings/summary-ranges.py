class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        res = []
        length = 0
        previous = nums[0]
        for i in nums[1:]:
            if i == previous + 1:
                length += 1
            else:
                if length == 0:
                    res.append(f"{previous}")
                else:
                    res.append(f"{previous - length}->{previous}")
                length = 0
            previous = i
        if length == 0:
            res.append(f"{previous}")
        else:
            res.append(f"{previous - length}->{previous}")
        return res


a = Solution()
print(a.summaryRanges([0,2,3,4,6,8,9]))