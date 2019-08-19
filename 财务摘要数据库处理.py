# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
import pymongo
from locale import *
# locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
from pymongo.collection import Collection

def getData():
    # 建立连接
    client = pymongo.MongoClient('localhost', 27017)
    # 建立数据库
    db = client["XinlangFinance"]

    # 从原有的txt文件导入share_id：

    # 表的对象化
    mgtable = Collection(db, 'FinanceReport_data_cwzy')
    # print({"SECCODE":str(scode),"year":year})
    data=mgtable.find({},{"_id": 0,"SECNAME" : 1,
    "SECCODE" : 1,
    "f_kind" : 1,
    "s_kind" : 1,
    "t_kind" : 1,
    "2019-06-30":1,
    "2019-03-31": 1,
    "2018-12-31": 1,
    "2018-09-30": 1,
    "2018-06-30":1,

    "2018-03-31":1,
    "2017-12-31":

                          })
    # print(data[0])
    return data

if __name__ == '__main__':
    gd=getData()
    for g in gd:
        print(g)