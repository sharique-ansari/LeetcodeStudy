# 3606. Coupon Code Validator
# https://leetcode.com/problems/coupon-code-validator/description/

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        out = []
        line_id = {
            "electronics": 1,
            "grocery": 2,
            "pharmacy": 3,
            "restaurant": 4,
        }
        valid_business = set(["electronics", "grocery", "pharmacy", "restaurant"])
        for s, b, a in zip(code, businessLine,isActive):

            if a and b in valid_business:
                if s and all(c.isalnum() or c == '_' for c in s):
                    out.append([s,b])
        out.sort(key = lambda a: (line_id[a[1]], a[0]))
        return [a[0] for a in out]
