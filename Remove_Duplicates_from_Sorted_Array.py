from os import remove
from typing import List
from unittest import result


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        resultArr = []
        remove = []
        for i, j in enumerate(nums):
            if j in resultArr:
                remove.append(i)
            else:
                resultArr.append(j)
        for x in remove[::-1]:
            nums.pop(x)
        return nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
obj = Solution()
print (obj.removeDuplicates(nums))