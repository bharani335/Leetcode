class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(eval(num1+"*"+num2))

Obj = Solution()
print(Obj.multiply("345432", "855485"))