from math import comb
import gurobipy as gp
from gurobipy import GRB
import itertools
from pprint import pprint
from sympy.logic.boolalg import to_cnf
from sympy.abc import A, B, D

#            2-(6, 3, 2)
t, v, k, a = 2, 43, 7, 1

b = a * (comb(v, t) // comb(k, t))


model = gp.Model('sudoku')

vars = model.addVars(b, k, v, vtype=GRB.BINARY, name='G')
# vars = [[[0 for z in range(v)] for y in range(k)] for x in range(b)]
# cnt = 1

# for x in range(b):
#     for y in range(k):
#         for z in range(v):
#             vars[x][y][z] = cnt
#             cnt += 1

# pprint(vars)

# unique constraint
for x in range(b):
    for y in range(k):
        l = []
        for z in range(v):
            l.append(vars[x, y, z])

        # print(l)
        model.addConstr(gp.quicksum(l) == 1)


for x in range(b):
    for z in range(v):
        l = []
        for y in range(k):
            l.append(vars[x, y, z])
        model.addConstr(gp.quicksum(l) <= 1)


# 0 0 0 0 1
# 1 0 0 0 0
# 0 0 1 0 0
# 0 1 0 0 0

for w in itertools.combinations(range(v), t):
    # print(w)

    tps = []
    for x in range(b):
        tt = [model.addVar(vtype=GRB.BINARY, name='t1') for _ in range(t)]

        l = [[] for _ in range(t)]

        for y in range(k):

            for i in range(t):
                l[i].append(vars[x, y, w[i]])

        for i in range(t):
            model.addConstr(gp.quicksum(l[i]) == tt[i])

        tp = model.addVar(vtype=GRB.BINARY, name='t')
        model.addGenConstrAnd(tp, tt, "and")
        tps.append(tp)

    model.addConstr(gp.quicksum(tps) == a)


# model.setObjective(-gp.quicksum(tps))

model.optimize()

solution = model.getAttr('X', vars)

for x in range(b):
    for y in range(k):
        for z in range(v):
            if solution[x, y, z] > 0.5:
                print(z, end=" ")
    print()
