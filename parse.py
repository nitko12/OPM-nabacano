from math import comb
import sys


cnt = 1


def get_cnt():
    global cnt
    cnt += 1
    # return 0
    return cnt - 1


if __name__ == "__main__":

    t, v, k, a = map(int, sys.argv[1:5])

    b = a * (comb(v, t) // comb(k, t))

    l = [[[get_cnt() for _ in range(v)] for _ in range(k)] for _ in range(b)]

    d = {}

    for s in sys.stdin:
        if len(s) < 1:
            continue
        if s[0] != "v":
            continue

        for x in s.split()[1:]:
            if x[0] == "-":
                d[int(x[1:])] = 0
            else:
                d[int(x)] = 1

    for x in range(b):
        for y in range(k):
            for z in range(v):
                # print(l[x][y][z])
                print(f"{d[l[x][y][z]]:2}", end=" ")
            print()
        print()
        print()

    for x in range(b):
        for y in range(k):
            f = -1
            for z in range(v):
                # print(l[x][y][z])
                # print(f"{d[l[x][y][z]]:2}", end=" ")
                # print(d[l[x][y][z]])
                if d[l[x][y][z]] == 1:
                    f = z + 1

            print(f, end=" ")
        print()
