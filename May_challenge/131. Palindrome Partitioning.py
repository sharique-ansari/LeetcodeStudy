# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/description/?envType=daily-question&envId=2024-05-22


def partition(s: str):
    final_out = []

    def rec_fun(out, index):
        print(out)

        if index == len(s):
            print(out)
            return

        rec_fun(out + list(s[index]), index + 1)

        # don't add index to list
        if out:
            # fg = out[-1]
            # dg = s[index]
            # fgh = fg.join(dg)
            # print(fgh)
            rec_fun(out[-1]+s[index], index + 1)

        # add index to out


    rec_fun([], 0)
    return final_out

partition(s="abcd")