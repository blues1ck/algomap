class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        res = 0
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if height[left] < height[right]:
                res += (min(left_max, right_max) - height[left])
                left += 1
            else:
                res += (min(left_max, right_max) - height[right])
                right -= 1
        return res


a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
