import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_list = fm.findSystemFonts()
path = font_list[font_list.index('C:\Windows\Fonts\malgun.ttf')]
font_name = fm.FontProperties(fname=path, size=18).get_name()
plt.rc('font', family=font_name)
countries = ['북한', '청와대', '부정선거', '우파', '우파 반대성향']
gold = [5, 90, 0.1, 0.9, 4]
colors = ['red', 'green', 'blue', 'yellow', 'cyan']
explode = [0, 0.2, 0, 0, 0]

plt.pie(gold, explode=explode, labels=countries, colors=colors, autopct="%.1f%%")
plt.title('좌파의 뇌구조')
plt.show()