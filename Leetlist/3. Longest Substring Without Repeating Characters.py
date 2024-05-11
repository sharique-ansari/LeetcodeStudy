# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i = 0
        # j = 0
        #
        # out = 0
        # dic = set()
        #
        # while j < len(s) and len(s)-i > out:
        #     if s[j] not in dic:
        #         dic.add(s[j])
        #         j+=1
        #         out = max(out, j-i)
        #     else:
        #         while s[i]!=s[j]:
        #             dic.remove(s[i])
        #             i+=1
        #         dic.remove(s[i])
        #         i+=1
        # return out
        
        # Method 2
        seen = {}
        left = 0
        output = 0

        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            output = max(output, right - left + 1)

        return output
