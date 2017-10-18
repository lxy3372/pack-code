#!/usr/bin/env python
# -*- encoding=utf-8 -*-
import errno

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
        # icon = wx.Icon("./bitmaps/zip.ico", wx.BITMAP_TYPE_ICO)
        # self.SetIcon(icon)
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
        self.pwd = wx.TextCtrl(panel, -1, "vcfez3G0mLZoE0LCjgJG8uvNkYJI53mJ")
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

    def on_copy(self, source_dir, desc_dir, files):
        if not source_dir or not desc_dir:
            raise FileNotFound("Dir not exists: %s" % file)

        if not os.path.isdir(source_dir):
            os.mkdir(desc_dir)

        for file in files:
            source_file = os.path.join(source_dir, file)
            targe_file = os.path.join(desc_dir, file)
            targe_dir = os.path.dirname(targe_file)
            if not os.path.isfile(source_file):
                raise FileNotFound("File not found: %s" % file)
            if not os.path.exists(targe_dir):
                os.mkdir(targe_dir)
            open(targe_file, 'rb').write(open(source_file, 'rb').read())

    def on_copy(self, source_dir, desc_dir, files):
        if not source_dir or not desc_dir:
            raise FileNotFound("Dir not exists: %s" % file)
        if not os.path.isdir(source_dir):
            os.mkdir(desc_dir)

        for file in files:
            if (file.lstrip() == ''):
                continue
            source_file = os.path.join(source_dir, file.lstrip(os.sep).rstrip())
            targe_file = os.path.join(desc_dir, file.lstrip(os.sep).rstrip())
            targe_dir = os.path.dirname(targe_file)
            if not os.path.isfile(source_file):
                raise FileNotFound("File not found: %s" % file)
            if not os.path.exists(targe_dir):
                try:
                    os.makedirs(targe_dir)
                except OSError as exc:
                    if exc.errno == errno.EEXIST and os.path.isdir(targe_dir):
                        pass
                    else:
                        raise
            open(targe_file, 'wb').write(open(source_file, 'rb').read())

    def on_zip(self, event):
        try:
            system = platform.system()

            source_dir = self.dic_picker1.GetPath()
            target_dir = self.dic_picker2.GetPath()
            tmp_dir = target_dir + os.sep + '.tmp'
            files = self.dir_list.GetValue().split('\n')
            self.on_copy(source_dir, tmp_dir, files)

            if self.pwd.GetValue() is not None:
                password = ''
                if (self.pwd.GetValue()):
                    password = ' -P' + self.pwd.GetValue()
                if system == "Windows":
                    raise Exception("暂未完善")
                    # cmd = '7z u ' + password + ' ' + p.des_dir + os.sep + p.file_name
                    # si = subprocess.STARTUPINFO()
                    # si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                else:
                    cmd = 'cd ' + tmp_dir + ' && zip -r -m' + password + ' ' + target_dir + os.sep + self.file_name.GetValue() + ' * -x */.DS_Store'

                cmd_ret = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                cmd_ret.wait()
                if cmd_ret.returncode != 0:
                    raise Exception("加密失败")
        except FileNotFound as e:
            title = e.message
        except DirNotFound as e:
            title = e.message
        except PHPSyntaxError as e:
            title = e.message
        except Exception as e:
            title = e.message
        else:
            title = "打包成功"
        dlg = wx.MessageDialog(None, title, "提示", wx.YES_DEFAULT)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()
        os.rmdir(tmp_dir)


if __name__ == '__main__':
    app = wx.App()
    Application(None, title="打包")
    app.MainLoop()
