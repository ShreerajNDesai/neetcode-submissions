class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0]* len(temperatures)
        for i,j in enumerate(temperatures):
            while stk and j > stk[-1][0]:
                v,idx = stk.pop()
                res[idx] = i - idx

            stk.append((j,i))
        return res