from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # note = {i:ransomNote.count(i) for i in set(ransomNote)}
        # magz = {i:magazine.count(i) for i in set(magazine)}
        # for i in note.keys():

        #     if i not in magz:
        #         return False
        #     if note[i]>magz[i]:
        #         return False
        # return True

        # Use Counter python library
        str1 = Counter(ransomNote)
        str2 = Counter(magazine)
        print(str1, str2)
        return str1 & str2 == str1