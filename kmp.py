def match_table(pattern):
    table = [0]
    k = 0
    for q in range(1, len(pattern)):
        while(k > 0 and pattern[k] != pattern[q]):
            k = table[k-1]
        if(pattern[k] == pattern[q]):
            k = k + 1
        table.append(k)
    return table


def kmp(text, pattern, table=None):
    if not table:
        table = match_table(pattern)
    q =  0
    found = []
    for i, l in enumerate(text):
        if pattern[q] == l:
            q += 1
        else:
            q = table[q-1]
        if q==len(pattern):
            found.append(i-q+1)
            q = table[q-1]
    return found
