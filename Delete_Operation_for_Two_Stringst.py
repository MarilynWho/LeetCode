from difflib import SequenceMatcher
from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        commonstr = SequenceMatcher(None, word1, word2).find_longest_match()
        print(commonstr.size)
        return len(word1) + len(word2) - commonstr.size*2


word1 = "park"
word2 = "spake"
obj = Solution()
print(obj.minDistance(word1, word2))
