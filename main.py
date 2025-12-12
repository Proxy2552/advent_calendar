from fonction import intervale, fake_id1, fake_id2


def main1(l):
    Fakelist = []
    for i in range(0, len(l) - 1, 2):
        L = intervale(l[i], l[i + 1])
        F = fake_id1(L)
        Fakelist = Fakelist + F
    S = 0
    for n in Fakelist:
        S += n
    return S


def main2(l):
    Fakelist = []
    for i in range(0, len(l) - 1, 2):
        L = intervale(l[i], l[i + 1])
        F = fake_id2(L)
        Fakelist = Fakelist + F
    S = 0
    for n in Fakelist:
        S += n
    return S
