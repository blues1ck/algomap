class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = 0
        for right in range(k):
            curr_sum += nums[right]
        max_avg = curr_sum / k
        left = 0
        while right < len(nums):
            max_avg = max(max_avg, curr_sum / k)
            right += 1
            if right == len(nums):
                break
            curr_sum += nums[right]
            curr_sum -= nums[left]
            left += 1
        return max_avg


a = Solution()
print(a.findMaxAverage([3,3,4,3,0],3))