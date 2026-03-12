class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidat = None
        counter = 0
        for num in nums:
            if counter == 0:
                candidat = num
            if num == candidat:
                counter += 1
            else:
                counter -= 1
        return candidat


a = Solution()
print(a.majorityElement([2, 2, 2, 1, 1, 1, 1]))