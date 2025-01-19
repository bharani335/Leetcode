class Solution:
    def countAndSay(self, n: int) -> str:
        def call_me(n, temp):
            res = ""
            x = 0
            while x in range(len(temp)):
                counter = 1
                while x+1 < len(temp) and temp[x] == temp [x+1]:
                    counter += 1
                    x += 1
                res +=  str(counter)+str(temp[x])
                x += 1
            n -= 1
            if n <= 1:
                return res

            return call_me(n, res)
        if n == 1:
            return '1'
        return call_me(n, '1')
    
    # Copy
    # def countAndSay(self, n: int) -> str:
    #     if n == 1:
    #         return "1"
    #
    #     str1 = self.countAndSay(n - 1)
    #
    #     ans = ''
    #     ch = str1[0]
    #     count = 1
    #     for i in range(1, len(str1)):
    #         if ch != str1[i]:
    #             ans += str(count) + ch
    #             ch = str1[i]
    #             count = 1
    #         else:
    #             count += 1
    #     ans += str(count) + ch
    #
    #     return ans


obj = Solution()
print(obj.countAndSay(4))