from difflib import SequenceMatcher
from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        commonstr = SequenceMatcher(None, word1, word2).get_matching_blocks()
        print(commonstr)
        commonsize = 0
        for i in commonstr:
            commonsize += i.size
        print(commonsize)
        return len(word1) + len(word2) - commonsize*2


word1 = "abcdeabcdx"
word2 = "abcdxabcde"

obj = Solution()
print(obj.minDistance(word1, word2))
