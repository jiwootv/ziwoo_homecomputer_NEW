import matplotlib.pyplot as plt

weapon = ['Nuke', 'White phosphorus', 'Tank', 'Gun', 'Nipe']
students = [190, 1900, 10000, 13045, 33012]
colors = ['red', 'orange', 'yellow', 'green', 'blue']

plt.bar(weapon, students, color=colors)

plt.xlabel('weapon')
plt.ylabel('Students')
plt.title('Number of students in the US and Canada with weapons')

plt.show()