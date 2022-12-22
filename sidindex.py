import pygame
import tkinter as tk
import easygui
from PIL import ImageTk
from tkinter import filedialog
import os
import re
from urllib.request import urlretrieve
from subprocess import Popen, PIPE, STDOUT
from easygui import *
import subprocess
import requests

# easygui.msgbox('欢迎使用')
window = tk.Tk()
window.geometry('500x500')
window.resizable(0,0)
window.title('红蜘蛛多媒体对抗器-作者网站:lyfbbs.freehost.ssjs.shop')
window.iconphoto(True, tk.PhotoImage(file='images/lyf.png'))
window.attributes("-topmost",999999999999999999999999999999999999999999999999999999999999)
bgImg = ImageTk.PhotoImage(file = './images/bg.png')
bg = tk.Label(window,background='#C3C3C3',width=500,height=500)
bg.pack()

text1text='阻断'
text1=tk.Label(window,text="模式:"+text1text,font = ("./font/simkai.ttf",50),background='#C3C3C3')
text1.place(x = 0,y = 0)

def suduanbtncmd():
    global text1text
    text1text='阻断'
    text1 = tk.Label(window, text="模式:" + text1text, font=("./font/simkai.ttf", 50), background='#C3C3C3')
    text1.place(x=0, y=0)

zuduanbtn = tk.Button(window,text='阻断模式',bd=1,font = ("./font/simkai.ttf",37),background='#FFC90E',command=suduanbtncmd,activebackground='#FFC90E')
zuduanbtn.place(x = 0,y = 100)
def zuduanmoshishuom():
    easygui.msgbox(msg='推荐使用，将重复执行结束红蜘蛛程序的命令，使用时不能关闭黑色窗口，可以最小化窗口，不想解除控制时请关闭黑色窗口',title='阻断说明',ok_button='明白了')
explain1=tk.Button(window,text='阻断说明',bd=1,font = ("./font/simkai.ttf",15),background='#FFC90E',activebackground='#FFC90E',command=zuduanmoshishuom)
explain1.place(x = 0,y = 185)

def deletebtncmd():
    global text1text
    text1text='删除'
    text1 = tk.Label(window, text="模式:" + text1text, font=("./font/simkai.ttf", 50), background='#C3C3C3')
    text1.place(x=0, y=0)

deletebtn = tk.Button(window,text='删除模式',bd=1,font = ("./font/simkai.ttf",37),background='red',command=deletebtncmd,activebackground='red')
deletebtn.place(x = 250,y = 100)
def deletemsgts():
    easygui.msgbox(msg='将删除红蜘蛛程序“REDAgent.exe”，和红蜘蛛安装目录，不推荐使用，开启时将会请求管理员权限，请同意。',title='删除说明',ok_button='明白了')
explain2=tk.Button(window,text='删除说明',bd=1,font = ("./font/simkai.ttf",15),background='red',activebackground='red',command=deletemsgts)
explain2.place(x = 100,y = 185)

scrhrefms='关'
def zidingyilujingdepand():
    global scrhrefms,scrhrefbtn
    if scrhrefms=='关':
        scrhrefms='开'
    else:
        scrhrefms = '关'

    scrhrefbtn = tk.Button(window, text='自定义路径：' + scrhrefms, bd=1, font=("./font/simkai.ttf", 37),background='#FFC90E', command=zidingyilujingdepand, activebackground='#FFC90E')
    scrhrefbtn.place(x=0, y=220)
    # 自定义路径的判断
scrhrefbtn = tk.Button(window,text='自定义路径：'+scrhrefms,bd=1,font = ("./font/simkai.ttf",37),background='#FFC90E',command=zidingyilujingdepand,activebackground='#FFC90E')
scrhrefbtn.place(x = 0,y = 220)
def zidingyilujinshuom():
    easygui.msgbox(msg='当选项为\"关\"时，将自动匹配红蜘蛛软件的路径；当选项为\"开\"时，需要在下方的文本框手动填写红蜘蛛软件的路径，也可以点击浏览路径选择路径。红蜘蛛默认路径为“C:\Program Files (x86)\\3000soft\Red Spider”，您填写的路径应该为红蜘蛛程序“REDAgent.exe”所在的路径，如“前面的路径\\3000soft\Red Spider”，输入的内容不应该以“\”来结尾。',title='自定义路径说明',ok_button='明白了')
    # 自定义路径说明
explain3=tk.Button(window,text='自定义路径说明',command=zidingyilujinshuom,bd=1,font = ("./font/simkai.ttf",15),background='#FFC90E',activebackground='#FFC90E')
explain3.place(x = 200,y = 185)

def benduikangqishuom():
    easygui.msgbox(msg='本对抗器为使用红蜘蛛多媒体教室的在校学生，写了个对抗程序，希望能帮到大家。作者网站：“https://lyfbbs.freehost.ssjs.shop/”，项目地址“https://lyfbbs.freehost.ssjs.shop/%E5%8F%91%E5%B8%83%E6%96%87%E7%AB%A0/essay.php?id=23”还有“https://github.com/gxlydlyf/Red-spider-blocker”。点击运行后可以运行根据选项生成好的bat文件，如果不能自动运行可以点击运行后手动运行，要运行文件的目录“'+os.getcwd()+'\cmd\\run.bat”',title='自定义路径说明',ok_button='明白了')
explain4=tk.Button(window,text='本对抗器说明',command=benduikangqishuom,bd=1,font = ("./font/simkai.ttf",15),background='#FFC90E',activebackground='#FFC90E')
explain4.place(x = 360,y = 185)

class newEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color="grey"):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color

    def foc_in(self, *args):
        if self["fg"] == self.placeholder_color:
            self.delete("0", "end")
            self["fg"] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


# entry2 = tk.Entry(window,font = ("./font/simkai.ttf",50))
# entry2.place(x = 0,y=300)

entry1 = newEntry(window,"输入红蜘蛛位置")
entry1.configure(font = ("./font/simkai.ttf",15),width=42)
entry1.place(x = 0,y=305)
entry1.foc_in()
entry1.delete("0", "end")
entry1.insert(0, 'C:\Program Files (x86)\\3000soft\Red Spider')

def liulanwenjianlujing():
    a = filedialog.askdirectory(title='选择红蜘蛛路径')
    if a != '':
        entry1.foc_in()
        entry1.delete("0", "end")
        entry1.insert(0, a)
liulanlujing=tk.Button(window,text='浏览路径',bd=1,font = ("./font/simkai.ttf",12),background='skyblue',activebackground='skyblue',command=liulanwenjianlujing)
liulanlujing.place(x = 425,y = 305)

def runbathzz():
    textdejieguo = entry1.get()
    # easygui.msgbox('你输入的路径是'+textdejieguo)
    with open('./cmd/run.bat','w+',encoding='utf8') as f:
        if text1text=='阻断':
            cmmddd = 'C:\Windows\System32\\taskkill /f /t /im "REDAgent.exe"\nC:\Windows\System32\\taskkill /f /t /im "RSpider.exe"'
            echoon1 = '@echo on'
            echoon2 = ''
            cmmddd2=''
        elif text1text=='删除':
            cmmddd = 'C:\Windows\System32\\taskkill /f /t /im "RSpider.exe"\nC:\Windows\System32\\taskkill /f /t /im "REDAgent.exe"\ndel /f /s /q REDAgent.exe'
            echoon1 = ''
            echoon2 = '@echo on'
        if scrhrefms=='关':
            cmmdddluj=''
            textdejieguo = 'C:\Program Files (x86)\\3000soft\Red Spider'
            if text1text == '删除':
                cmmddd2='''cd /d C:\Program Files\\3000soft\Red Spider
rmdir /s/q "C:\Program Files\\3000soft\Red Spider"
cd /d C:\Program Files (x86)\\3000soft\Red Spider
rmdir /s/q "C:\Program Files (x86)\\3000soft\Red Spider"
cd /d C:\Program Files(x86)\\3000soft\Red Spider
rmdir /s/q "C:\Program Files(x86)\\3000soft\Red Spider"'''
            cmmdddluj='''
C:\Windows\System32\\attrib -r "C:\Program Files\\3000soft\Red Spider"
cd /d C:\Program Files\\3000soft\Red Spider
{cmd}
C:\Windows\System32\\attrib -r "C:\Program Files (x86)\\3000soft\Red Spider"
cd /d C:\Program Files (x86)\\3000soft\Red Spider
{cmd}
C:\Windows\System32\\attrib -r "C:\Program Files(x86)\\3000soft\Red Spider"
cd /d C:\Program Files(x86)\\3000soft\Red Spider
{cmd}
            '''.format(cmd=cmmddd)
        elif scrhrefms=='开':
            if text1text == '删除':
                cmmddd2='rmdir /s/q "{luj}"'.format(luj=textdejieguo)
            cmmdddluj = 'cd /d {luj}'.format(luj=textdejieguo)
        neirong = '''
@echo off
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

if '%errorlevel%' NEQ '0' (

echo 请求管理员权限...

goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt

echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"

echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"

"%temp%\getadmin.vbs"

exit /B

:gotAdmin
echo {luj}
{echoon1}
:start

{echoon2}
C:\Windows\System32\\attrib -r "{luj}"
{cmmdddluj}
{cmmddd}
{cmmddd2}

goto start
'''.format(luj=textdejieguo,cmmddd=cmmddd,cmmdddluj=cmmdddluj,cmmddd2=cmmddd2,echoon1=echoon1,echoon2=echoon2)
        f.write(neirong)
    # print(os.getcwd()+'\cmd\\run.bat')
    # subprocess.Popen('start '+os.getcwd()+'\cmd\\run.bat')
    # os.popen('start cmd /k start .\cmd\\run.bat').read()
    os.system("start .\cmd\\run.bat")
btnrun = tk.Button(window,text='运行',font = ("./font/simkai.ttf",50),background='red',activebackground='red',width=10,command=runbathzz)
btnrun.place(x=75,y=380)
window.mainloop()