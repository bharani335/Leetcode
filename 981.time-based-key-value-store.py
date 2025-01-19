#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])
        print(f"*** {self.d}")

    def get(self, key: str, timestamp: int) -> str:
        print(f"@@@@@@@@@@@@@@@@@@@@ {self.d}")
        x = self.d[key]
        L, M, R = 0, 0, len(x) - 1
        while L <= R:
            M = (L + R)//2
            print(f"==>> L, M, R, x[M]: {L, M, R, x[M]}")
            print(f"==>> M: {M}")
            print(f"==>> x[M]: {x[M]}")
            print(f"==>> timestamp: {timestamp}")
            if x[M][0] > timestamp:
                R = M - 1
                print(f"==>> R: {R}")
            else:
                L = M + 1
                print(f"==>> L: {L}")

        L -= 1

        print(f"000==>> L, R: {L, R}")
        # print('OOOOOO', x[L][0] <= timestamp, timestamp, x[L])
        return x[L][1] if L < len(x) and x[L][0] <= timestamp else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
