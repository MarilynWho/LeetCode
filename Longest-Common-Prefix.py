from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def _iter():
            for i in zip(*strs):
                if i.count(i[0]) == len(i):
                    yield i[0]
                else:
                    return
        return ''.join(_iter())


strs = ["flower", "flow", "flight"]

obj = Solution()
print(obj.longestCommonPrefix(strs))
