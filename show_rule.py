#!/usr/bin/python3
# encoding:utf-8
# -*- Mode: Python -*-
# Author: sansa <hisansas@gmail.com>

import wx
import pymysql

List = ["MALE", "FEMALE", "CP", "FRIEND", "OLDMAN", "CLASSMATE", "CUTE", "ART", "PART", "TECH"]

class RuleFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, style=wx.DEFAULT_FRAME_STYLE ^ (wx.RESIZE_BORDER | wx.MINIMIZE_BOX |
                                                          wx.MAXIMIZE_BOX))
        self.SetSize((450, 600))
        self.SetPosition((200, 100))
        self.ruleText = wx.TextCtrl(self, pos=(5, 5), size=(450, 600), style=wx.TE_MULTILINE | wx.TE_READONLY)

        #设置图标
        icon = wx.Icon()
        icon.LoadFile("./fig/Icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "", "mytestdb")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM GiftRule"

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            # 打印结果
            #print(results)
            # return gifts_sort[-1], gifts_sort[-2], gifts_sort[-3]

        except:
            print("Error: unable to fetch data")

        # 关闭数据库连接
        db.close()

        text = "ALL RULES:\n"
        text1 = "\nBig confidence level\n"
        text2 = "\nSmall confidence level\n"
        j = 0
        for input in List:
            j += 1
            for i in range(len(results)):
                if results[i][j] >= 0.5:
                    text1 += "IF:[" + input + "] THEN [" + results[i][0] + "] (" + str(results[i][j]) + ")\n"
                elif (results[i][j] < 0.5) & (results[i][j] > 0):
                    text2 += "IF:[" + input + "] THEN [" + results[i][0] + "] (" + str(results[i][j]) + ")\n"
        text += text1 + text2
        self.ruleText.WriteText(text)
