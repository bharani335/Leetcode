import collections
import itertools
import re


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        matches = re.findall("\*{2,}", p)
        print(matches)
        matches = sorted(collections.Counter(matches), key=lambda x: len(x), reverse=True)
        print(p)
        print(matches)
        for match in matches:
            p = p.replace(match, "*")
            print(p)

        pattern_size = len(p)
        source_size = len(s)
        t = [[False] * (pattern_size + 1)] * (source_size + 1)
        if pattern_size > 0 and p[0] == "*":
            t[0][1] = True

        t[0][0] = True
        for i in range(1, len(t)):
            for j in range(1, len(t[0])):
                if p[j-1] == "?" or s[i-1] == p[j-1]:
                    t[i][j] = t[i-1][j-1]
                elif p[j-1] == "*":
                    t[i][j] = t[i][j - 1] or t[i - 1][j]

        return t[source_size][pattern_size]


Obj = Solution()
# source = "aa"
# pattern = "*"
# True

source = "aaaaa"
pattern = "?a*"
# True

# source = "adceb"
# pattern = "*a*b"
# # True

# source = ""
# pattern = "****"
# # True

source = "aa"
pattern = "a"
# False

# source = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
# pattern = "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"
# # True

# source = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
# pattern = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"

# source = "babbabaabaaabbbbabbbbbababaaaaabababbbbabbbabaabbb"
# pattern = "bb***ba*b***aa*bba***"
# # False

print(Obj.isMatch(source, pattern))

# [a-z]{1}
