import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_list = fm.findSystemFonts()
path = font_list[font_list.index('C:\Windows\Fonts\malgun.ttf')]
font_name = fm.FontProperties(fname=path, size=18).get_name()
plt.rc('font', family=font_name)

for font in font_list:
    fp = fm.FontProperties(fname=font)
    fn = fp.get_name()
    print("%s >> %s" % (fp, fn))

f = open('gra.csv')
data = csv.reader(f)
next(data)
resulty2 = []
resulty = []
resultx = []

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '11' and row[0].split('-')[2] == '10':
            resulty.append(float(row[-1]))
            resulty2.append(float(row[-2]))
            resultx.append(str(row[0].split('-')[0]) + '년')

plt.plot(resultx, resulty, 'hotpink', label='최고기온')
plt.plot(resultx, resulty2, 'blue', label='최저기온')
plt.legend()

plt.title('내 생일의 기온 변화 그래프')
plt.show()
