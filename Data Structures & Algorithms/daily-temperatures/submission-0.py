class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            j = i + 1
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    result[i] = j - i
                    break
                j += 1

        return result
        