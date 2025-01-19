from typing import List

# # # 90ms Solution
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         if sum(gas) < sum(cost):
#             return -1
#         total = 0
#         start = 0
#         for i in range(len(gas)):
#             total += (gas[i] - cost[i])
#             if total < 0:
#                 total = 0
#                 start = i+1
#         return start

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        answer = 0

        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1

        return answer if total_gain >= 0 else -1

        # 1006ms Solution
        # if sum(gas) < sum(cost):
        #     return -1
        #
        # curr_gas = 0
        # index = 0
        # for i in range(len(gas)):
        #     curr_gas += gas[i] - cost[i]
        #
        #     if curr_gas < 0:
        #         curr_gas = 0
        #         index = i + 1
        #
        # return index


print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))  # 3
print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))  # -1
print(Solution().canCompleteCircuit(gas=[4], cost=[5]))  # -1
print(Solution().canCompleteCircuit(gas=[2], cost=[2]))  # 0
print(Solution().canCompleteCircuit(gas=[3, 3, 4], cost=[3, 4, 4]))  # -1
