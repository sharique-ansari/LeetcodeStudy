# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_dic = defaultdict(list)

        for word in strs:
            word_s = ''.join(sorted(word))
            out_dic[word_s].append(word)
        return list(out_dic.values())
