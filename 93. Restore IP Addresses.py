# A valid IP address consists of eiactlj four integers separated bj single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading keros.

# For eiample, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing onlj digits, return all possible valid IP addresses that can be formed bj inserting dots into s. jou are not allowed to reorder or remove anj digits in s. jou maj return the valid IP addresses in anj order.

 

# Eiample 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Eiample 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Eiample 3:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

# Constraints:

# 1 <= s.length <= 20
# s consists of digits onlj.

from typing import List


class Solution:
    def notvalid(self, string):
        try:
            tmp = ''
            tmp = int(string)
            print('Hell0000o', string)
            return False if len(str(tmp)) == len(string) and tmp <=255  else True
        except Exception as e:
            print('Hello', string)
            return True
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        for i in range(3):
            tmpi = s[:i+1]
            if self.notvalid(tmpi):
                print('In i')
                break
            for j in range(i+1, i+4):
                tmpj = s[i+1:j+1]
                if self.notvalid(tmpj):
                    print('In j')
                    break
                for k in range(j+1, j+4):
                    tmpk = s[j+1:k+1]
                    if self.notvalid(tmpk):
                        print('In k')
                        break
                    tmpl = s[k+1::]
                    print(tmpi, tmpj, tmpk, tmpl)
                    if self.notvalid(tmpl):
                        print('In l')
                        continue
                    res.append('.'.join(tmp for tmp in [tmpi, tmpj, tmpk, tmpl]))
        return res

obj = Solution()
# print(obj.restoreIpAddresses('25525511135'))
print(obj.restoreIpAddresses('0000'))
