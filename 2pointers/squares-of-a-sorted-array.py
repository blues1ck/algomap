class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        if len(nums) < 2:
            return [x * x for x in nums]
        min_ind = len(nums) - 1
        for i in range(1, len(nums)):
            if abs(nums[i]) > abs(nums[i - 1]):
                min_ind = i - 1
                break
        left_counter = min_ind - 1
        right_counter = min_ind
        while right_counter < len(nums) and left_counter >= 0:
            if abs(nums[left_counter]) < abs(nums[right_counter]):
                res.append(nums[left_counter] * nums[left_counter])
                left_counter -= 1
            else:
                res.append(nums[right_counter] * nums[right_counter])
                right_counter += 1
        res += [x * x for x in nums[right_counter:]]
        res += [x * x for x in (nums[:left_counter + 1])[::-1]]
        
        return res
        
a = Solution()
print(a.sortedSquares([-2, -1, 0]))