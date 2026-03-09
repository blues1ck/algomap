class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = 1
        if nums.count(0) > 1:
            return [0] * len(nums)
        flag = False
        for i in nums:
            if i != 0:
                prod *= i
            else:
                flag = True
        if flag:
            return [0 if x!= nums.index(0) else prod for x in range(len(nums))]
        return [prod // x if x != 0 else prod for x in nums]


a = Solution()
print(a.productExceptSelf([-1,1,0,-3,0]))
