class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # # Should be TLE
        # out = 0
        # for i in range(1,len(nums)-1):
        #     prev = nums[:i]
        #     next = nums[i+1:]
        #     out+=prev.count(nums[i]*2)*next.count(nums[i]*2)
        #     # print(prev, nums[i], next)
        # return out

        out = 0
        mod = 10**9 + 7

        freq_prev = Counter()
        freq_next = Counter(nums)
        freq_next[nums[0]]-=1

        for i in range(1,len(nums)-1):
            freq_prev[nums[i-1]]+=1
            freq_next[nums[i]]-=1

            out=(out+freq_prev[nums[i]*2]*freq_next[nums[i]*2])%mod
        return out
