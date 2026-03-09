class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        current = max(nums)
        for i in nums:
            if abs(i) > abs(current):
                pass
            elif abs(i) == abs(current):
                current = max(current, i)
            else:
                current = i
        return current


a = Solution()
print(Solution.findClosestNumber(a, [-4, -2, 1, 4, 8]))