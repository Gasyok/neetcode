class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.timemap.get(key):
            self.timemap[key] = [(timestamp, value)]

        else:
            self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if not self.timemap.get(key, None):
            return ""
        vals = self.timemap.get(key, [])
        left, right = 0, len(vals) - 1
        res = ""
        while left <= right:
            mid = (right + left) // 2
            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
timeMap.set("love", "high", 10)
timeMap.set("love", "low", 20)
timeMap.get("love", 5)
timeMap.get("love", 10)
timeMap.get("love", 15)
timeMap.get("love", 20)
timeMap.get("love", 25)

# [key -> (value, timestamp), ...]
