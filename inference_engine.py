#!/usr/bin/python3
# encoding:utf-8
# -*- Mode: Python -*-
# Author: sansa <hisansas@gmail.com>

import pymysql
import numpy as np

def Cal_gift(sex, relation, character):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "", "mytestdb")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT " + sex + "," + relation + "," + character + " FROM GiftRule"

    #直接用函数选择
    #sql = "SELECT GIFTNAME, Cal_CH3(" + sex + "," + relation + "," + character + ") AS MY FROM GiftRule ORDER BY MY DESC LIMIT 3"

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

    gifts = np.array(np.zeros(len(results)))
    for i in range(len(results)):
        gifts[i] = Cal_CH3(results[i][0], results[i][1], results[i][2])

    gifts_sort = np.argsort(gifts)

    return gifts_sort[-1], gifts_sort[-2], gifts_sort[-3]

def Cal_CH2(CF1, CF2):
    """
    计算置信度
    """
    #同正
    if (CF1 >= 0.0) & (CF2 >= 0.0):
        return CF1 + CF2 - CF1 * CF2
    #同负
    if (CF1 < 0.0) & (CF2 < 0.0):
        return CF1 + CF2 + CF1 * CF2
    #异号
    if (CF1 * CF2 < 0.0):
        return (CF1 + CF2) / (1 - min(abs(CF1), abs(CF2)))

def Cal_CH3(CF1, CF2, CF3):
    CH12 = Cal_CH2(CF1, CF2)
    return Cal_CH2(CH12, CF3)