#!/usr/bin/env python
# -*- encoding=utf-8 -*-

__author__ = "Ricky"

from pack import *
import wx
import platform
import os
import subprocess


class Application(wx.Frame):
    def __init__(self, parent, title):
        super(Application, self).__init__(parent, title=title, size=(600, 500))
        self.init_menu()
        self.init_panel()
        self.Centre()
        self.Show()

    def init_menu(self):
        menu_bar = wx.MenuBar()
        icon = wx.Icon("./bitmaps/zip.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        helpm = wx.Menu()
        menu_bar.Append(helpm, '&关于')

        self.SetMenuBar(menu_bar)

    def init_panel(self):
        panel = wx.Panel(self, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        boxs = wx.FlexGridSizer(7, 2, 9, 25)

        source_title = wx.StaticText(panel, label="项目地址：")
        des_title = wx.StaticText(panel, label="打包目录：")
        list_title = wx.StaticText(panel, label="打包列表：")
        file_name_title = wx.StaticText(panel, label="打包名称：")
        pass_title = wx.StaticText(panel, label="加密密码:")

        self.dic_picker1 = wx.DirPickerCtrl(panel, wx.ID_ANY, wx.EmptyString)
        self.dic_picker2 = wx.DirPickerCtrl(panel, wx.ID_ANY, wx.EmptyString)
        self.dir_list = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.pwd = wx.TextCtrl(panel, -1, "")
        self.file_name = wx.TextCtrl(panel, -1, "pack.zip")

        boxs.AddMany(
            [(source_title), (self.dic_picker1, 1, wx.EXPAND), (des_title), (self.dic_picker2, 1, wx.EXPAND),
             (list_title, 1, wx.EXPAND),
             (self.dir_list, 1, wx.EXPAND), (file_name_title), (self.file_name, 1, wx.EXPAND), (pass_title),
             (self.pwd, 1, wx.EXPAND)])

        boxs.AddGrowableRow(2, 1)
        boxs.AddGrowableCol(1, 1)

        hbox.Add(boxs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        self.submit = wx.Button(panel, label="打包")
        self.cancel = wx.Button(panel, label="取消")

        # self.cancel.Bind(wx.EVT_BUTTON, self.on_self.cancel)
        self.Bind(wx.EVT_BUTTON, self.on_zip, self.submit)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, self.cancel)

        boxs.Add(self.submit)
        boxs.Add(self.cancel)

        panel.SetSizer(hbox)

    def on_cancel(self, event):
        self.Close()

    def on_zip(self, event):

        try:
            p = Pack()
            p.set_source_dir(self.dic_picker1.GetPath())
            p.set_des_dir(self.dic_picker2.GetPath(), self.file_name.GetValue())
            file_line = self.dir_list.GetValue().split('\n')
            p.set_pack_list(file_line)
            p.set_pwd(self.pwd.GetValue())
            p.pack()
            system = platform.system()
            ignorefile = p.des_dir + os.sep + '.zipignore'
            if self.pwd.GetValue() is not None:
                password = ''
                f = open(ignorefile, 'w')
                f.close()
                if system == "Windows":
                    if(self.pwd.GetValue()):
                        password = ' -p'+self.pwd.GetValue()
                    cmd = '7z u '+password+ ' ' + p.des_dir + os.sep + p.file_name + ' ' + ignorefile
                else:
                    if(self.pwd.GetValue()):
                        password = ' -P'+self.pwd.GetValue()
                    cmd = 'zip -u '+password+ ' ' + p.des_dir + os.sep + p.file_name + ' ' + ignorefile

                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                cmd_ret = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                cmd_ret.wait()
                if cmd_ret.returncode != 0:
                    raise Exception("加密失败")
                    # else:
                    # cmd1 = u'7z d -p'+self.pwd.GetValue()+' '+p.des_dir+os.sep+p.file_name+u' .zipignore'
                    # cmd1_ret = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    # cmd1_ret.wait()
        except FileNotFound as e:
            title = e.message
        except DirNotFound as e:
            title = e.message
        except PHPSyntaxError as e:
            title = e.message
        except Exception as e:
            title = "打包失败"
        else:
            title = "打包成功"
        dlg = wx.MessageDialog(None, title, "提示", wx.YES_DEFAULT)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()


if __name__ == '__main__':
    app = wx.App()
    Application(None, title="打包")
    app.MainLoop()
