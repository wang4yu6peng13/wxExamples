#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

class Example(wx.Frame):
    def __init__(self, title):
        super(Example, self).__init__(None, title=title,
            size=(250, 150))

        # 绑定渲染窗口的动作到OnPaint
        # 这样当resize窗口，会重新调用该函数
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Centre()
        self.Show()

    # 画一条线，参数为起始点的x,y，终点的x,y
    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        #dc.DrawLine(50, 60, 190, 60)
        dc.DrawLines(((20, 60), (100, 60), (100, 10),(20, 10), (20,60)))

if __name__ == '__main__':
    app = wx.App()
    Example('Line')
    app.MainLoop()