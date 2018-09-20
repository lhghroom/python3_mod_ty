#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
import os.path

import chardet

mtyErrString=''  #供其它模块读取的包含此模块中各函数中记录的错误信息的全局变量

#print(dir(tkinter.messagebox)) #查看这个模块提供了哪些方法
def msgboxGhlh(info,titletext='孤荷凌寒的对话框QQ578652607',style=0,isShowErrMsg=False):
    '''
    模仿vb的msgbox，参数顺序都基本一致
    #style的值如下：
    #0 只有一个ok按钮的提示框，有蓝背景圆圈，白色i号图标
    #1 有ok按钮和cancel按钮，有问号图标（确定，取消）
    #3 有显示yes、no、cancel按钮，有问号图标
    #4 显示yes和no按钮，有问号图标显示是和否按钮。
    #5 显示retry和cancel按钮，有黄色背景三角形，黑色感叹号，重试和取消按钮
    #16 显示错误信息，有错误的图标
    #48 显示警告信息，有黄色背景三角形，黑色感叹号
    #50 显示包含一个【是】按钮和【否】按钮的对话框，有一个问号图标，但【是】返回字符串对象'yes',【否】返回字符串对象'no'
    '''
    global mtyErrString #只有这样才能在函数内使用外部的全局变量
    mtyErrString='' #每个函数使用前先清空之前的错误信息，以存储本函数可能出现的错误信息
    try:

        if style==0: #只有一个ok按钮的提示框，显示一般信息,单独一个确定按钮返回字符串对象 'ok'
            return tkinter.messagebox.showinfo(title =titletext, message = info)
        elif style==1: #有ok(确定)按钮和cancel按钮,确定按钮和取消按钮放在一起，确定按钮返回布尔值True，取消按钮返回布尔值False
            return tkinter.messagebox.askokcancel(title=titletext,message = info)
        elif style==3: #有显示yes、no、cancel按钮,是/否/取消在一起时，取消返回的是None对象，类型为：NoneType
            return tkinter.messagebox.askyesnocancel(title=titletext,message = info)
        elif style==4: #显示yes和no按钮，也就是显示是和否按钮。yes返回True no返回False
            return tkinter.messagebox.askyesno(title=titletext,message = info) 
        elif style==5: #显示retry和cancel按钮，也就是重试和取消按钮,重试和取消按钮放在一起，重试返回布尔值True,取消返回布尔值False
            return tkinter.messagebox.askretrycancel(title=titletext,message = info)
        elif style==16: #显示错误信息,单独一个确定按钮返回字符串对象 'ok'
            return tkinter.messagebox.showerror(title=titletext,message = info)
        elif style==48: #显示警告信息,单独一个确定按钮返回字符串对象 'ok'
            return tkinter.messagebox.showwarning(title=titletext,message = info)
        elif style==50: #显示包含一个【是】按钮和【否】按钮的对话框，有一个问号图标，但【是】返回字符串对象'yes',【否】返回字符串对象'no'
            return tkinter.messagebox.askquestion(title=titletext,message = info)
        else :#只有一个ok按钮的提示框，显示一般信息,单独一个确定按钮返回字符串对象 'ok'
            return tkinter.messagebox.showinfo(title =titletext, message = info)

    except Exception as e:
        mtyErrString='弹出对话框都出错了:' + str(e) + '\n此函数由【孤荷凌寒】创建,QQ578652607'
        if isShowErrMsg==True:
            return tkinter.messagebox.showerror(title=titletext,message = mtyErrString)
        else:
            return False
    else:
        pass
    finally:
        pass
 
#--取文件的后缀名部分
def getFilehzGhlh(strpath,isIncPoint=False,isShowMsg=False):
    '''
    获取一个文件（可以是完整路径，也可以是一个绝对文件名）的后缀名
    isIncPoint如果是True，则会返回.xxx形式的后缀，如果为False，则会返回xxx形式的后缀
    '''
    global mtyErrString #只有这样才能在函数内使用外部的全局变量
    mtyErrString='' #每个函数使用前先清空之前的错误信息，以存储本函数可能出现的错误信息
    try:
        strls=os.path.splitext(strpath)[1]
        if isIncPoint==True:
            return strls
        else:
            ar=strls.split('.')
            return ar[1]
    except Exception as e:
        mtyErrString='获取指定文件的后缀名出错了:' + str(e) + '\n此函数由(孤荷凌寒】创建Q578652607'
        if isShowMsg==True:
            msgboxGhlh(mtyErrString,"出现错误",16 )
        
        return ''
    else:
        pass
    finally:
        pass
