class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if len(set(temperatures)) == 1:
            return [0]*n

        res = []
        l = 0
        r = 1

        while l < n:
            if r >= n:
                l+=1
                r=l+1
                res.append(0)
            elif r <= n and temperatures[l] < temperatures[r]:
                res.append(r-l)
                l+=1
                r=l+1
            else:
                r+=1
        return res
