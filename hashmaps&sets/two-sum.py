class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(nums, reverse=True)
        for i in range(len(sorted_nums) - 1):
            for j in range(i + 1, len(sorted_nums)):
                if sorted_nums[i] + sorted_nums[j] == target:
                    a, b = sorted_nums[i], sorted_nums[j]
                    i_a = nums.index(a)
                    i_b = len(nums) - nums[::-1].index(b)
                    return [i_a, i_b]
                    

a = Solution()
print(a.twoSum([2,3,3,3,15], 6))