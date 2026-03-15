class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for j in range(len(nums) - 2):
            if j > 0 and nums[j] == nums[j-1]:
                continue
            left = j + 1
            right = len(nums) - 1
            while (left < right):
                if  nums[left] + nums[right] + nums[j] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[j] < 0: 
                    left += 1
                else:
                    res.append([nums[left], nums[right], nums[j]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res


a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))