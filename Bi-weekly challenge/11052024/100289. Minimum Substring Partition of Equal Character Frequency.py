
def is_balanced(s):
        if len(s) == 1:
            return True
        char_dic = {}
        for i in s:
            if i in char_dic:
                char_dic[i] += 1
            else:
                char_dic[i] = 1
        comp = char_dic[s[0]]
        if len(char_dic) == 1 and comp > 1:
            return False
        for count in char_dic.values():
            if count != comp:
                return False
        return True

def balance_rec(s):
    out = []
    for i in range(1, len(s)):
        s1, s2 = s[:i], s[i:]
        print(s1, s2)
        s1_b = is_balanced(s1)
        s2_b = is_balanced(s2)
        if s1_b and s2_b:
            out.append(2)
        elif s1_b:
            out.append(1 + balance_rec(s2))
        elif s2_b:
            out.append(1 + balance_rec(s1))
        else:
            out.append(balance_rec(s1) + balance_rec(s2))
    if out:
        return min(out)
    else:
        return 1

balance_rec("aaaaa")