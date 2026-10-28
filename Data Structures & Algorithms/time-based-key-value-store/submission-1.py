class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        try:
            self.timeMap[key][timestamp] = value
        except KeyError:
            self.timeMap[key] = {timestamp: value}
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.timeMap:
            return res
        time_stamp_values = list(self.timeMap[key].keys())
        l, r = 0, len(time_stamp_values) - 1
        while(l<=r):
            mid = (l+r)//2
            if time_stamp_values[mid] <= timestamp:
                res = self.timeMap[key][time_stamp_values[mid]]
                l = mid + 1 
            else:
                r = mid - 1
        return res