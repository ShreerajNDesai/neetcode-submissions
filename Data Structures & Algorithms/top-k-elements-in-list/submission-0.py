class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sett = set(nums)
        dic = {}
        for i in sett:
            count = nums.count(i)
            dic[i]=count
        return sorted(dic, key=dic.get, reverse=True)[:k]


            