"""이 프로그램을 가지고 우리가 배운 프레임과 버튼등을 이용해서 변경해서
더 보기 좋게 만들어 보세요.
"""

import tkinter, random

"""이 프로그램은 아주 간단한 퀴즈를 만드는 프로그램입니다."""
score = 0
check = 0
q1 = ['(과학 중학교 1학년 과정) E=mc^2는 무엇일까요?', '(수학)파이 는 무엇일까요?', "(기타)아프리카 잠비아 칠루비 섬의 주식은 무엇인가요?",
      '(과학)절대영도는??', '다음중 인간이 번식하는데 필요한 세포가 아닌 것은?']
q2 = ['', '2', '2', '1', '4', '1']
q3 = [['힘 = 가속도 * 질량', '에너지 = 질량 * 빛의 속도 ^2', 'a의 제곱 + b의 제곱 = c의 제곱', '(x-3)*x/2', 'C= π*d = 2*π*r', 'a*2) + (b*2) = (a+b) * 2'], ['3.1415926235897932384626....', '3.1415926535897932384626....', '3.1315926535897932384626....', '3.1415926535897942384626....'], ['시마', '쩌우 까우', '옥수숫가루', '고구마, 감자'],
      ['−253.15 °C', '−273.35 °C', '−273.11 °C', '−273.15 °C'], ['난자 + 정자', '정자 + 수정란', '난자 + 정자 * 2', '난자 + 수정란']]

"""정답과 오답을 알려주는 함수"""
mg = ['어떻게 그렇게 멍청할수가 있는 거죠?', '지나가던 사람도 가다 욕을 할 정도의 지능!', 'ㅋㅋㅋㅋㅋㅋㅋ 이 바보', '맵다 매워....',
      '코드 뜯었죠? 이거 원래 안나오는 오답 메시지인데... 꺼.지.세.요']

def yesorno(a='', a1=''):
    global score, check, mg
    if a1 == a and not a == '':
        label2.config(text="정답입니다.")
        score = score + 1
    elif a1 == a and a == '':
        pass
    else:

        label2.config(text="오답입니다!!!!" + mg[random.randint(1,4)])
    return


window = tkinter.Tk()

window.title("유지우의 개빡치는 퀴즈프로그램 V 1.0")
window.geometry("1040x800+100+100")
window.resizable(False, False)

label1 = tkinter.Label(window, text="다음에 나오는 퀴즈를 풀어 주세요.")
label1.config(font=("Courier", 20))
label1.pack()
label2 = tkinter.Label(window, text='아주 쉬운 퀴즈 지금 부터 시작합나다!!! 문제는' + str(len(q1)) + '문제 입니다.')
label2.config(font=("Courier", 10))
label2.pack()
label3 = tkinter.Label(window, text='여기에 문제가 출제 됩니다. 엔터키를 누루면 시작합니다.', anchor='n', fg='blue', justify='left')
label3.config(font=("Courier", 13), )
label3.pack()


def paroblem(event):
    global check
    if not check == len(q1) + 1:
        aa = entry.get()
        if check < len(q1):
            text = str()
            text = text + str(check + 1) + '번 문제: ' + q1[check]
            for b1, b2 in enumerate(q3[check]):
                text = text + '\n'
                text = text + '  ' + str(b1 + 1) + ')' + str(b2)
            label3.config(text=text)
        yesorno(q2[check], aa)
        check += 1
    else:
        label2.config(text="하나도 '안' 수고하셨어요")
        label3.config(text='풀어주셔서 감사합니다.')
    entry.delete(0, "end")
    label1.config(text='당신의 점수는' + str(score * 20) + '입니다.')
    pass


entry = tkinter.Entry(window)
entry.bind("<Return>", paroblem)
entry.config(font=("Courier", 20))
entry.pack()

window.mainloop()