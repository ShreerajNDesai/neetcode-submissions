class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        res = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l,seen[s[r]]+1)
            seen[s[r]] = r
            res = (r-l)+1 if (r-l)+1 > res else res
        return res