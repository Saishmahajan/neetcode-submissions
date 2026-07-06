class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result = []

        # for i in range(len(temperatures)):
        #     days = 0

        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             days = j - i
        #             break

        #     result.append(days)

        # return result

        stack = []
        result = [0] * len(temperatures)
        days = 0

        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                
                index = stack.pop()
                result[index] = i - index
            stack.append(i)

        return result
    