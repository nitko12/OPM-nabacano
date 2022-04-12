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
    # pprint(l)

    l = [1, 2, 3, 4, 5]
    cnt = 6

    exactly_n(2, l)
