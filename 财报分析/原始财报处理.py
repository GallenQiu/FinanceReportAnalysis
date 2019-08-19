# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
import pymongo

from pymongo.collection import Collection

class Report_dealer:
    def __init__(self):
        self.scode = input("输入股票代码：")
        self.year = input("输入年份：")
        if self.year=="last":
            self.info=self.getData(self.scode ,self.year )
        else:
            self.info=self.getData(self.scode ,self.year )
            self.info0 =self.getData(self.scode, int(self.year) - 1)

    def getData(self,scode,year):
        # 建立连接
        client = pymongo.MongoClient('localhost', 27017)
        # 建立数据库
        db = client["XinlangFinance"]

        # 从原有的txt文件导入share_id：

        # 表的对象化
        mgtable = Collection(db, 'FinanceReport_data2')
        print({"SECCODE":str(scode),"year":year})
        data=mgtable.find({"SECCODE":str(scode),"year":int(year)})
        # print(data[0])
        return data[0]

    #资产负债比率(重要科目)
    def asset_liability_ratio(self):
        alr_dict_list=[]

        cash=self.info["货币资金"]#货币资金
        if self.info['应收票据及应收账款'] == 0:
            receivable=(self.info["应收账款"])+(self.info["应收票据"])#应收账款+应收票据
        else:
            receivable = self.info["应收票据及应收账款"]
        # print(receivable)
        inventory=self.info["存货"]#存货
        # print(inventory)

        otherFA=(self.info["其他流动资产"])#其他流动资产
        FA=self.info["流动资产合计"]#流动资产合计
        goodwill=self.info["商誉"]#商誉
        NFA=self.info["非流动资产合计"]#非流动资产合计

        if self.info['应付票据及应付账款'] == 0:
            payable = float(self.info["应付账款"]) + float(self.info["应付票据"])  # 应收账款+应收票据
        else:
            payable = float(self.info["应付票据及应付账款"])

        FD=float(self.info["流动负债合计"])#流动负债合计
        NFD=self.info["非流动负债合计"]#非流动负债合计
        equity=self.info["所有者权益(或股东权益)合计"]#所有者权益（或股东权益）合计

        '''资产'''
        alr_dict={"kind":"资产"}
        #比率(占总资产%)
        Cap=self.info["资产总计"]#资产总计
        #现金与约当现金(%)
        cashCap=round(cash/Cap*100,1)
        alr_dict["现金与约当现金(%)"]=cashCap

        #应收款项( %)
        receivableCap=round(receivable/Cap*100,1)
        alr_dict["应收款项( %)"] = receivableCap
        #存货( %)
        inventoryCap=round(inventory/Cap*100,1)
        alr_dict["存货( %)"] = inventoryCap
        #其他流动资产(%)
        otherFACap=round(otherFA/Cap*100,1)
        alr_dict["其他流动资产(%)"] = otherFACap
        #流动资产( %)
        FACap=round(FA/Cap*100,1)
        alr_dict["流动资产( %)"] = FACap
        #商誉(%)
        goodwillCap = round(goodwill/ Cap * 100, 1)
        alr_dict["商誉(%)"] = goodwillCap
        #非流动资产
        NFACap=round(NFA/ Cap * 100, 1)
        alr_dict["非流动资产%)"] = NFACap
        '''负债'''
        alr_dict_1 = {"kind": "负债"}
        #应付账款（%）
        payableCap=round(payable/Cap * 100, 1)
        alr_dict_1["应付账款（%）"]=payableCap
        # 流动负债（%）
        FDCap = round(FD / Cap * 100, 1)
        alr_dict_1["流动负债（%）"] = FDCap
        # 非流动资产（%）
        NFDCap = round(NFD / Cap * 100, 1)
        alr_dict_1["非流动资产（%）"] = NFDCap
        '''权益'''
        alr_dict_2 = {"kind": "权益"}
        #股东权益（%）
        equityCap = round(equity / Cap * 100, 1)
        alr_dict_2["股东权益（%）"]=equityCap
        alr_dict_list.append(alr_dict)
        alr_dict_list.append(alr_dict_1)
        alr_dict_list.append(alr_dict_2)
        for o in alr_dict_list:
            print(o)

    #现金流量表
    def cash_flow_st(self):
        # scode = input("输入股票代码：")
        # year = input("输入年份：")
        # #
        # if year=="n12":
        #     info=getData(scode,year)
        # else:
        #     info=getData(scode,year)

        cash_flow_dict={}
        #期初现金
        cash_flow_dict["期初现金"]=float(self.info["加:期初现金及现金等价物余额"])
        #+ 营业活动现金流量 (from 损益表)
        cash_flow_dict["+ 营业活动现金流量 (from 损益表)"] =float(self.info["经营活动产生现金流量净额"])
        #+ 投资活动现金流量 (from 资产负债表左)
        cash_flow_dict["+ 投资活动现金流量 (from 资产负债表左)"] =float(self.info["投资活动产生的现金流量净额"])#投资活动产生的现金流量净额
        #+ 融资活动现金流量 (from 资产负债表右)
        cash_flow_dict["+ 融资活动现金流量 (from 资产负债表右)"] =float(self.info["筹资活动产生的现金流量净额"])#筹资活动产生的现金流量净额
        #期末现金
        cash_flow_dict["期末现金"] =float(self.info["六、期末现金及现金等价物余额"])
        #自由现金流（FCF）=经营活动产生的现金流量净额-购建固定资产、无形资产和其他长期资产支付的现金
        cash_flow_dict["自由现金流（FCF）"] =self.info["经营活动产生现金流量净额"]-self.info["购建固定资产、无形资产和其他长期资产所支付的现金"]
        print(self.info["经营活动产生现金流量净额"],self.info["购建固定资产、无形资产和其他长期资产所支付的现金"])
        print(cash_flow_dict)

    # #五大财务比率（+成长能力）
    def five_ratio(self):

        info=self.info
        info0=self.info0
        '''财务结构'''
        dict0 = {"kind":"财务结构"}

        dict0["资产负债率(%)"]=float(info["负债合计"])/float(info["资产总计"])
        dict0["长期资金占重资产比率(%)"] =(float(info["所有者权益(或股东权益)合计"])+float(info["非流动负债合计"]))/(float(info["在建工程"])+float(info["固定资产净额"])+float(info["工程物资"]))#长期资金占重资产比率(Longterm Ratio) = (股东权益+长期负债)(Total Equity + Non Current Liability) / (固定资产 + 工程物资 + 在建工程)(Fixed Assets + Construction Materials +Construction In Progress)

        '''偿债能力'''
        dict1 = {"kind": "财务结构"}
        dict1["流动比率(%)"] =float(info["流动资产合计"])/float(info["流动负债合计"])#流动比率(Current Ratio) = 流动资产总额(Total Assets) / 流动负债总额(Current Liabilities)
        if info['应收票据及应收账款'] == 0:
            receivable=(info["应收账款"])+(info["应收票据"])#应收账款+应收票据
        else:
            receivable = info["应收票据及应收账款"]
        dict1["速动比率(%)"] =(float(info["货币资金"])+float(info["交易性金融资产"])+receivable+float(info["应收利息"])+float(info["应收股利"])+float(info["其他应收款"]))/float(info["流动负债合计"])#速动比率(%) = (货币资金 + 交易性金融资产 + 应收票据及应收账款 + 合同资产 + 应收股利 + 应收利息 + 其他应收款) / 流动负债(Total Liabilities)

        '''缺利息费用，暂时用财务费用'''
        dict1["利息保障倍数"] =(float(info["四、利润总额"])-float(info["财务费用"]))/float(info["财务费用"])#利息保障倍数(Interest Coverage) = 息税前利润(EBITDA) / 利息费用(Interest Expense)

        '''运营能力'''
        dict2 = {"kind": "财务结构"}

        dict2["应收款项周转率(次/年)"] =float(info["营业收入"])/float((info0["应收账款"]+info["应收账款"])/2)#应收款项周转率(次/年) = 营业收入/平均应收账款
        dict2["应收款项周转天数(天)"] =365/(float(info["营业收入"])/float((info0["应收账款"]+info["应收账款"])/2))
        dict2["存货周转率(次/年)"] =float(info["营业收入"])/float((info0["存货"]+info["存货"])/2)#营业成本/平均存货
        dict2["存货周转天数(天)"] =365/(float(info["营业收入"])/float((info0["存货"]+info["存货"])/2))
        dict2["固定资产周转率(次/年)"] =float(info["营业收入"])/float((info0["固定资产净额"]+info["固定资产净额"])/2)
        # dict2["完整生意周期(天)"] =
        #销售成本÷平均应付账款
        dict2["应付款项周转天数(天)"] =float(float(info["营业成本"]/(info0["应付账款"]+info["应付账款"])/2))
        # dict2["缺钱天数(天)"] =
        dict2["总资产周转率(次/年)"] =float(info["营业收入"])/float((info0["资产总计"]+info["资产总计"])/2)

        '''盈利能力'''
        dict3 = {"kind": "财务结构"}

        dict3["ROA=资产收益率(%)"] =float(info["五、净利润"])/float((info0["资产总计"]+info["资产总计"])/2)
        dict3["ROE=净资产收益率(%)"] =float(info["五、净利润"])/float((info0["所有者权益(或股东权益)合计"]+info["所有者权益(或股东权益)合计"])/2)

        dict3["毛利率(%)"] =(float(info["营业收入"])-float(info["营业成本"]))/float(info["营业收入"])
        dict3["营业利润率(%)"] =float(info["四、利润总额"])/float(info["营业收入"])
        dict3["净利率(%)"] =float(info["五、净利润"])/float(info["营业收入"])
        dict3["营业费用率(%)"] =float((info["销售费用"])+info["财务费用"]+info["管理费用"])/float(info["营业收入"])
        dict3["经营安全边际率(%)"] =float(info["四、利润总额"])/float(info["营业收入"])/(float(info["营业收入"])-float(info["营业成本"]))/float(info["营业收入"])
        # dict3["EPS=基本每股收益(元)"] =

        '''成长能力'''
        dict4 = {"kind": "财务结构"}

        dict4["营收增长率(%)"] =(float(info["营业收入"])-float(info0["营业收入"]))/float(info0["营业收入"])
        dict4["营业利润增长率(%)"] =(float(info["四、利润总额"])-float(info0["四、利润总额"]))/float(info0["四、利润总额"])
        dict4["净资产增长率(%)"] =(float(info["所有者权益(或股东权益)合计"])-float(info0["所有者权益(或股东权益)合计"]))/float(info0["所有者权益(或股东权益)合计"])

        '''现金流量'''
        dict5 = {"kind": "财务结构"}

        dict5["现金流量比率(%)"] =float(info["经营活动产生的现金流量净额"])/float(info["流动负债合计"])
        # dict5["现金流量允当比率(%)"] =
        # dict5["现金再投资比率(%)"] =


        all_dict=[]
        all_dict.extend([dict0,dict1,dict2,dict3,dict4,dict5])
        for i in all_dict:
            print(i)

    def scheduler(self):
        self.asset_liability_ratio()
        self.cash_flow_st()
        self.five_ratio()


if __name__ == '__main__':
    Rp=Report_dealer()
    Rp.scheduler()

