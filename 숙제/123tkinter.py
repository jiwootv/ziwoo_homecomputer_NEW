# import tkinter as tk
# root = tk.Tk()
#
# label1 = tk.label(root, text="안녕하세요!!!")
# label1.pack
#
# root.mainroop
#
#
# from tkinter import *
# label1.pack()
#
# class MyFrame(Frame):
#   def__init__(self, master):
#       Frame.__init__(self, master)
#
#       self.master = master
#       self.master.title("고객 입력")
#       self.pack(fiil=BOTH, expand=True)
#
#       # 성명
#       frame1 = Frame(self)
#       frame1.pack(fill=x)
#
#       lblName = Label1(frame1, text="성명", width=10)
#       lblName.pack(side=LEFT, padx=10, expand=True)
#
#       entryName = Entry(frame1)
#       entryName.pack(fill=x, padx=10, expand=true)
#
#         # 회사
#         frame2 = Frame(self)
#         frame2.pack(fill=X)
#
#         lblComp = Label(frame2, text="회사명", width=10)
#         lblComp.pack(side=LEFT, padx=10, pady=10)
#       # 특징
#       frame3 = Frame(self)
#       frame3.pack(fiil=BOTH, expand=true)
#
#       lblComment = Label(frame2, text="회사명", width=10)
#       lblComment.pack(side=LEFT, anchor=N, padx=10, pady=10)
#
#         txtComment = Text(frame3)
#         txtComment.pack(fill=X, pady=10, padx=10)
#
#         # 저장
#         frame4 = Frame(self)
#         frame4.pack(fill=X)
#         btnSave = Button(frame4, text="저장")
#         btnSave.pack(side=LEFT, padx=10, pady=10)
#
#
# def main():
#     root = Tk()
#     root.geometry("600x550+100+100")
#     app = MyFrame(root)
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()

# import tkinter as tk
#
# def okClick():
#     name=b.get()
#     print(name)
#     a.config(text=name)
#
# def ret(event):
#     a.config(text='안녕')
#
# root = tk.Tk()
#
# a= tk.Label(text="안녕")
# a.config(font=("Courier", 100))
# a.pack()
#
# b=tk.Entry()
# b.pack()
#
# btn = tk.Button(root, text="OK", command=okClick)
# btn.pack()
#
# a.bind('<Button-1>', ret)
# root.mainloop()


# from tkinter import *
#
#
# def keyPressed(event):
#     # 키보드 문자하나 출력
#     a.config(text=event.char)
#
#
# root = Tk()
#
# frame = Frame(root, width=100, height=100)
# a=Label(frame, text='문자')
# a.pack()
# # Key 이벤트 바인딩
# frame.bind('<Key>', keyPressed)
# frame.place(x=0, y=0)
#
# # 키보드 포커를 갖게 한다
# frame.focus_set()
#
# root.mainloop()
#




import tkinter as tk


def cal1():
    d.config(text=int(a1.get()) * int(b1.get()))


def cal2():
    d.config(text=int(a1.get()) / int(b1.get()))


def cal3():
    d.config(text=int(a1.get()) + int(b1.get()))


def cal4():
    d.config(text=int(a1.get()) - int(b1.get()))


root = tk.Tk()

root.title("유지우-계산기 V 1.0")
root.geometry("640x400+100+100")
root.resizable(False, False)

a = tk.Label(root, text='첫번째 숫자를 입력하세요.')
a.config(font=('Roman', 30))
a.pack()
a1 = tk.Entry(root)
a1.pack()
b = tk.Label(root, text='두번째 숫자를 입력하세요.')
b.config(font=('Roman', 30))
b.pack()
b1 = tk.Entry(root)
b1.pack()
c1 = tk.Button(root, text='곱하기', command=cal1)
c2 = tk.Button(root, text='나누기', command=cal2)
c3 = tk.Button(root, text='더하기', command=cal3)
c4 = tk.Button(root, text='빼기', command=cal4)
c1.config(font=('Roman', 20))
c2.config(font=('Roman', 20))
c3.config(font=('Roman', 20))
c4.config(font=('Roman', 20))
c1.pack()
c2.pack()
c3.pack()
c4.pack()
d = tk.Label(root, text='결과값을 나타냅니다.')
d.pack()

root.mainloop()