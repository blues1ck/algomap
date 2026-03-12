class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return (not len(set(nums)) == len(nums))


a = Solution()
print(a.containsDuplicate([1, 2, 3, 1]))