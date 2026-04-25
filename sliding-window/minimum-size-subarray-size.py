class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0
        left = 0 
        right = 0
        current_sum = 0
        min_len = len(nums) + 1
        while right < len(nums):
            current_sum += nums[right]
            while current_sum >= target and right >= left:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
            right += 1
        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len
                
a = Solution()
print(a.minSubArrayLen(4, [1, 4, 4]))

