class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        left = 0
        right = len(numbers) - 1
        while (numbers[left] + numbers[right] != target):
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]
            
a = Solution()
print(a.twoSum([2,7,9,11,15], 9))