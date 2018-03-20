import matplotlib.pyplot as plt
import numpy as np

RLIST = [0.33333]
DLIST = [0.33333]
ILIST = [0.33333]

init = np.array([0.33333, 0.33333, 0.33333])
initMat = np.matrix(init)
print(initMat)
print(initMat.shape)

trans = np.array([[0.75,0.05,0.20],[0.20,0.60,0.20],[0.40,0.20,0.40]])
transMat = np.matrix(trans)
print(transMat)

res = initMat * transMat
RLIST.append(res[0, 0])
DLIST.append(res[0, 1])
ILIST.append(res[0, 2])

for i in range(40):
    res = res * transMat
    RLIST.append(res[0, 0])
    DLIST.append(res[0, 1])
    ILIST.append(res[0, 2])

print(res.shape)
print(res)

plt.plot(RLIST)
plt.plot(DLIST)
plt.plot(ILIST)
plt.xlabel('Time')
plt.ylabel('Voting percent')
plt.annotate('DemocraticParty',xy = (5,0.2))
plt.annotate('RepublicanParty',xy = (5,0.5))
plt.annotate('IndependentCandidate',xy = (5,0.25))
plt.show()