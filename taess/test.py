# def find_prime_factorizations(n):
#     prime_factorizations = []
#     i = 2
#     while n != 1:
#         if n % i == 0:
#             n /= i
#             prime_factorizations.append(i)
#         else:
#             i += 1
#
#     return prime_factorizations
#
#
# a, b = map(int, sys.stdin.readline().split())
# a, b = find_prime_factorizations(a), find_prime_factorizations(b)
# a_x = [0] * (max(a) + 1)
# b_x = [0] * (max(b) + 1)
#
# for num in a:
#     a_x[num] += 1
# for num in b:
#     b_x[num] += 1
#
# inters = []
# for i in range(min(len(a_x), len(b_x))):
#     while a_x[i] != 0 and b_x[i] != 0:
#         inters.append(i)
#         a_x[i] -= 1
#         b_x[i] -= 1
#
# res1 = 1
# for num in inters:
#     res1 *= num
# print(res1)
#
# res2 = a + b
# for num1 in inters:
#     for num2 in res2:
#         if num1 == num2:
#             num1 = 1
#             num2 = 1
# pr = 1
# for num in res2:
#     pr *= num
# print(pr)

from tkinter import *
from tkinter.filedialog import *
import tkinter.font as tkFont
from datetime import *
import os
import datetime as dt

def newfile():
    Window.title("제목없음-메모장")
    Textbox.delete(1.0,END)

def openfile():
    file = askopenfilename(initialdir="/", title="파일열기", filetypes=(("텍스트파일","*.txt"),("모든파일","*.*")))
    Window.title(os.path.basename(file)+"-메모장")
    Textbox.delete(1.0, END)
    f=open(file,"r")
    Textbox.insert(1.0,f.read())
    f.close()

def savefile():
    f = asksaveasfile(mode="w", defaultextension=".txt")
    if f is None :
        return
    ts = str(Textbox.get(1.0, END))
    f.write(ts)
    f.close()

def exitfile():
    efile = Toplevel(Window)
    efile.title("메모장 종료")
    elab = Label(efile, text = "\n메모장을 저장하시겠습니까?\n")
    elab.pack()
    sbutton = Button(efile, text="저장", command=savefile)
    sbutton.pack()
    ebutton = Button(efile, text="종료", command=Window.destroy)
    ebutton.pack()

def memoinfo():
    m = Toplevel(Window)
    m.title("메모장 정보")
    mlabel = Label(m, text="\n메모장 버전 1.0\n 제작:하은&태훈\n", width=40, height=20)
    mlabel.config(bg="#FFDEE9")
    mlabel.pack()

def txtinfo():
    t = Toplevel(Window)
    t.title("문서 정보")
    ts = str(Textbox.get(1.0, END))
    tlist = (list(ts.split(' ')))
    tline = list(ts.split('\n'))
    tlabel = Label(t, text = """
    낱말 수 : 
    글자 수(공백포함) :
    글자 수(공백제외) :  """.format())
    tlabel.pack()

def underLine():
    under_ = tkFont.Font(underline=True, size=10)
    Textbox.configure(font=under_)

def italic():
    f_ital = tkFont.Font(slant = "italic")
    Textbox.configure(font=f_ital)

def bold():
    f_bold = tkFont.Font(weight="bold")
    Textbox.configure(font=f_bold)

def default():
    def_ = tkFont.Font(weight="normal",size=10)
    Textbox.configure(font=def_)


def time():
    Textbox.insert(INSERT, datetime.now())
def sp_1():
    Textbox.insert(INSERT, "☆")
def sp_2():
    Textbox.insert(INSERT, "★")
def sp_3():
    Textbox.insert(INSERT, "♡")
def sp_4():
    Textbox.insert(INSERT, "♥")


Window = Tk()
Window.title("Hun&Eun 메모장")
Window.geometry("500x400")

Textbox = Text(Window)
scr = Scrollbar(Textbox)
scr.config(command=Textbox.yview)
scr.pack(side=RIGHT, fill=Y)
Window.grid_rowconfigure(0, weight=1)
Window.grid_columnconfigure(0, weight=1)
Textbox.grid(sticky = N+E+S+W)

file = None

menu = Menu(Window)
fi = Menu(menu, tearoff=0)
fi.add_command(label="새파일",command=newfile)
fi.add_command(label="불러오기",command=openfile)
fi.add_command(label="저장",command=savefile)
fi.add_command(label="종료",command=exitfile)
menu.add_cascade(label="파일", menu=fi)

font = Menu(menu, tearoff=0)
font.add_command(label="밑줄",command=underLine)
font.add_command(label="기울임",command=italic)
font.add_command(label="진하게",command=bold)
font.add_command(label="기본설정",command=default)
menu.add_cascade(label="글꼴",menu=font)

info = Menu(menu, tearoff=0)
info.add_command(label="문서정보",command=txtinfo)
info.add_command(label="메모장정보",command=memoinfo)
menu.add_cascade(label="도움말", menu=info)

inp = Menu(menu, tearoff=0)
inp.add_command(label="☆",command = sp_1)
inp.add_command(label="★",command = sp_2)
inp.add_command(label="♡",command = sp_3)
inp.add_command(label="♥",command = sp_4)
inp.add_separator()
inp.add_command(label="시간",command = time)
menu.add_cascade(label='입력',menu=inp)
Window.config(menu=menu)


Window.mainloop()