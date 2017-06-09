#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import Tkinter
import tkMessageBox


class Application(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.grid()
        self.create_label(text="打包文件列表：")
        self.create_text()
        self.create_label(text="项目根目录：")
        self.create_source_dir()
        self.create_label(text="项目打包到：")
        self.create_destination_dir()
        self.create_button()

    def create_label(self, text=None):
        self.label = Tkinter.Label(self, text=text)
        self.label.grid()

    def create_text(self):
        self.code_list = Tkinter.Text(self, height=10, width=80)
        self.code_list.grid(pady=10, padx=10)

    def create_source_dir(self):
        self.soure_input = Tkinter.Entry(self)
        self.soure_input.grid()

    def create_destination_dir(self):
        self.destination = Tkinter.Entry(self)
        self.destination.grid()

    def create_button(self):
        self.submit = Tkinter.Button(self, text='提交', command=self.pack)
        self.submit.grid()

    def pack(self):
        code_str = self.code_list.get('0.0', Tkinter.END)
        source = self.soure_input.get()
        des = self.destination.get()
        tkMessageBox.showinfo(title='消息', message="%s %s %s" % (code_str, source, des))


app = Application()
app.master.wm_title("测试")
app.mainloop()
