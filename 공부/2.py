
import matplotlib.pyplot as plt

countries = ['USA', 'korea', 'China', 'Russia', 'germany']
gold = [5, 90, 0.1, 0.9, 4]
colors = ['red', 'green', 'blue', 'yellow', 'cyan']
explode = [0, 0.1, 0, 0, 0]

plt.pie(gold, explode=explode, labels=countries, colors=colors, autopct="%.1f%%")
plt.title('medal')
plt.show()