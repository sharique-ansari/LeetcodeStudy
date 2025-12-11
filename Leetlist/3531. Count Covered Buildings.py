# https://leetcode.com/problems/count-covered-buildings/description/?envType=daily-question&envId=2025-12-11
# 3531. Count Covered Buildings

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # TLE error (attempt 1)
        # covered = 0 # output variable
        # buildings_set = set((x,y) for x,y in buildings)

        # # left-right
        # covered_left = set()
        # for col in range(1,n+1):
        #     seen = False
        #     for row in range(1,n+1):
        #         if (row,col) in buildings_set:
        #             if not seen:
        #                 seen = True
        #             else:
        #                 covered_left.add((row,col))
        # # print(covered_left)

        # covered_top = set()
        # for row in range(1,n+1):
        #     seen = False
        #     for col in range(1,n+1):
        #         if (row,col) in buildings_set:
        #             if not seen:
        #                 seen = True
        #             else:
        #                 covered_top.add((row,col))
        # # print(covered_top)

        # covered_bottom = set()
        # for row in range(1,n+1):
        #     seen = False
        #     for col in range(n,0,-1):
        #         if (row,col) in buildings_set:
        #             if not seen:
        #                 seen = True
        #             else:
        #                 covered_bottom.add((row,col))
        # # print(covered_bottom)

        # covered_right = set()
        # for col in range(1,n+1):
        #     seen = False
        #     for row in range(n,0,-1):
        #         if (row,col) in buildings_set:
        #             if not seen:
        #                 seen = True
        #             else:
        #                 covered_right.add((row,col))
        # # print(covered_right)


        # return len(set.intersection(covered_left, covered_right, covered_top, covered_bottom))


        # I feel like using a dictionary would be a correct DS choice here
        # Attempt 2 using dict to store neighbours
        # same_rows = defaultdict(list)

        # same_cols = defaultdict(list)


        # for row, col in buildings:

        #     same_rows[row].append(col)

        #     same_cols[col].append(row)

        # print(same_rows)

        # print(same_cols)


        # covered = 0


        # for brow, bcol in buildings:

        #     row_neigbours = same_rows[brow]

        #     col_neighbours = same_cols[bcol]

        #     c1, c2 , r1, r2 = False, False, False, False

        #     for c in row_neigbours:

        #         if c < bcol:

        #             c1 = True

        #         if c > bcol:

        #             c2 = True

        #     for r in col_neighbours:

        #         if r > brow:

        #             r1 = True

        #         if r < brow:

        #             r2 = True

        #     if r1 and r2 and c1 and c2:

        #         covered+=1

        #         continue

        # return covered

        # Attempt 3; don't store all neighbours, only the boundries
        same_rows = defaultdict(dict)
        same_cols = defaultdict(dict)

        for row, col in buildings:
            same_rows[row]['min'] = min(same_rows[row].get("min", math.inf),col)
            same_rows[row]['max'] = max(same_rows[row].get('max', -1),col)

            same_cols[col]['min'] = min(same_cols[col].get("min", math.inf),row)
            same_cols[col]['max'] = max(same_cols[col].get('max', -1),row)
        # print(same_rows)
        # print(same_cols)

        covered = 0

        for brow, bcol in buildings:

            if bcol < same_rows[brow]['max'] and bcol > same_rows[brow]['min'] and brow < same_cols[bcol]['max'] and brow> same_cols[bcol]['min']:
                covered +=1
        return covered
            


        
