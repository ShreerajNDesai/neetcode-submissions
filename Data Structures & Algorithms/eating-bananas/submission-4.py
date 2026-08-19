class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        total = sum(piles)
        l,r = (total - 1) // h + 1,(total - n - 1) // (h - n + 1)+1
        
        while l <= r:
            mid = (l+r) // 2

            if sum((pile-1) // mid + 1 for pile in piles) <= h:
                r = mid-1
            else:
                l = mid+1
        return l