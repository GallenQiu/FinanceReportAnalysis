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
    mgtable = Collection(db, 'FinanceReport_data')
    # print({"SECCODE":str(scode),"year":year})
    data=mgtable.find({},{"_id": 0})
    # print(data[0])
    return data

if __name__ == '__main__':
    gd=getData()
    ol=[]
    for d in gd:
        for n in d:
            try:
                if n == "SECCODE":
                    pass
                else:
                    d[n]=float(d[n].replace(",",""))
            except:

                pass
        # print(d)
        ol.append(d)

    try:
        # 建立连接
        client = pymongo.MongoClient('localhost', 27017)
        # 建立数据库
        db = client["XinlangFinance"]

        # 从原有的txt文件导入share_id：

        # 表的对象化
        mgtable = Collection(db, 'FinanceReport_data2')

        mgtable.insert_many(ol)

    except:
        print("写入出错！！")
        pass
    # print(gd)
