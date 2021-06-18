import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_list = fm.findSystemFonts()
path = font_list[font_list.index('C:\Windows\Fonts\malgun.ttf')]
font_name = fm.FontProperties(fname=path, size=18).get_name()
plt.rc('font', family=font_name)

countries = ['미국', '우크라이나', '조게껍질나라', '바카야로이드', '발냄새 나는 검정고무신', 'ga임의 나라', '중국', '대한민국']
gold = [34, 54, 24, 54, 24, 77, 0.1, 99]
silver = [23, 41, 32, 14, 34, 19, 0.1, 182]
bronze = [23, 41, 32, 14, 34, 19, 0.1, 200]

bottom_silver = gold
bottom_bronze = [a + b + 3 for a, b in zip(gold, silver)]

fig, ax = plt.subplots()
p1 = ax.bar(countries, gold, color='gold', label='Gold')
p2 = ax.bar(countries, silver, bottom=bottom_silver, label='Silver')
p3 = ax.bar(countries, bronze, bottom=bottom_bronze, label='Bronze')

plt.xlabel('나라')
plt.xlabel('메달수')
plt.xlabel('3095년 가루바나나 올림픽')
plt.legend()

ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p3, label_type='center')
plt.show()