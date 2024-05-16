# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers

        start = 0
        end = len(s) - 1

        while start < end:
            if s[start].isalnum():
                if s[end].isalnum():
                    if s[start].lower()!=s[end].lower():
                        return False
                    start += 1
                    end -= 1
                else:
                    end -= 1
            else:
                start += 1
        return True