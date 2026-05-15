class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # key: key, val: list[(value, timestamp)] sorted ascending based on timestamp
        # since each call to set will have increasing timestamp, this can be O(1)
        val = (value, timestamp)
        if key not in self.map:
            self.map[key] = []
        self.map[key].append(val)

    def get(self, key: str, timestamp: int) -> str:
        val = self.map.get(key) # list of (value, timestamp)
        
        if not val:
            return ""
        
        l = 0
        r = len(val) - 1
        best = None

        # if timestamp does not exist, we will return the value associated with the timestamp
        # that is closest to and smaller than timestamp
        while l <= r:
            mid = l + (r - l) // 2
            cur_timestamp = val[mid][1]
            cur_value = val[mid][0]

            if cur_timestamp == timestamp:
                return cur_value
            elif cur_timestamp > timestamp:
                r = mid - 1
            elif cur_timestamp < timestamp:
                if not best:
                    best = val[mid]
                else:
                    if cur_timestamp > best[1]:
                        best = val[mid]
                l = mid + 1

        return "" if not best else best[0]
