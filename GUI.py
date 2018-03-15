#!/usr/bin/python3
# encoding:utf-8
# -*- Mode: Python -*-
# Author: sansa <hisansas@gmail.com>

import wx
import os
import sys
from inference_engine import *
from show_rule import *
from edit_rule import *

sys.path.append('..')

#图片位置
pic1_pos = (37, 161)
pic2_pos = (318, 161)
pic3_pos = (598, 161)
gifts_C = ["灯光音响~", "小猫摆件~", "闹钟~", "渔夫帽~", "按摩椅~", "项链~", "手账本~", "香水~", "乳胶枕头~", "茶具~", "手表~", "加湿器"]
gifts_E = ["audio", "cat", "clock", "hat", "massor", "necklace", "notebook", "perfume", "pillow", "tea", "watch", "wet"]
relation_list = ["对象", "好朋友", "长辈", "同事/同学"]
relation_list_E = ["CP", "FRIEND", "OLDMAN", "CLASSMATE"]
character_list = ["萌萌哒", "文艺小清新", "实用", "科技"]
character_list_E = ["CUTE", "ART", "PART", "TECH"]
sex_list = ["男", "女"]
sex_list_E = ["MALE", "FEMALE"]

class TPStaticText(wx.StaticText):
    """ transparent StaticText """

    def __init__(self, parent, id, label='',
                 pos=wx.DefaultPosition,
                 size=wx.DefaultSize,
                 style=0,
                 name='TPStaticText'):
        style |= wx.CLIP_CHILDREN | wx.TRANSPARENT_WINDOW
        wx.StaticText.__init__(self, parent, id, label, pos, size, style=style)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        event.Skip()
        dc = wx.GCDC(wx.PaintDC(self))
        dc.SetFont(self.GetFont())
        dc.DrawText(self.GetLabel(), 0, 0)

class MainFrame(wx.Frame):
    """
    主窗口
    """
    def __init__(self, parent, id, title, size):
        wx.Frame.__init__(self, parent, id, title,
                          style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))

        # 设置背景图片
        background_image = './fig/background.jpg'
        to_bmp_image = wx.Image(background_image, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.background_bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))

        # 设置选框
        self.choose_relation = wx.Choice(self.background_bitmap, choices=relation_list, pos=(299, 450), size=(100, 25))
        self.choose_character = wx.Choice(self.background_bitmap, choices=character_list, pos=(164, 489), size=(100, 25))
        self.choose_sex = wx.Choice(self.background_bitmap, choices=sex_list, pos=(164,450), size=(100,25))
        self.choose_character.Bind(wx.EVT_CHOICE, self.change_Hint)
        self.choose_relation.Bind(wx.EVT_CHOICE, self.change_Hint)
        self.choose_sex.Bind(wx.EVT_CHOICE, self.change_Hint)

        #设置按键
        self.showRuleButton = wx.Button(self.background_bitmap, label='查看规则~', pos=(747, 450), size=(100, 25))
        self.OKButton = wx.Button(self.background_bitmap, label='寻找礼物~', pos=(747, 489), size=(100, 25))
        self.EditButton = wx.Button(self.background_bitmap, label='添加规则~', pos=(747, 528), size=(100, 25))
        #设置控件关联函数
        self.showRuleButton.Bind(wx.EVT_BUTTON, self.showRules)
        self.OKButton.Bind(wx.EVT_BUTTON, self.getResults)
        self.EditButton.Bind(wx.EVT_BUTTON, self.EditRules)

        #设置图标
        icon = wx.Icon()
        icon.LoadFile("./fig/Icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        #设置静态文本
        self.HintLabel = wx.StaticText(self.background_bitmap, 1, label='请选择~', pos=(445, 470))
        self.HintLabel.SetBackgroundColour('white')

        #self.show_picture('../fig/wet.png', pic1_pos)

        #设置基本参数
        self.SetSize(size)
        self.Center()
        self.title = title
        self.pic_path = None
        self.engine = None
        self.contour_num = None
        self.Show()

    def show_picture(self, path, pos):
        pic = wx.Image(path, wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        bmp = wx.StaticBitmap(self, 0, pic, pos=pos)
        bmp.Show()

    def showRules(self, event):
        ruleFrame = RuleFrame(self, 1, 'All Rules')
        ruleFrame.Show()

    def EditRules(self, event):
        editFrame = EditFrame(self, 1, 'Edit Rules')
        editFrame.Show()

    def getResults(self,event):
        if ((self.choose_sex.GetSelection() >= 0) & (self.choose_relation.GetSelection() >= 0)
                & (self.choose_character.GetSelection() >= 0)):
            fig1_index, fig2_index, fig3_index = \
                Cal_gift(sex_list_E[self.choose_sex.GetSelection()], relation_list_E[self.choose_relation.GetSelection()], character_list_E[self.choose_character.GetSelection()])

            giftsToShow = "推荐给你：" + gifts_C[fig1_index] + gifts_C[fig2_index] + "和" + gifts_C[fig3_index]
            self.HintLabel.SetLabel(giftsToShow)
            self.show_picture("./fig/" + str(gifts_E[fig1_index]) + ".png", pic1_pos)
            self.show_picture("./fig/" + str(gifts_E[fig2_index]) + ".png", pic2_pos)
            self.show_picture("./fig/" + str(gifts_E[fig3_index]) + ".png", pic3_pos)
        else:
            self.HintLabel.SetLabel("请选择筛选条件~")

    def change_Hint(self,event):
        if ((self.choose_relation.GetSelection() >= 0) & (self.choose_sex.GetSelection() >= 0)):
            strToShow = "你选择将礼物送给：" + str(relation_list[self.choose_relation.GetSelection()])
            self.HintLabel.SetLabel(strToShow)
            if self.choose_character.GetSelection() >= 0:
                strToShow += "，偏向" + str(character_list[self.choose_character.GetSelection()]) + "类~"
                self.HintLabel.SetLabel(strToShow)

if __name__ == '__main__':
    app = wx.App()
    MainFrame(None, -1, title='Gifts to You_Expert System', size=(900, 625))
    app.MainLoop()