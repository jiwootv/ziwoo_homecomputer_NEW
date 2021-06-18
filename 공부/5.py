
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4 * np.pi, 2000)
y = np.sin(x)
y2 = np.cos(x) + 1
y3 = np.tan(x)

plt.plot(x, y, color='yellow', label='sine')
plt.ylim(-2, 2)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid(True)
plt.plot(x, y2, color='red', label='cosine')
plt.ylim(-2, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid(True)

plt.plot(x, y3, color='orange', label='tangent')
plt.ylim(-2, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
# months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# temp_fi = [15, 16, 18, 21, 24, 27, 28, 26, 23, 19, 16, 11]
# temp_ny = [2, 2, 4, 11, 16, 22, 25, 26, 24, 14, 12, 3]
#
# plt.plot(months, temp_fi, marker="o", color="red", linestyle=':', label="FL")
# plt.plot(months, temp_ny, marker="*", color="skyblue", linestyle=':', label="NY")
# plt.xlabel("Month")
# plt.ylabel("celcius Temprature")
# plt.title('Monthly Temperrature in temp_fl'