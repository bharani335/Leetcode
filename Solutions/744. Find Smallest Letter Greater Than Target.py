

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        L, M, R = 0, 0, len(letters)-1
        while L < R:
            M = (L + R)//2
            if letters[M] > target:
                R = M
            elif letters[M] <= target:
                L = M + 1
            print(L, M, R)

        print(L, M, R)
        return letters[L] if L==R and letters[L] > target else letters[0]
    
        # 33ms Solution
        # left, right = 0, len(letters)
        # while left < right:
        #     mid = (left + right) // 2
        #     left, right = (mid + 1, right) if letters[mid] <= target else (left, mid)
        # print(f'"{letters[left % len(letters)]}"')

Obj = Solution()
letters, target = ["c","f","j"], "a"
# letters, target = ["x","x","y","y"], "z"
# letters, target = ["x","x","y","y"], "x"
print(Obj.nextGreatestLetter(letters, target))