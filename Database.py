#!/usr/bin/python3
# encoding:utf-8
# -*- Mode: Python -*-
# Author: sansa <hisansas@gmail.com>

# !/usr/bin/python3

#写入数据库（第一次运行一次就可以）

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "", "mytestdb")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS GiftRule")

# 使用预处理语句创建表
sql = """CREATE TABLE GiftRule (
         GIFTNAME char(20) PRIMARY KEY,
         MALE FLOAT,
         FEMALE FLOAT,
         CP FLOAT,  
         FRIEND FLOAT,
         OLDMAN FLOAT,
         CLASSMATE FLOAT,
         CUTE FLOAT,
         ART FLOAT,
         PART FLOAT,
         TECH FLOAT)"""

cursor.execute(sql)

# SQL 插入语句
sql = """INSERT INTO GiftRule(GIFTNAME, MALE, FEMALE, CP, FRIEND, OLDMAN, CLASSMATE, CUTE, ART, PART, TECH)
         VALUES ('audio', 0.3, 0.6, 0.6, 0.6, 0.1, 0.7, 0.6, 0.3, 0.4, 0.6),
                ('cat', 0.1, 0.9, 0.3, 0.5, 0.1, 0.5, 0.9, 0.4, 0.2, -1.0),
                ('hat', -1.0, 0.7, 0.5, 0.5, -0.5, 0.3, 0.5, 0.5, 0.4, -1.0),
                ('massor', 0.5, 0.5, 0.2, 0.2, 1.0, 0.2, 0.1, 0.1, 0.6, 0.4),
                ('necklace', 0.2, 0.6, 0.7, 0.5, -1.0, 0.5, 0.2, 0.7, 0.6, -0.5),
                ('notebook', 0.5, 0.5, 0.3, 0.7, 0.1, 0.8, 0.5, 0.9, 0.8, -0.5),
                ('perfume', 0.3, 0.6, 0.9, 0.7, -1.0, 0.45, 0.1, 0.4, 0.5, -0.5),
                ('pillow', 0.5, 0.5, 0.3, 0.5, 0.8, 0.4, 0.2, 0.1, 0.9, 0.2),
                ('tea', 0.5, 0.5, 0.2, 0.4, 0.9, 0.3, 0.1, 0.3, 0.8, -0.5),
                ('watch', 0.9, -1.0, 0.8, 0.7, 0.3, 0.6, 0.1, 0.5, 0.8, 0.4),
                ('wet', 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.8, 0.6, 0.9, 0.3),
                ('clock', 0.6, 0.5, 0.4, 0.5, 0.1, 0.6, 0.2, 0.2, 0.8, 0.6)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

sql = """
CREATE FUNCTION cal_h2(cf1 FLOAT, cf2 FLOAT)
  RETURNS FLOAT
BEGIN
  IF cf1 >= 0 and cf2 >=0 THEN
    set @mycf = CF1 + CF2 - CF1 * CF2;
  END IF;
  IF cf1 < 0 and cf2 <0 THEN
    set @mycf = CF1 + CF2 + CF1 * CF2;
  END IF;
  IF cf1*cf2<0 THEN
    IF abs(cf1)<abs(cf2) THEN
      set @mymy = abs(cf1);
    ELSE SET @mymy = abs(cf2);
    END IF;
    set @mycf = (CF1 + CF2) / (1 - @mymy);
  END IF;
  RETURN (SELECT @mycf);
END;

CREATE FUNCTION Cal_CH3(CF1 FLOAT, CF2 FLOAT, CF3 FLOAT)
  RETURNS FLOAT
BEGIN
  set @myvalue = cal_h2(CF1,CF2);
  RETURN cal_h2(@myvalue,CF3);
END;"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

# 关闭数据库连接
db.close()