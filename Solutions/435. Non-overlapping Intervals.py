from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        left = 0
        right = 1
        count = 0
        while right < len(intervals):
            # Non overlapping
            if intervals[left][1] <= intervals[right][0]:
                left = right
                right += 1
                continue
            # Remove Right, while right is partially overlapped with left
            elif intervals[left][1] <= intervals[right][1]:
                right += 1
                count += 1
                continue
            # Remove Left, while right is fully overlapped with left
            elif intervals[left][1] >= intervals[right][1]:
                left = right
                right += 1
                count += 1
        return count

        # ans, prevHi = 0, -inf
        # for x, y in sorted(intervals, key=lambda x: x[1]):
        #     if x < prevHi:
        #         ans += 1
        #     else:
        #         prevHi = y
        # return ans

obj = Solution()
intervals =[[1,2],[2,3]]
intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
print(obj.eraseOverlapIntervals(intervals))