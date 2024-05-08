# https://leetcode.com/problems/relative-ranks/
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        out = []
        dic = {}
        for i in range(len(score)):
            if i==0:
                dic[sorted_score[0]] = "Gold Medal"
            elif i==1:
                dic[sorted_score[1]] = "Silver Medal"
            elif i==2:
                dic[sorted_score[2]] = "Bronze Medal"
            else:
                dic[sorted_score[i]]=f"{i+1}"
        for i in score:
            out.append(dic[i])
        return out