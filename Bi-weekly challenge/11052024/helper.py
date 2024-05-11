s = "abcdef"
for i in range(len(s)):
    s1, s2 = s[:i], s[i:]
    print(s1, s2)