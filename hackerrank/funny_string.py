def funnyString(s):
    rev_s = s[::-1] # กลับสตริง
    for i in range(1, len(s)):
        diff1 = abs(ord(s[i]) - ord(s[i-1]))
        diff2 = abs(ord(rev_s[i]) - ord(rev_s[i-1]))
        if diff1 != diff2:
            return "Not Funny"
    return "Funny"
