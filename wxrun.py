#!/usr/bin/env python
# -*- encoding=utf-8 -*-

__author__ = "Ricky"

import wx


class Application(wx.Frame):
    def __init__(self, parent, title):
        super(Application, self).__init__(parent, title=title, size=(400, 400))
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
        boxs = wx.FlexGridSizer(3, 2, 9, 25)

        source_title = wx.StaticText(panel, label="项目地址：")
        des_title = wx.StaticText(panel, label="打包目录：")
        list_title = wx.StaticText(panel, label="打包列表：")

        dic_picker1 = wx.DirPickerCtrl(panel, wx.ID_ANY, "请选择源文件夹")
        dic_picker2 = wx.DirPickerCtrl(panel, wx.ID_ANY, "请选择目标文件夹")
        dic_picker2.SetOwnForegroundColour('gray')
        input3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        boxs.AddMany(
            [(source_title), (dic_picker1, 1, wx.EXPAND), (des_title), (dic_picker2, 1, wx.EXPAND),  (list_title, 1, wx.EXPAND),
             (input3, 1, wx.EXPAND)])

        boxs.AddGrowableRow(2, 1)
        boxs.AddGrowableCol(1, 1)

        hbox.Add(boxs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)



if __name__ == '__main__':
    app = wx.App()
    Application(None, title="打包")
    app.MainLoop()
