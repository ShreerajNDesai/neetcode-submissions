from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data[key]
        if not arr:
            return ""

        if timestamp >= arr[-1][0]:
            return arr[-1][1]
            
        if timestamp < arr[0][0]:
            return ""

        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res