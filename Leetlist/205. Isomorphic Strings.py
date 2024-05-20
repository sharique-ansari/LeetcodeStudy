# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        translation_dic = {}

        for i,j in zip(s,t):
            if i in translation_dic:
                if translation_dic[i]!=j:
                    return False
            elif j in translation_dic.values():
                return False
            translation_dic[i]=j
        return True