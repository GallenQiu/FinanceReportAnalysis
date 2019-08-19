# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
'''最近5年的财报财务摘要'''
import requests,json,time,pymongo,time,re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from multiprocessing import Queue
from concurrent.futures import ThreadPoolExecutor
from pymongo.collection import Collection
class Xinalang():
    def __init__(self):
        self.queue=Queue()
        self.info=[]
        self.dict_list=[]
        self.usa=UserAgent()

    def req(self,ninfo):
        # try:
            info=json.loads(ninfo)
            scode=info["SECCODE"]

            data_=info
            url0='http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/{}.phtml'.format(scode)
            url_list=[]
            url_list.extend([url0])
            # data = {}
            for url in url_list:
                headers={
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"accept-encoding":"gzip,deflate,br",
"accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
"cache-control":"max-age=0",
"upgrade-insecure-requests":"1",
"user-agent":self.usa.random,}
                response=requests.get(url,headers=headers,timeout=5)#,headers=headers
                # print(response.text)
                html_text=response.content.decode("GBK")
                html1=html_text.split("FundHoldSharesTable")[1].split("<!--财务摘要end-->")[0]
                html2=html1.split("<!--分割数据的空行begin-->")
                for h in html2:
                    li={}
                    soup=BeautifulSoup(h,"lxml")

                    for tr in soup.select("tr"):
                        try:
                            key=tr.select("td")[0].text
                            value=tr.select("td")[1].text
                            if value =="\xa0":
                                value=None
                            elif key =='截止日期':
                                value=value
                            else:
                                value = float(value.replace("元","").replace(",",""))

                            li[key]=value
                        except:
                            pass
                    if li != {}:
                        data_[li["截止日期"]]=li
                        # print(li)
                '''报表日期'''

                # data_.update(data)

            print(info["SECNAME"])
            # print(data_)
            self.dict_list.append(data_)


    def scheduler(self):

        with open("D:\python文件库\项目\Financal analysis\A股数据分析\stockCode.txt",encoding="utf8") as f:
            lines=f.readlines()
        c=-1
        for line in lines[3216:]:

            # info=json.loads(line)
            #
                # info["year"]=year
                # info_str=json.dumps(info)
                # print(json.loads(info_str))
            try:
                self.req(line)
            except:
                print("Retry!")
                self.req(line)
            self.write_json()
            time.sleep(1.5)
            # self.queue.put(line)

        # pool=ThreadPoolExecutor(max_workers=6)
        # while self.queue.qsize()>0:
        #     pool.submit(self.req, self.queue.get())
        # pool.shutdown()
        #
        # print("剩下："+str(len(self.info)))
        # while len(self.info)>0:
        #
        #     self.req(self.info.pop())

        self.write_json()

    def write_json(self):
        try:
            # 建立连接
            client = pymongo.MongoClient('localhost', 27017)
            # 建立数据库
            db = client["XinlangFinance"]

            # 从原有的txt文件导入share_id：

            # 表的对象化
            mgtable = Collection(db, 'FinanceReport_data_cwzy')

            mgtable.insert_many(self.dict_list)
            self.dict_list.pop()

        except:
            print("写入出错！！")
            pass



if __name__ == '__main__':


    start_time=time.time()

    X = Xinalang()
    X.scheduler()

    print("总耗时：{}秒".format(time.time()-start_time))


