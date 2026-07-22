class TimeMap:


    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        valList = self.store.get(key,[])
        l = 0
        r = len(valList) - 1

        while l<=r:
            m = (l+r)//2
            if valList[m][1] <= timestamp:
                l = m+1
                res = valList[m][0]
            else:
                r = m-1
        return res

