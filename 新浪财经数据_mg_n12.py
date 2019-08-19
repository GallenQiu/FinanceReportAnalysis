# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
'''最近12个月的财报'''
import requests,json,time,pymongo,time
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
            # year=info["year"]
            # print(scode,year)
            data_=info
            url0='http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_BalanceSheet/stockid/{}/ctrl/part/displaytype/4.phtml'.format(scode)
            url1='http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_ProfitStatement/stockid/{}/ctrl/part/displaytype/4.phtml'.format(scode)
            url2='http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_CashFlow/stockid/{}/ctrl/part/displaytype/4.phtml'.format(scode)
            url_list=[]
            url_list.extend([url0,url1,url2])
            # data_year=[]
            data = {}
            for url in url_list:
                headers={
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"accept-encoding":"gzip,deflate,br",
"accept-language":"zh-CN,zh;q=0.9,en;q=0.8",
"cache-control":"max-age=0",
"upgrade-insecure-requests":"1",
"user-agent":self.usa.random,}
                response=requests.get(url,headers=headers)#,headers=headers
                # print(response.text)
                soup=BeautifulSoup(response.content.decode("GBK"),"lxml")

                '''报表日期'''
                trs = soup.select("tbody tr")

                for tr in trs:
                    tds=tr.select("td")
                    if tds[1:] != []:
                        # print(tds)
                        # try:
                        value_list=[]
                        # value = [td.text for td in tds[1:]]
                        for td in tds[1:]:
                            td=td.text
                            # print(td)

                            if td == "--":
                                td = 0.00

                            try:
                                value_list.append(float(td.replace(',','')))
                                # data[tds[0].text] =
                            except:
                                value_list.append(td)
                                # data[tds[0].text] = td
                        data[tds[0].text]=value_list
                        # except:
                        #     pass


                # print(data)
                # data_year.append(data)
                data_.update(data)
            # print(data_)
            # data_["data"]=data_year
            print(info["SECNAME"])
            self.dict_list.append(data_)
        # except TimeoutError:
        #     print("超时")
        #     self.info.append(ninfo)
        # except:
        #     print("其他错误")
        #     print("其他错误")
        #     info = json.loads(ninfo)
        #     print(info["SECNAME"], info["year"])

    def scheduler(self):

        with open("D:\python文件库\项目\Financal analysis\A股数据分析\stockCode.txt",encoding="utf8") as f:
            lines=f.readlines()
        c=-1
        for line in lines[2234:]:

            # info=json.loads(line)
            #
                # info["year"]=year
                # info_str=json.dumps(info)
                # print(json.loads(info_str))
            self.req(line)
            self.write_json()
            time.sleep(2)
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
            mgtable = Collection(db, 'FinanceReport_data_n12_06')

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


