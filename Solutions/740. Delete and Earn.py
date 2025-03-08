from collections import Counter
from json import loads
from sys import stdin
from typing import List


def deleteAndEarn(nums: List[int]) -> int:
    cout = Counter(nums)
    # print(cout)
    # 1,1,1,2,2,3,3,4,4,4
    previouskey = notpicked = picked = 0
    for i in sorted(cout.keys()):
        # print("---------")
        if i-1 == previouskey:
            res = max(picked, notpicked + i*cout[i])
            tmp = picked
            picked = res
            notpicked = tmp
            # picked, notpicked = notpicked + i*cout[i], 0 + picked
            # print("***", i, i*cout[i], res, picked, notpicked)
        else:
            notpicked = res
            res += i*cout[i]
            picked = res
            print("----", i, i*cout[i], res, picked, notpicked)
        previouskey = i
        # print i, i*cout[i], res, picked, notpicked)
    return res

f = open("user.out","w") 
for n in map(loads, stdin):
    arr = n.split(',')
    print(str(deleteAndEarn(arr)), file = f)
exit(0)