class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0]* len(temperatures)
        for i,j in enumerate(temperatures):
            while stk and j > stk[-1][0]:
                value,index = stk.pop()
                res[index] = i - index

            stk.append((j,i))
        return res