class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        index_stack = []
        output = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1]:
                temp_stack.pop()
                prev_idx = index_stack.pop()
                output[prev_idx] = idx - prev_idx

            temp_stack.append(temp)
            index_stack.append(idx)

        return output