# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = Counter(s)
        dic_t = Counter(t)
        return dic_s==dic_t