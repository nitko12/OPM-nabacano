from pyeda.inter import *
from pyeda.boolalg.expr import *
from math import comb
from pprint import pprint

t, v, k, a = 2, 6, 3, 2

b = a * (comb(v, t) // comb(k, t))

# b = 1

cnt = 1


def get_cnt():
    global cnt
    cnt += 1
    # return 0
    return cnt - 1


l = [[[get_cnt() for _ in range(v)] for _ in range(k)] for _ in range(b)]

# pprint(l)

# for x in range(b):
#     for y in range(k):
#         for z in range(v):
#             print(f"{l[x][y][z]:4}", end=" ")
#         print()
#     print()
#     print()


def only_one(l):
    print(" ".join(map(str, l)), 0)
    for x in range(len(l)):
        for y in range(x + 1, len(l)):
            print(f"-{l[x]} -{l[y]} 0")


def only_less_one(l):
    # print(" ".join(map(str, l)), 0)
    for x in range(len(l)):
        for y in range(x + 1, len(l)):
            print(f"-{l[x]} -{l[y]} 0")


def exactly_n(n, l):
    ll = []
    for x in itertools.combinations(l, n):
        aa = get_cnt()

        for y in x:
            print(f"{y} -{aa} 0")
        print(" ".join(map(lambda i: f"-{i}", x)), f"{aa}", 0)

        ll.append(aa)

    aa = get_cnt()

    for y in ll:
        print(f"-{y} {aa} 0")
    print(" ".join(map(str, ll)), f"-{aa}", 0)

    print(f"{aa} {aa} 0")  # must have one pair e.g.

    ll = []
    for x in itertools.combinations(l, n+1):
        aa = get_cnt()

        for y in x:
            print(f"{y} -{aa} 0")
        print(" ".join(map(lambda i: f"-{i}", x)), f"{aa}", 0)

        ll.append(aa)

    aa = get_cnt()

    for y in ll:
        print(f"{y} {aa} 0")
    print(" ".join(map(lambda i: f"{i}", x)), f"-{aa}", 0)

    print(f"-{aa} -{aa} 0")  # can't have 3 e.g.


if __name__ == "__main__":
    # only_one([1, 2, 3, 4, 5, 6])
    # only_one([7, 8, 9, 10, 11, 12])
    # only_one([13, 14, 15, 16, 17, 18])

    # only_less_one([1, 7, 13])
    # only_less_one([2, 8, 14])
    # only_less_one([3, 9, 15])
    # only_less_one([4, 10, 16])
    # only_less_one([5, 11, 17])
    # only_less_one([6, 12, 18])

    # cnt = 19
    # a1 = get_cnt()
    # a2 = get_cnt()
    # a3 = get_cnt()
    # a4 = get_cnt()
    # a5 = get_cnt()
    # a6 = get_cnt()

    # # -19 -20 -21 -22 23 -24

    # aa = "19"
    # ss = "1 7 13"
    # for x in ss.split():
    #     print(f"-{x} {aa} 0")
    # print(ss, f"-{aa}", 0)

    # aa = "20"
    # ss = "2 8 14"
    # for x in ss.split():
    #     print(f"-{x} {aa} 0")
    # print(ss, f"-{aa}", 0)

    # aa = "21"
    # ss = "3 9 15"
    # for x in ss.split():
    #     print(f"-{x} {aa} 0")
    # print(ss, f"-{aa}", 0)

    # aa = "22"
    # ss = "4 10 16"
    # for x in ss.split():
    #     print(f"-{x} {aa} 0")
    # print(ss, f"-{aa}", 0)

    # aa = "22"
    # ss = "5 11 17"
    # for x in ss.split():
    #     print(f"-{x} {aa} 0")
    # print(ss, f"-{aa}", 0)

    # aa = "23"
    # ss = "6 12 18"
    # for x in ss.split():
    #     print(f"-{x} {aa} 0")
    # print(ss, f"-{aa}", 0)

    # print(a1, a2, a3, a4, a5, a6)

    for x in range(b):
        bl = l[x]

        for y in range(k):
            ll = []
            for z in range(v):
                ll.append(bl[y][z])

            # print(ll)
            only_one(ll)

        for z in range(v):
            ll = []
            for y in range(k):
                ll.append(bl[y][z])

            # print(ll)
            only_less_one(ll)

    # svi t clani podskupovi
    # for w in itertools.combinations(range(1, 1 + v), t):
        # svi a clani podskupovi

    llls = []
    for x in range(b):
        bl = l[x]
        lll = []
        for z in range(v):
            ll = []
            for y in range(k):
                ll.append(bl[y][z])

            aa = get_cnt()

            for y in ll:
                print(f"-{y} {aa} 0")
            print(" ".join(map(str, ll)), f"-{aa}", 0)

            lll.append(aa)
            # print(ll)
            # only_less_one(ll)

        # koliko ih ima koji broj
        # pprint(lll)
        llls.append(lll)

    # w = (0, 1)

    # pprint(llls)

    ds = []
    for x in llls:
        d = {}

        for h in itertools.combinations(list(range(1, len(x)+1)), t):
            # print(h)
            aa = get_cnt()

            for y in h:
                print(f"{x[y-1]} -{aa} 0")
            print(" ".join(map(lambda x: f"-{x}", h)), f"{aa}", 0)

            d[h] = aa

        ds.append(d)

    # pprint(ds)

    gg = 0
    for h in itertools.combinations(range(1, 1 + v), t):
        # print(h)
        # print([x[h] for x in ds])

        # print()
        exactly_n(a, [x[h] for x in ds])
        # print()

        if gg == 2:
            break
        gg += 1
