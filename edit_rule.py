#!/usr/bin/python3
# encoding:utf-8
# -*- Mode: Python -*-
# Author: sansa <hisansas@gmail.com>

import wx
import pymysql

List = ["MALE", "FEMALE", "CP", "FRIEND", "OLDMAN", "CLASSMATE", "CUTE", "ART", "PART", "TECH"]

class EditFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX |
                                                          wx.MAXIMIZE_BOX))
        self.SetSize((400, 180))
        self.SetPosition((500, 500))
        self.SetBackgroundColour('white')

        self.chooseIF= wx.Choice(self, choices=List, pos=(50, 20), size=(80, 25))
        self.text1 = wx.StaticText(self, label='IF:',pos=(20,25), size=(20, 25))
        self.text1.SetBackgroundColour('white')
        self.editTHEN = wx.TextCtrl(self, pos=(210, 20), size=(80, 25))
        self.text1 = wx.StaticText(self, label='THEN:', pos=(160, 25), size=(40, 25))
        self.text1.SetBackgroundColour('white')
        self.text1 = wx.StaticText(self, label='(', pos=(310, 25), size=(5, 25))
        self.text1.SetBackgroundColour('white')
        self.editCF = wx.TextCtrl(self, pos=(320, 20), size=(36, 25))
        self.text1 = wx.StaticText(self, label=')', pos=(362, 25), size=(5, 25))
        self.text1.SetBackgroundColour('white')
        self.createButton = wx.Button(self, label='Create', pos=(100, 90), size=(80, 30))
        self.cancelButton = wx.Button(self, label='Cancel', pos=(200, 90), size=(80, 30))
        self.cancelButton.Bind(wx.EVT_BUTTON, self.cancel_creation)

        #设置图标
        icon = wx.Icon()
        icon.LoadFile("./fig/Icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

    def cancel_creation(self, event):
        self.Close()

