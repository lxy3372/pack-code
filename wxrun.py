#!/usr/bin/env python
# -*- encoding=utf-8 -*-

__author__ = "Ricky"

import wx


class Application(wx.Frame):
    def __init__(self, parent, title):
        super(Application, self).__init__(parent, title=title, size=(600, 500))
        self.init_menu()
        self.init_panel()
        self.Centre()
        self.Show()

    def init_menu(self):
        menu_bar = wx.MenuBar()
        filem = wx.Menu()
        helpm = wx.Menu()
        menu_bar.Append(filem, '&File')
        menu_bar.Append(helpm, '&Help')

        self.SetMenuBar(menu_bar)

    def init_panel(self):
        panel = wx.Panel(self, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        boxs = wx.FlexGridSizer(6, 2, 9, 25)

        source_title = wx.StaticText(panel, label="项目地址：")
        des_title = wx.StaticText(panel, label="打包目录：")
        list_title = wx.StaticText(panel, label="打包列表：")
        pass_title = wx.StaticText(panel, label="加密密码:")

        self.dic_picker1 = wx.DirPickerCtrl(panel, wx.ID_ANY, wx.EmptyString)
        self.dic_picker2 = wx.DirPickerCtrl(panel, wx.ID_ANY, wx.EmptyString)
        self.dir_list = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.pwd = wx.TextCtrl(panel)


        boxs.AddMany(
            [(source_title), (self.dic_picker1, 1, wx.EXPAND), (des_title), (self.dic_picker2, 1, wx.EXPAND),  (list_title, 1, wx.EXPAND),
             (self.dir_list, 1, wx.EXPAND), (pass_title), (self.pwd, 1, wx.EXPAND)])

        boxs.AddGrowableRow(2, 1)
        boxs.AddGrowableCol(1, 1)

        hbox.Add(boxs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        self.submit = wx.Button(panel, label="打包")
        self.cancel = wx.Button(panel, label="取消")

        #self.cancel.Bind(wx.EVT_BUTTON, self.on_self.cancel)
        self.Bind(wx.EVT_BUTTON, self.on_zip, self.submit)
        self.Bind(wx.EVT_BUTTON, self.on_cancel, self.cancel)

        boxs.Add(self.submit)
        boxs.Add(self.cancel)

        panel.SetSizer(hbox)


    def on_cancel(self, event):
        self.Close()

    def on_zip(self, event):
        print self.dic_picker1.GetPath()
        print self.dic_picker2.GetPath()
        print self.dir_list.GetValue()
        print self.pwd.GetValue()
        dlg = wx.MessageDialog(None, "打包成功", "提示", wx.YES_DEFAULT)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App()
    Application(None, title="打包")
    app.MainLoop()
