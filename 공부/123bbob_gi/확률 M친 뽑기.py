import tkinter
import tkinter as tk
import random
import time

root = tk.Tk()
root.geometry('1200x1200')
root.resizable(False, False)

"""
뽑기 코드
"""
rank_kinds = [["일반", "희귀", "초희귀", "영웅", "신화", "전설", "크로마틱"], ["노말", "레어", "슈퍼 레어", "초 슈퍼 레어", "울트라 슈퍼 레어", "초 울트라 슈퍼 레어", "래전드 울트라 초 슈퍼 레어"], ['C', 'B', 'A', 'A+', 'S', 'SR', 'SSS']]

rank = random.randint(0, 100)
print(rank)
if 0 < rank < 50:
    b = random.randint(1, 30)
    if 0 < b < 12:
        label1 = tkinter.Image("dee-b.gif")
        label1.tk()
        label2 = tk.Label(root, text="그냥 흔한 놈. 빨간 적에 큰 데미지를 주고 가끔 살아남는다. 모든 적에 맷집이 좋고, 공격력은 10번 때려서 고양이 한 마리 죽일 정도.")
        label2.pack()