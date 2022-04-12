from pyeda.inter import *
from pyeda.boolalg.expr import *
from math import comb
from pprint import pprint
import sys

cnt = 1


def get_cnt():
    global cnt
    cnt += 1
    # return 0
    return cnt - 1


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


def l_and(l):
    aa = get_cnt()

    for y in l:
        print(f"{y} -{aa} 0")
    print(" ".join(map(lambda i: f"-{i}", l)), f"{aa}", 0)

    return aa


def l_or(l):
    aa = get_cnt()

    for y in l:
        print(f"-{y} {aa} 0")
    print(" ".join(map(lambda i: f"{i}", l)), f"-{aa}", 0)

    return aa


def exactly_n(n, l):
    ll = []
    for x in itertools.combinations(l, n):
        aa = l_and(x)
        ll.append(aa)

    aa = l_or(ll)

    print(f"{aa} {aa} 0")  # must have one pair e.g.

    ll = []
    for x in itertools.combinations(l, n+1):
        aa = l_and(x)
        ll.append(aa)

    aa = l_or(ll)

    print(f"-{aa} -{aa} 0")  # can't have 3 e.g.


if __name__ == "__main__":

    t, v, k, a = map(int, sys.argv[1:5])

    b = a * (comb(v, t) // comb(k, t))

    # b = 1

    l = [[[get_cnt() for _ in range(v)] for _ in range(k)] for _ in range(b)]

    for x in range(b):
        bl = l[x]

        for y in range(k):
            ll = []
            for z in range(v):
                ll.append(bl[y][z])

            only_one(ll)

        for z in range(v):
            ll = []
            for y in range(k):
                ll.append(bl[y][z])

            only_less_one(ll)

    ds = []
    for x in range(b):
        bl = l[x]

        ll = []
        for z in range(v):
            # print([l[x][y][z] for y in range(k)])
            aa = l_or([l[x][y][z] for y in range(k)])
            ll.append(aa)

        d = []
        for h in itertools.combinations(ll, t):
            aa = l_and(h)
            d.append(aa)

        ds.append(d)

    # pprint(ds)

    for i, h in enumerate(itertools.combinations(range(1, 1+v), t)):
        # print(h)
        # pprint([ds[x][i] for x in range(b)])
        exactly_n(a, [ds[x][i] for x in range(b)])
