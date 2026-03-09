class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        if len(intervals) == 1:
            return intervals
        res = []
        overlp_beggining = intervals[0][0]
        expect_ending = intervals[0][1]
        for i in intervals[1:]:
            if expect_ending < i[0]:
                res.append([overlp_beggining, expect_ending])
                overlp_beggining = i[0]
                expect_ending = i[1]
            else:
                expect_ending = max(expect_ending, i[1])

        res.append([overlp_beggining, expect_ending])
        return res

a = Solution()
print(a.merge([[4,7], [1, 10], [11, 11]]))