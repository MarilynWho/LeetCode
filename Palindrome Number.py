class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


x = 10
obj = Solution()
print(obj.isPalindrome(x))

