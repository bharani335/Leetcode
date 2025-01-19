from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 2:
            if len(ratings) == 1:
                return 1
            else:
                if ratings[0] == ratings[1]:
                    return 2
                else:
                    return 3
        else:
            minimum_candies = 2 if ratings[0] == ratings[1] else 3
            previous = 1 if ratings[0] >= ratings[1] else 2
        for i in range(2, len(ratings)):
            if ratings[i - 1] >= ratings[i]:
                previous = 1
            else:
                previous += 1
            minimum_candies += previous
        return minimum_candies


print(Solution().candy(ratings=[1]))
print(Solution().candy(ratings=[1, 0, 2]))  # 5
print(Solution().candy(ratings=[1, 2, 2]))  # 4
print(Solution().candy(ratings=[1,3,2,2,1])) # 7
print(Solution().candy(ratings=[1,3,2,2,1])) # 7
print(Solution().candy(ratings=[1]))
print(Solution().candy(ratings=[1]))
print(Solution().candy(ratings=[1]))
