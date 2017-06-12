#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import Tkinter
import tkMessageBox
import tkFileDialog


class Application(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)

    def build(self):
        self.source_path = Tkinter.StringVar()
        self.des_path = Tkinter.StringVar()
        self.create_source_row()
        self.create_des_row()
        self.grid()

    def create_source_row(self):
        self.source_row = Tkinter.Label(text="项目地址:").grid(row=0, column=0)
        self.source_input = Tkinter.Entry(self, textvariable=self.source_path).grid(row=0, column=1)
        self.source_btn = Tkinter.Button(self, text="路径选择", command=self.build_source_path()).grid(row=0, column=2)

    def create_des_row(self):
        self.des_row = Tkinter.Label(text=" 目标地址:").grid(row=1, column=0)
        self.des_input = Tkinter.Entry(self, textvariable=self.des_path).grid(row=1, column=1)
        self.des_btn = Tkinter.Button(self, text="路径选择", command=self.build_des_path()).grid(row=1, column=2)

    def build_source_path(self):
        self.build_select_path(self.source_path)

    def build_des_path(self):
        self.build_select_path(self.des_path)

    def build_select_path(self, path):
        path_str = tkFileDialog.askdirectory()
        path.set(path_str)



    def pack(self):
        code_str = self.code_list.get('0.0', Tkinter.END)
        source = self.soure_input.get()
        des = self.destination.get()
        tkMessageBox.showinfo(title='消息', message="%s %s %s" % (code_str, source, des))


app = Application()
app.master.wm_title("测试")
app.master.geometry("600x400")
app.build()
app.mainloop()
