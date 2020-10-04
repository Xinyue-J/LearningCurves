import matplotlib.pyplot as plt
import numpy as np
import random

a = np.arange(-2, 2, 0.0001)
x = np.arange(-1, 1, 0.0001)

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2, 2)
plt.ylim(-1, 5)

# random
k = 0
b = 0
N = 10000
for i in range(0, N):
    x1 = random.random() * 2 - 1
    x2 = random.random() * 2 - 1
    # plt.plot(a, (x1 + x2) * a - x1 * x2, 'b', linewidth=0.2)
    k += (x1 + x2)
    b -= x1 * x2

k_aver = k / N
b_aver = b / N
var_list = []
Eout_list = []
for i in range(0, 100):
    x1 = random.random() * 2 - 1
    x2 = random.random() * 2 - 1
    var_list.append(((x1 + x2) * x - x1 * x2 - k_aver * x + b_aver) ** 2)
    Eout_list.append(((x1 + x2) * x - x1 * x2 - x * x) ** 2)
    plt.plot(a, (x1 + x2) * a - x1 * x2, 'b', linewidth=0.2)
print(k_aver)
print(b_aver)
plt.plot(a, k_aver * a - b_aver, 'g')
plt.plot(a, a * a, 'r')
plt.show()

bias = np.mean((k_aver * x - b_aver - x * x) ** 2)
var = np.mean(var_list)
Eout = np.mean(Eout_list)
print('bias:', bias)
print('var:', var)
print('bias+var:', bias + var)
print('Eout:', Eout)
