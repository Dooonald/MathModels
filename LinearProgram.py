import pulp

#实例化我们的问题
model = pulp.LpProblem("Profit maximising problem", pulp.LpMaximize)
A = pulp.LpVariable('A', lowBound=0, cat='Integer')
B = pulp.LpVariable('B', lowBound=0, cat='Integer')
#目标函数
model += 30000 * A + 45000 * B, "profit"
#约束
model += 3 * A + 4 * B <= 30
model += 5 * A + 6 * B <= 60
model += 1.5 * A + 3 * B <= 21
#解决我们的问题
model.solve()
pulp.LpStatus[model.status]
#打印我们的决策变量值
print("Production of Car A = {}".format(A.varValue))
print("Production of Car B = {}".format(B.varValue))

#打印我们的目标函数值
print(pulp.value(model.objective))