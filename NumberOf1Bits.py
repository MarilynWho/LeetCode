class Solution(object):
    
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        r=0
        for i in "{0:b}".format(n):
            if i == '1':
                r = r+1
        return r
        """
        binary = 0
        while (n != 0):
            binary += (n % 2)
            n//=2
        return binary

n = 0b00000000000000000000000000001011
obj = Solution();
print(obj.hammingWeight(n))