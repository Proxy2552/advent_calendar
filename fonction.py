def intervale(a, b):
    L = [a]
    h = b - a
    for i in range(h):
        L.append(L[i] + 1)
    return L


def fake_id1(L):
    fakelist = []
    for i in L:
        S = str(i)
        n = len(S)
        if n > 1 and S[0] == "0":
            continue
        a = ""
        b = ""
        if len(S) % 2 == 0:
            for j in range(len(S) // 2):
                a += S[j]
            for q in range(len(S) // 2, len(S)):
                b += S[q]
            if a == b:
                f = a + b
                f = int(f)
                fakelist.append(f)
    return fakelist


def fake_id2(L):
    fakelist = []
    for i in L:
        S = str(i)
        n = len(S)
        est_fake = False
        for k in range(1, n // 2 + 1):
            if n % k == 0:
                R = n // k
                M = S[:k]
                if S == M * R:
                    est_fake = True
                    break
        if est_fake:
            fakelist.append(i)
    return fakelist
