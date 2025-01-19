import random


class RandomizedSet:
    def __init__(self):
        self.randomized_set = set()

    def insert(self, val: int) -> bool:
        size = len(self.randomized_set)
        self.randomized_set.add(val)
        return size == len(self.randomized_set) - 1

    def remove(self, val: int) -> bool:
        try:
            self.randomized_set.remove(val)
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.randomized_set))

    # 250ms Solution
    # def __init__(self):
    #     self.dict = {}
    #     self.list = []
    #     self.size = 0
    #
    # def insert(self, val: int) -> bool:
    #     if val not in self.dict:
    #         self.dict[val] = self.size
    #         self.list.append(val)
    #         self.size += 1
    #         return True
    #     return False
    #
    # def remove(self, val: int) -> bool:
    #     if val in self.dict:
    #         # print('======')
    #         # print(self.dict)
    #         idx = self.dict.pop(val)
    #         if idx != self.size - 1:
    #             self.list[self.size - 1], self.list[idx] = self.list[idx], self.list[self.size - 1]
    #             self.dict[self.list[idx]] = idx
    #         self.list.pop()
    #         self.size -= 1
    #         return True
    #     return False
    #
    # def getRandom(self) -> int:
    #     rand = int(random() * self.size)
    #     return self.list[rand]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()