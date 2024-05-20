# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        pointer = 0
        for char in t:
            # print(pointer, char, s[pointer])
            if pointer == len(s):
                return True
            if char == s[pointer]:
                pointer += 1

        return pointer == len(s)