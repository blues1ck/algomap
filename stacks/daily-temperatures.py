class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        indexes = []

        for i in range(len(temperatures)):
            while indexes and temperatures[i] > temperatures[indexes[-1]]:
                prev_idx = indexes.pop()
                answer[prev_idx] = i - prev_idx
            indexes.append(i)

        return answer


a = Solution()
print(a.dailyTemperatures([73,74,75,71,69,72,76,73]))
