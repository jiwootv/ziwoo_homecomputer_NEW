
import matplotlib.pyplot as plt

months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
temp_fi = [15, 16, 18, 21, 24, 27, 28, 26, 23, 19, 16, 11]
temp_ny = [2, 2, 4, 11, 16, 22, 25, 26, 24, 14, 12, 3]

plt.plot(months, temp_fi, marker="o", color="red", linestyle=':', label="FL")
plt.plot(months, temp_ny, marker="*", color="blue", linestyle=':', label="NY")
plt.xlabel("Month")
plt.ylabel("celcius Temprature")
plt.title('Monthly Temperrature in temp_fl(fi: red, NY: blue)')
plt.show()