from ast import Break
from typing import List

def take_second(elem):
    return elem[1]

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        close_targ = 0
        ind = []
        for i, val in sorted(enumerate(nums), key=take_second, reverse=True):
            if close_targ+val <= target:
                close_targ += val
                ind.append(i)
            else:
                continue
        return ind


nums = [-3, 4, 3, 90]
target = 0
obj = Solution();
print(obj.twoSum(nums, target))