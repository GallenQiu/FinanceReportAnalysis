# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
from regionRp import Report_dealer
import numpy as np


class Report_index:
    def __init__(self,scode):
        # self.scode = input("输入股票代码：")
        self.scode =scode
        # self.year = input("输入年份：")
        # if self.year=="last":
        #     self.info=self.getData(self.scode ,self.year )
        # else:
        #     self.info=self.getData(self.scode ,self.year )
        #     self.info0 =self.getData(self.scode, int(self.year) - 1)
        self.getData()
        '''指数数据如下'''
        self.five_index ={}
        self.cash_flow_dict={}
        self.alr_dict_list={}

    def getData(self):
        Rd = Report_dealer(self.scode)
        self.info = Rd.scheduler()

    def getData_cwzy(self):
        import pymongo
        from pymongo.collection import Collection
        # 建立连接
        client = pymongo.MongoClient('localhost', 27017)
        # 建立数据库
        db = client["XinlangFinance"]

        # 表的对象化
        mgtable = Collection(db, 'FinanceReport_data_cwzy')
        # print({"SECCODE":str(scode),"year":year})
        data = mgtable.find({"SECCODE":self.scode}, {"_id": 0})
        # print(data[0])
        return data


    # 资产负债比率(重要科目)
    def asset_liability_ratio(self):
        alr_dict_list=[]
        info=self.info[0]

        '''资产部分'''
        alr_dict0={}
        # 比率(占总资产%)
        cap = np.array(info["资产总计"])#资产总计
        # 现金与约当现金(%)
        alr_dict0["现金与约当现金(%)"]= np.array(info["货币资金"])/cap
        # 应收款项( %)
        alr_dict0["应收款项( %)"] = np.array(info["应收票据及应收账款"])/cap
        # 存货( %)
        alr_dict0["存货( %)"] = np.array(info["存货"])/cap
        # 其他流动资产(%)
        alr_dict0["其他流动资产(%)"] = np.array(info["其他流动资产"])/cap
        # 流动资产( %)
        alr_dict0["流动资产( %)"] = np.array(info["流动资产合计"])/cap
        #商誉(%)
        alr_dict0["商誉(%)"] = np.array(info["商誉"])/ cap
        #非流动资产
        alr_dict0["非流动资产%)"] = np.array(info["非流动资产合计"])/ cap

        '''负债部分'''
        alr_dict_1 = {}
        #应付账款（%）
        alr_dict_1["应付账款（%）"]=np.array(info["应付票据及应付账款"])/cap
        # 流动负债（%）
        alr_dict_1["流动负债（%）"] = np.array(info["流动负债合计"]) / cap
        # 非流动资产（%）
        alr_dict_1["非流动资产（%）"] = np.array(info["非流动负债合计"]) / cap

        '''权益部分'''
        alr_dict_2 = {}
        #股东权益（%）
        alr_dict_2["股东权益（%）"]=np.array(info["所有者权益(或股东权益)合计"]) / cap

        # alr_dict_list.append(alr_dict)
        # alr_dict_list.append(alr_dict_1)
        # alr_dict_list.append(alr_dict_2)
        # for o in alr_dict_list:
        #     print(o)
        alr_dict={}
        alr_dict["资产部分"]=alr_dict0
        alr_dict["负债部分"] =alr_dict_1
        alr_dict["权益部分"] =alr_dict_2
        self.alr_dict_list=alr_dict

    #现金流量表
    def cash_flow_st(self):
        info=self.info[2]
        cash_flow_dict={}
        #期初现金
        cash_flow_dict["期初现金"]=np.array(info["现金的期初余额"])
        #+ 营业活动现金流量 (from 损益表)
        cash_flow_dict["+ 营业活动现金流量 (from 损益表)"] =np.array(info["经营活动产生的现金流量净额"])
        #+ 投资活动现金流量 (from 资产负债表左)
        cash_flow_dict["+ 投资活动现金流量 (from 资产负债表左)"] =np.array(info["投资活动产生的现金流量净额"])#投资活动产生的现金流量净额
        #+ 融资活动现金流量 (from 资产负债表右)
        cash_flow_dict["+ 融资活动现金流量 (from 资产负债表右)"] =np.array(info["筹资活动产生的现金流量净额"])#筹资活动产生的现金流量净额
        #期末现金
        cash_flow_dict["期末现金"] = np.array(info["六、期末现金及现金等价物余额"])
        #自由现金流（FCF）=经营活动产生的现金流量净额-购建固定资产、无形资产和其他长期资产支付的现金
        cash_flow_dict["自由现金流（FCF）"] = np.array(info["经营活动产生的现金流量净额"])-np.array(info["购建固定资产、无形资产和其他长期资产所支付的现金"])
        # print(np.array(info["经营活动产生的现金流量净额"]))
        # print(np.array(["购建固定资产、无形资产和其他长期资产所支付的现金"]))
        # print(cash_flow_dict)
        self.cash_flow_dict=cash_flow_dict


    # #五大财务比率（+成长能力）
    def five_ratio(self):
        all_dict = {}
        info=self.info

        '''财务结构'''
        dict0 = {}

        dict0["资产负债率(%)"] = np.array(info[0]["负债合计"][:-1]) / np.array(info[0]["资产总计"][:-1])
        dict0["权益乘数"] = np.array(info[0]["资产总计"][:-1]) / np.array(info[0]["所有者权益(或股东权益)合计"][:-1])
        dict0["长期资金占重资产比率(%)"] = (np.array(info[0]["所有者权益(或股东权益)合计"][:-1]) + np.array(info[0]["非流动负债合计"][:-1])) / (np.array(info[0]["在建工程"][:-1]) + np.array(info[0]["固定资产净额"][:-1]) + np.array(info[0]["工程物资"][:-1]))  # 长期资金占重资产比率(Longterm Ratio) = (股东权益+长期负债)(Total Equity + Non Current Liability) / (固定资产 + 工程物资 + 在建工程)(Fixed Assets + Construction Materials +Construction In Progress)

        '''偿债能力'''
        dict1 = {}
        dict1["流动比率(%)"] = np.array(info[0]["流动资产合计"][:-1]) / np.array(info[0]["流动负债合计"][:-1])  # 流动比率(Current Ratio) = 流动资产总额(Total Assets) / 流动负债总额(Current Liabilities)
        dict1["速动比率(%)"] =( np.array(info[0]["货币资金"][:-1])+np.array(info[0]["应收票据及应收账款"][:-1])+np.array(info[0]["其他应收款"][:-1])+np.array(info[0]["交易性金融资产"][:-1]) )/ np.array(info[0]["流动负债合计"][:-1])

        '''缺利息费用，暂时用财务费用'''
        dict1["利息保障倍数"] = (np.array(info[1]["四、利润总额"][:-1]) - np.array(info[1]["财务费用"][:-1])) / np.array(info[1]["财务费用"][:-1])  # 利息保障倍数(Interest Coverage) = 息税前利润(EBITDA) / 利息费用(Interest Expense)

        '''运营能力'''
        dict2 = {}
        #平均应收账款
        avg_rvb=((  np.array(info[0]["应收账款"][1:])+np.array(info[0]["应收票据"][1:]) + np.array(info[0]["应收账款"][:-1])+ np.array(info[0]["应收票据"][:-1])   ) / 2)
        avg_rvb[0]=(info[-1]["应收账款"][0]+info[-1]["应收账款"][-1]+info[-1]["应收票据"][0]+info[-1]["应收票据"][-1])/2
        dict2["应收款项周转率(次/年)"] = np.array(info[1]["营业收入"][:-1]) /avg_rvb# 应收款项周转率(次/年) = 营业收入/平均应收账款
        # print(np.array(info[0]["应收票据及应收账款"][1:]) + np.array(info[0]["应收票据及应收账款"][:-1]))
        dict2["应收款项周转天数(天)"] = 365 / dict2["应收款项周转率(次/年)"]

        avg_inv = ((np.array(info[0]["存货"][1:])+ np.array(info[0]["存货"][:-1])) / 2)
        avg_inv[0] = (info[-1]["存货"][0] + info[-1]["存货"][-1] ) / 2
        dict2["存货周转率(次/年)"] = np.array(info[1]["营业成本"][:-1]) / avg_inv  # 营业成本/平均存货
        dict2["存货周转天数(天)"] = 365 / dict2["存货周转率(次/年)"]

        avg_fa = ((np.array(info[0]["固定资产净额"][1:]) + np.array(info[0]["固定资产净额"][:-1])) / 2)
        avg_fa[0] = (info[-1]["固定资产净额"][0] + info[-1]["固定资产净额"][-1]) / 2
        dict2["固定资产周转率(次/年)"] = np.array(info[1]["营业收入"][:-1]) / avg_fa
        # dict2["完整生意周期(天)"] =
        # 销售成本÷平均应付账款

        avg_pbl = ((np.array(info[0]["应付账款"][1:]) + np.array(info[0]["应付票据"][1:]) + np.array(info[0]["应付账款"][:-1]) + np.array(info[0]["应付票据"][:-1])) / 2)
        avg_pbl[0] = (info[-1]["应付账款"][0] + info[-1]["应付账款"][-1] + info[-1]["应付票据"][0] + info[-1]["应付票据"][-1]) / 2
        dict2["应付款项周转天数(天)"] = avg_pbl*365/np.array(info[1]["营业成本"][:-1])

        avg_ta = ((np.array(info[0]["资产总计"][1:]) + np.array(info[0]["资产总计"][:-1])) / 2)
        avg_ta[0] = (info[-1]["资产总计"][0] + info[-1]["资产总计"][-1]) / 2
        dict2["总资产周转率(次/年)"] = np.array(info[1]["营业收入"][:-1]) / avg_ta

        '''盈利能力'''
        dict3 = {}

        dict3["ROA=资产收益率(%)"] = np.array(info[1]["五、净利润"][:-1]) / avg_ta
        # dict3["ROE=净资产收益率(%)"] = np.array(info[1]["五、净利润"][:-1]) / (
        #             (np.array(info[0]["所有者权益(或股东权益)合计"][1:]) + np.array(info[0]["所有者权益(或股东权益)合计"][:-1])) / 2)

        dict3["毛利率(%)"] = (np.array(info[1]["营业收入"][:-1]) - np.array(info[1]["营业成本"][:-1])) / np.array(info[1]["营业收入"][:-1])
        dict3["营业利润率(%)"] = np.array(info[1]["三、营业利润"][:-1]) / np.array(info[1]["营业收入"][:-1])
        dict3["净利率(%)"] = np.array(info[1]["五、净利润"][:-1]) / np.array(info[1]["营业收入"][:-1])
        dict3["营业费用率(%)"] = (np.array(info[1]["销售费用"][:1]) + np.array(info[1]["财务费用"][:-1]) + np.array(info[1]["管理费用"][:-1]) )/ np.array(info[1]["营业收入"][:-1])
        dict3["经营安全边际率(%)"] = dict3["营业利润率(%)"]/ dict3["毛利率(%)"]
        dict3["EPS=基本每股收益(元)"] =np.array(info[1]["基本每股收益(元/股)"][:-1])

        '''成长能力'''
        dict4 = {}
        cwzy_info=self.getData_cwzy()[0]
        main_income=(cwzy_info[info[0]["报表日期"][0]]["主营业务收入"]-cwzy_info[info[0]["报表日期"][0].replace("2019","2018")]["主营业务收入"])/cwzy_info[info[0]["报表日期"][0].replace("2019","2018")]["主营业务收入"]
        main_2018=(cwzy_info["2018-12-31"]["主营业务收入"]-cwzy_info["2017-12-31"]["主营业务收入"])/cwzy_info["2017-12-31"]["主营业务收入"]
        main_2017=(cwzy_info["2017-12-31"]["主营业务收入"]-cwzy_info["2016-12-31"]["主营业务收入"])/cwzy_info["2016-12-31"]["主营业务收入"]
        main_2016=(cwzy_info["2016-12-31"]["主营业务收入"]-cwzy_info["2015-12-31"]["主营业务收入"])/cwzy_info["2015-12-31"]["主营业务收入"]
        main_2015=(cwzy_info["2015-12-31"]["主营业务收入"]-cwzy_info["2014-12-31"]["主营业务收入"])/cwzy_info["2014-12-31"]["主营业务收入"]
        main_r=np.array([main_income,main_2018,main_2017,main_2016,main_2015])
        # print(cwzy_info[info[0]["报表日期"][-1]]["主营业务收入"],info[0]["报表日期"])
        dict4["营收增长率(%)"] = main_r

        profit=(np.array(info[1]["三、营业利润"][:-1]) - np.array(info[1]["三、营业利润"][1:])) / np.array(info[1]["三、营业利润"][1:])
        profit[0]=(self.info[3]["三、营业利润"][0] - self.info[3]["三、营业利润"][-1]) / self.info[3]["三、营业利润"][-1]
        dict4["营业利润增长率(%)"] =profit
        # print(dict4["营业利润增长率(%)"])

        nzb=(np.array(info[0]["所有者权益(或股东权益)合计"][:-1]) - np.array(info[0]["所有者权益(或股东权益)合计"][1:])) / np.array(info[0]["所有者权益(或股东权益)合计"][1:])
        nzb[0]=(self.info[3]["所有者权益(或股东权益)合计"][0] - self.info[3]["所有者权益(或股东权益)合计"][-1]) / self.info[3]["所有者权益(或股东权益)合计"][-1]
        dict4["净资产增长率(%)"] = nzb
        '''现金流量'''
        dict5 = {}

        dict5["现金流量比率(%)"] = np.array(info[2]["经营活动产生的现金流量净额"][:-1]) / np.array(info[0]["流动负债合计"][:-1])
        # dict5["现金流量允当比率(%)"] =
        # dict5["现金再投资比率(%)"] =
        avg_na = ((np.array(info[0]["所有者权益(或股东权益)合计"][1:]) + np.array(info[0]["所有者权益(或股东权益)合计"][:-1])) / 2)
        avg_na[0] = (info[-1]["所有者权益(或股东权益)合计"][0] + info[-1]["所有者权益(或股东权益)合计"][-1]) / 2
        dict3["ROE=净资产收益率(%)"] = dict3["净利率(%)"]*dict2["总资产周转率(次/年)"]*(1/(1-dict0["资产负债率(%)"]))
        dict3["ROE=净资产收益率(%)2"] = np.array(info[1]["五、净利润"][:-1])/avg_na

        all_dict["财务结构"] = dict0
        all_dict["偿债能力"] = dict1
        all_dict["运营能力"] = dict2
        all_dict["盈利能力"] = dict3
        all_dict["成长能力"] = dict4
        all_dict["现金流量"] = dict5
        # all_dict.extend([dict0,dict1,dict2,dict3,dict4,dict5])
        # for i in all_dict:
        #     print(i)
        self.five_index=all_dict

    def scheduler(self):
        self.asset_liability_ratio()
        self.cash_flow_st()
        self.five_ratio()
        return self.five_index ,self.cash_flow_dict,self.alr_dict_list
'''
        五类财务比率:
            data={  '财务结构': {...},
                    '偿债能力': {...},
                    '运营能力': {...},
                    '盈利能力': {...},
                    '成长能力': {...},
                    '现金流量': {...},
        }
        现金流量：
            Ri.scheduler()[1]={ '期初现金':array(...),
                                '+ 营业活动现金流量 (from 损益表)':array(...),
                                '+ 投资活动现金流量 (from 资产负债表左)':array(...),
                                '+ 融资活动现金流量 (from 资产负债表右)':array(...),}
        资产负债百分比：            
            Ri.scheduler()[2]={ '资产部分':{...},
                                '负债部分': {...},
                                '权益部分': {...} }
        '''


if __name__ == '__main__':
    Rp=Report_index("600519")
    print(Rp.scheduler())
