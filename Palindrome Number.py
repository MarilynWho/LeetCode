import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or (x%10 == 0 and x!=0)):
            return False
        revers = 0
        while (x>revers):
            revers = revers*10 + x % 10
            x = math.floor(x/10)
        return x == revers or x == math.floor(revers/10)

'''
        if x< 0 or x%10 == 0 and x != 0:
            return False
        return str(x) == str(x)[::-1]
'''


x = 121
obj = Solution()
print(obj.isPalindrome(x))

