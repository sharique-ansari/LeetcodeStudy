# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])