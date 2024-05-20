# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split(" ")

        # #method1
        # if len(pattern)!=len(split_s):
        #     return False
        # return len(set(pattern))==len(set(split_s))==len(set(zip(pattern, split_s)))

        map_dic = {}
        if len(pattern)!=len(split_s):
            return False

        for i,j in zip(pattern, split_s):
            if i in map_dic:
                if map_dic[i] != j:
                    return False
                else:
                    pass
            else:
                if j in map_dic.values():
                    return False
                else:
                    map_dic[i] = j
        return True