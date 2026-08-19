class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=sum(piles)
        right=-(-(left-len(piles)+1)//(h-len(piles)+1))
        left=-(-left//h) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            mh = 0
            for p in piles:
                mh += (p + mid - 1) // mid
            if mh <= h:
                right = mid
            else:
                left = mid
        
        return right