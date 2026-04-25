from collections import deque


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        prev_zero = deque()
        curr_zeros = 0
        left = 0
        right = 0
        res = 0

        while right < len(nums):
            if nums[right] == 0:
                curr_zeros += 1
                prev_zero.append(right)
                if curr_zeros > k:
                    left = prev_zero.popleft() + 1
                    curr_zeros -= 1

            res = max(res, right - left + 1)
            right += 1

        return res
            

a = Solution()
print(a.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2



# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]