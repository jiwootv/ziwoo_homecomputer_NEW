"""이 프로그램을 가지고 우리가 배운 프레임과 버튼등을 이용해서 변경해서
더 보기 좋게 만들어 보세요.(어 이게 왜있지)
(선생님이 썼네)
"""

import tkinter as tk

"""이 프로그램은 아주 간단한 퀴즈를 만드..들어논 프로그램 입니다.."""
text12345 = '가나다라마바사아자차카타파하어쩌구저쩌구'
root = tk.Tk()
def tktxt(text, size):
    global txt12345
    txt12345 = tk.Label(text=text)
    txt12345.pack()
    txt12345.config(font=("Counrier", size))
tktxt('퀴즈를 시작하겠습니다.', 20)
tktxt('뜬금없이 시작해서 죄송하지만, 일단 시작하도록 하겠습니다.', 10)
tktxt('일단은 저 버튼을 누1르시면 됩니다.', 10)
tktxt('2번에도 쉽지 않을 것입니다.', 10)
tktxt('zㅏ 그럼 넘어가죠!', 20)

bc = tk.Entry()
bc.pack()



root.mainloop()
