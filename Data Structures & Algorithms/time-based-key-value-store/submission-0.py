class TimeMap:

    def __init__(self):
        self.data = defaultdict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = {}
        if timestamp not in self.data[key]:
            self.data[key][timestamp] = []

        self.data[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        seen = 0
        for time in self.data[key]:
            if time <= timestamp:
                seen = max(seen, time)
        
        return "" if seen == 0 else self.data[key][seen][-1]
                

        
