from pyomo.contrib.simplemodel import *
import cvxpy as cp

c = 2.0  # cost per unit
b = 2.5  # backorder cost
h = 0.5  # holding cost
d = {1: 15, 2: 60, 3: 72, 4: 78, 5: 82}  # demand
p = {1: 0.2, 2: 0.3, 3: 0.1, 4: 0.1, 5: 0.3}  # probability of demand

scenarios = range(1, 6)

m = SimpleModel()
x = cp.Variable(4, )
y = m.var('y', scenarios)

# constraints for every scenario

for i in scenarios:
    m += y[i] >= (c - b) * x + b * d[i]
    m += y[i] >= (c + h) * x - h * d[i]

m += sum(y[i] * p[i] for i in scenarios)

status = m.solve("glpk")  # call external solver

print("Status = %s" % status.solver.termination_condition)

print("%s = %f" % (x, value(x)))

for i in y:
    print("%s = %f" % (y[i], value(y[i])))

print("Objective = %f" % value(m.objective()))
