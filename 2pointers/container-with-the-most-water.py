class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while (left < right):
            curr_h = min(height[left], height[right])
            curr_area = curr_h * (right - left)
            res = max(res, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7,9,9]))