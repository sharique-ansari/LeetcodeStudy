class Solution:
    def countTriples(self, n: int) -> int:
        out = set()
        for a in range(1,n):
            for b in range(1,n):
                if (b,a) in out:
                    out.add((a,b))
                    continue
                z = math.sqrt(a**2 + b**2)
                if z<=n and z.is_integer():
                    out.add((a,b))
        # print(out)
        return len(out)
