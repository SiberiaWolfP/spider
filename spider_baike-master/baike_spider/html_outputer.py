#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import sqlite3

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output(self):
        for data in self.datas:
            conn = sqlite3.connect("C:\Users\ASUS\Desktop\web\db.sqlite3")

            sql = "insert into webmain_baike(url,name,text)values('%s','%s','%s')" % (data['url'],data['title'],data['summary'])
            conn.execute(sql)
            conn.commit()
            conn.close()