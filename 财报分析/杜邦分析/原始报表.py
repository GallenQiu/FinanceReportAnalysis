# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"
import pymongo
from pymongo.collection import Collection
class Report_dealer:

    def __init__(self,code):
        # self.scode = input("输入股票代码：")
        self.scode = str(code)
        # self.year = input("输入年份：")
        # if self.year=="last":
        #     self.info=self.getData(self.scode ,self.year )
        # else:
        self.info=self.getData(self.scode)
        # self.info0 =self.getData(self.scode, int(self.year) - 1)
        '''报表'''
        self.balanceS = {}
        self.incomeS = {}
        self.cashFlowS = {}
        self.last12={}

    def getData(self,scode):
        # 建立连接
        client = pymongo.MongoClient('localhost', 27017)
        # 建立数据库
        db = client["XinlangFinance"]

        # 表的对象化
        mgtable = Collection(db, 'FinanceReport_data2')
        # print({"SECCODE":str(scode)})
        data=mgtable.find({"SECCODE":str(scode)}).sort([('year',-1)])
        # print(data[0])
        return data

    def getData_n12(self,scode):
        # 建立连接
        client = pymongo.MongoClient('localhost', 27017)
        # 建立数据库
        db = client["XinlangFinance"]

        # 表的对象化
        mgtable = Collection(db, 'FinanceReport_data_n12_06')
        # print({"SECCODE":str(scode)})
        data=mgtable.find({"SECCODE":str(scode)})
        # print(data[0])
        return data

    #资产负债表
    def balanceSheet(self):

        info_all=list(self.getData(self.scode))
        # for data in info_all:
        #     print(data)
        '''整理后放入字典balanceS'''
        balanceS = {}
        balanceS["SECNAME"] = info_all[0]["SECNAME"]
        balanceS["SECCODE"] = info_all[0]["SECCODE"]
        balanceS["f_kind"] = info_all[0]["f_kind"]
        balanceS["s_kind"] = info_all[0]["s_kind"]
        balanceS["t_kind"] = info_all[0]["t_kind"]

        balanceS["year"] = [info["year"] for info in info_all]
        # print(info_all[0]["报表日期"])
        balanceS["报表日期"] = [info["报表日期"] for info in info_all]
        balanceS["货币资金"] = [info["货币资金"] for info in info_all]
        balanceS["交易性金融资产"] = [info["交易性金融资产"] for info in info_all]
        balanceS["衍生金融资产"] = [info["衍生金融资产"] for info in info_all]
        balanceS["应收票据及应收账款"] = [info["应收票据及应收账款"] for info in info_all]
        balanceS["应收票据"] = [info["应收票据"] for info in info_all]
        balanceS["应收账款"] = [info["应收账款"] for info in info_all]
        balanceS["预付款项"] = [info["预付款项"] for info in info_all]
        balanceS["应收利息"] = [info["应收利息"] for info in info_all]
        balanceS["应收股利"] = [info["应收股利"] for info in info_all]
        balanceS["其他应收款"] = [info["其他应收款"] for info in info_all]
        balanceS["买入返售金融资产"] = [info["买入返售金融资产"] for info in info_all]
        balanceS["存货"] = [info["存货"] for info in info_all]
        balanceS["划分为持有待售的资产"] = [info["划分为持有待售的资产"] for info in info_all]
        balanceS["一年内到期的非流动资产"] = [info["一年内到期的非流动资产"] for info in info_all]
        balanceS["待摊费用"] = [info["待摊费用"] for info in info_all]
        balanceS["待处理流动资产损益"] = [info["待处理流动资产损益"] for info in info_all]
        balanceS["其他流动资产"] = [info["其他流动资产"] for info in info_all]
        balanceS["流动资产合计"] = [info["流动资产合计"] for info in info_all]
        balanceS["发放贷款及垫款"] = [info["发放贷款及垫款"] for info in info_all]
        balanceS["可供出售金融资产"] = [info["可供出售金融资产"] for info in info_all]
        balanceS["持有至到期投资"] = [info["持有至到期投资"] for info in info_all]
        balanceS["长期应收款"] = [info["长期应收款"] for info in info_all]
        balanceS["长期股权投资"] = [info["长期股权投资"] for info in info_all]
        balanceS["投资性房地产"] = [info["投资性房地产"] for info in info_all]
        balanceS["固定资产净额"] = [info["固定资产净额"] for info in info_all]
        balanceS["在建工程"] = [info["在建工程"] for info in info_all]
        balanceS["工程物资"] = [info["工程物资"] for info in info_all]
        balanceS["固定资产清理"] = [info["固定资产清理"] for info in info_all]
        balanceS["生产性生物资产"] = [info["生产性生物资产"] for info in info_all]
        balanceS["公益性生物资产"] = [info["公益性生物资产"] for info in info_all]
        balanceS["油气资产"] = [info["油气资产"] for info in info_all]
        balanceS["无形资产"] = [info["无形资产"] for info in info_all]
        balanceS["开发支出"] = [info["开发支出"] for info in info_all]
        balanceS["商誉"] = [info["商誉"] for info in info_all]
        balanceS["长期待摊费用"] = [info["长期待摊费用"] for info in info_all]
        balanceS["递延所得税资产"] = [info["递延所得税资产"] for info in info_all]
        balanceS["其他非流动资产"] = [info["其他非流动资产"] for info in info_all]
        balanceS["非流动资产合计"] = [info["非流动资产合计"] for info in info_all]
        balanceS["资产总计"] = [info["资产总计"] for info in info_all]
        balanceS["短期借款"] = [info["短期借款"] for info in info_all]
        balanceS["交易性金融负债"] = [info["交易性金融负债"] for info in info_all]
        balanceS["应付票据及应付账款"] = [info["应付票据及应付账款"] for info in info_all]
        balanceS["应付票据"] = [info["应付票据"] for info in info_all]
        balanceS["应付账款"] = [info["应付账款"] for info in info_all]
        balanceS["预收款项"] = [info["预收款项"] for info in info_all]
        balanceS["应付手续费及佣金"] = [info["应付手续费及佣金"] for info in info_all]
        balanceS["应付职工薪酬"] = [info["应付职工薪酬"] for info in info_all]
        balanceS["应交税费"] = [info["应交税费"] for info in info_all]
        balanceS["应付利息"] = [info["应付利息"] for info in info_all]
        balanceS["应付股利"] = [info["应付股利"] for info in info_all]
        balanceS["其他应付款"] = [info["其他应付款"] for info in info_all]
        balanceS["预提费用"] = [info["预提费用"] for info in info_all]
        balanceS["一年内的递延收益"] = [info["一年内的递延收益"] for info in info_all]
        balanceS["应付短期债券"] = [info["应付短期债券"] for info in info_all]
        balanceS["一年内到期的非流动负债"] = [info["一年内到期的非流动负债"] for info in info_all]
        balanceS["其他流动负债"] = [info["其他流动负债"] for info in info_all]
        balanceS["流动负债合计"] = [info["流动负债合计"] for info in info_all]
        balanceS["长期借款"] = [info["长期借款"] for info in info_all]
        balanceS["应付债券"] = [info["应付债券"] for info in info_all]
        balanceS["长期应付款"] = [info["长期应付款"] for info in info_all]
        balanceS["长期应付职工薪酬"] = [info["长期应付职工薪酬"] for info in info_all]
        balanceS["专项应付款"] = [info["专项应付款"] for info in info_all]
        balanceS["预计非流动负债"] = [info["预计非流动负债"] for info in info_all]
        balanceS["递延所得税负债"] = [info["递延所得税负债"] for info in info_all]
        balanceS["长期递延收益"] = [info["长期递延收益"] for info in info_all]
        balanceS["其他非流动负债"] = [info["其他非流动负债"] for info in info_all]
        balanceS["非流动负债合计"] = [info["非流动负债合计"] for info in info_all]
        balanceS["负债合计"] = [info["负债合计"] for info in info_all]
        balanceS["实收资本(或股本)"] = [info["实收资本(或股本)"] for info in info_all]
        balanceS["资本公积"] = [info["资本公积"] for info in info_all]
        balanceS["减：库存股"] = [info["减：库存股"] for info in info_all]
        balanceS["其他综合收益"] = [info["其他综合收益"] for info in info_all]
        balanceS["专项储备"] = [info["专项储备"] for info in info_all]
        balanceS["盈余公积"] = [info["盈余公积"] for info in info_all]
        balanceS["一般风险准备"] = [info["一般风险准备"] for info in info_all]
        balanceS["未分配利润"] = [info["未分配利润"] for info in info_all]
        balanceS["归属于母公司股东权益合计"] = [info["归属于母公司股东权益合计"] for info in info_all]
        balanceS["少数股东权益"] = [info["少数股东权益"] for info in info_all]
        balanceS["所有者权益(或股东权益)合计"] = [info["所有者权益(或股东权益)合计"] for info in info_all]
        balanceS["负债和所有者权益(或股东权益)总计"] = [info["负债和所有者权益(或股东权益)总计"] for info in info_all]
        # print(balanceS)

        info_all_n12 = self.getData_n12(self.scode)[0]
        '''将最近月份的资产负债表信息添加到balanceS中'''


        balanceS["year"][:0] = [2019]

        balanceS["报表日期"][:0] = [info_all_n12["报表日期"][0]]
        balanceS["货币资金"][:0] = [info_all_n12["货币资金"][0]]
        balanceS["交易性金融资产"][:0] = [info_all_n12["交易性金融资产"][0]]
        balanceS["衍生金融资产"][:0] = [info_all_n12["衍生金融资产"][0]]
        balanceS["应收票据及应收账款"][:0] = [info_all_n12["应收票据及应收账款"][0]]
        balanceS["应收票据"][:0] = [info_all_n12["应收票据"][0]]
        balanceS["应收账款"][:0] = [info_all_n12["应收账款"][0]]
        balanceS["预付款项"][:0] = [info_all_n12["预付款项"][0]]
        balanceS["应收利息"][:0] = [info_all_n12["应收利息"][0]]
        balanceS["应收股利"][:0] = [info_all_n12["应收股利"][0]]
        balanceS["其他应收款"][:0] = [info_all_n12["其他应收款"][0]]
        balanceS["买入返售金融资产"][:0] = [info_all_n12["买入返售金融资产"][0]]
        balanceS["存货"][:0] = [info_all_n12["存货"][0]]
        balanceS["划分为持有待售的资产"][:0] = [info_all_n12["划分为持有待售的资产"][0]]
        balanceS["一年内到期的非流动资产"][:0] = [info_all_n12["一年内到期的非流动资产"][0]]
        balanceS["待摊费用"][:0] = [info_all_n12["待摊费用"][0]]
        balanceS["待处理流动资产损益"][:0] = [info_all_n12["待处理流动资产损益"][0]]
        balanceS["其他流动资产"][:0] = [info_all_n12["其他流动资产"][0]]
        balanceS["流动资产合计"][:0] = [info_all_n12["流动资产合计"][0]]
        balanceS["发放贷款及垫款"][:0] = [info_all_n12["发放贷款及垫款"][0]]
        balanceS["可供出售金融资产"][:0] = [info_all_n12["可供出售金融资产"][0]]
        balanceS["持有至到期投资"][:0] = [info_all_n12["持有至到期投资"][0]]
        balanceS["长期应收款"][:0] = [info_all_n12["长期应收款"][0]]
        balanceS["长期股权投资"][:0] = [info_all_n12["长期股权投资"][0]]
        balanceS["投资性房地产"][:0] = [info_all_n12["投资性房地产"][0]]
        balanceS["固定资产净额"][:0] = [info_all_n12["固定资产净额"][0]]
        balanceS["在建工程"][:0] = [info_all_n12["在建工程"][0]]
        balanceS["工程物资"][:0] = [info_all_n12["工程物资"][0]]
        balanceS["固定资产清理"][:0] = [info_all_n12["固定资产清理"][0]]
        balanceS["生产性生物资产"][:0] = [info_all_n12["生产性生物资产"][0]]
        balanceS["公益性生物资产"][:0] = [info_all_n12["公益性生物资产"][0]]
        balanceS["油气资产"][:0] = [info_all_n12["油气资产"][0]]
        balanceS["无形资产"][:0] = [info_all_n12["无形资产"][0]]
        balanceS["开发支出"][:0] = [info_all_n12["开发支出"][0]]
        balanceS["商誉"][:0] = [info_all_n12["商誉"][0]]
        balanceS["长期待摊费用"][:0] = [info_all_n12["长期待摊费用"][0]]
        balanceS["递延所得税资产"][:0] = [info_all_n12["递延所得税资产"][0]]
        balanceS["其他非流动资产"][:0] = [info_all_n12["其他非流动资产"][0]]
        balanceS["非流动资产合计"][:0] = [info_all_n12["非流动资产合计"][0]]
        balanceS["资产总计"][:0] = [info_all_n12["资产总计"][0]]
        balanceS["短期借款"][:0] = [info_all_n12["短期借款"][0]]
        balanceS["交易性金融负债"][:0] = [info_all_n12["交易性金融负债"][0]]
        balanceS["应付票据及应付账款"][:0] = [info_all_n12["应付票据及应付账款"][0]]
        balanceS["应付票据"][:0] = [info_all_n12["应付票据"][0]]
        balanceS["应付账款"][:0] = [info_all_n12["应付账款"][0]]
        balanceS["预收款项"][:0] = [info_all_n12["预收款项"][0]]
        balanceS["应付手续费及佣金"][:0] = [info_all_n12["应付手续费及佣金"][0]]
        balanceS["应付职工薪酬"][:0] = [info_all_n12["应付职工薪酬"][0]]
        balanceS["应交税费"][:0] = [info_all_n12["应交税费"][0]]
        balanceS["应付利息"][:0] = [info_all_n12["应付利息"][0]]
        balanceS["应付股利"][:0] = [info_all_n12["应付股利"][0]]
        balanceS["其他应付款"][:0] = [info_all_n12["其他应付款"][0]]
        balanceS["预提费用"][:0] = [info_all_n12["预提费用"][0]]
        balanceS["一年内的递延收益"][:0] = [info_all_n12["一年内的递延收益"][0]]
        balanceS["应付短期债券"][:0] = [info_all_n12["应付短期债券"][0]]
        balanceS["一年内到期的非流动负债"][:0] = [info_all_n12["一年内到期的非流动负债"][0]]
        balanceS["其他流动负债"][:0] = [info_all_n12["其他流动负债"][0]]
        balanceS["流动负债合计"][:0] = [info_all_n12["流动负债合计"][0]]
        balanceS["长期借款"][:0] = [info_all_n12["长期借款"][0]]
        balanceS["应付债券"][:0] = [info_all_n12["应付债券"][0]]
        balanceS["长期应付款"][:0] = [info_all_n12["长期应付款"][0]]
        balanceS["长期应付职工薪酬"][:0] = [info_all_n12["长期应付职工薪酬"][0]]
        balanceS["专项应付款"][:0] = [info_all_n12["专项应付款"][0]]
        balanceS["预计非流动负债"][:0] = [info_all_n12["预计非流动负债"][0]]
        balanceS["递延所得税负债"][:0] = [info_all_n12["递延所得税负债"][0]]
        balanceS["长期递延收益"][:0] = [info_all_n12["长期递延收益"][0]]
        balanceS["其他非流动负债"][:0] = [info_all_n12["其他非流动负债"][0]]
        balanceS["非流动负债合计"][:0] = [info_all_n12["非流动负债合计"][0]]
        balanceS["负债合计"][:0] = [info_all_n12["负债合计"][0]]
        balanceS["实收资本(或股本)"][:0] = [info_all_n12["实收资本(或股本)"][0]]
        balanceS["资本公积"][:0] = [info_all_n12["资本公积"][0]]
        balanceS["减：库存股"][:0] = [info_all_n12["减：库存股"][0]]
        balanceS["其他综合收益"][:0] = [info_all_n12["其他综合收益"][0]]
        balanceS["专项储备"][:0] = [info_all_n12["专项储备"][0]]
        balanceS["盈余公积"][:0] = [info_all_n12["盈余公积"][0]]
        balanceS["一般风险准备"][:0] = [info_all_n12["一般风险准备"][0]]
        balanceS["未分配利润"][:0] = [info_all_n12["未分配利润"][0]]
        balanceS["归属于母公司股东权益合计"][:0] = [info_all_n12["归属于母公司股东权益合计"][0]]
        balanceS["少数股东权益"][:0] = [info_all_n12["少数股东权益"][0]]
        balanceS["所有者权益(或股东权益)合计"][:0] = [info_all_n12["所有者权益(或股东权益)合计"][0]]
        balanceS["负债和所有者权益(或股东权益)总计"][:0] = [info_all_n12["负债和所有者权益(或股东权益)总计"][0]]

        self.balanceS=balanceS
        '''balanceS={"货币资金":[最近月份期末数,2018,2017,2016,2015,2014]}'''
        # print(balanceS)

    def incomeStm(self):
        info_all = list(self.getData(self.scode))

        incomeS={}

        incomeS["一、营业总收入"] = [info["一、营业总收入"] for info in info_all]
        incomeS["营业收入"] = [info["营业收入"] for info in info_all]
        incomeS["二、营业总成本"] = [info["二、营业总成本"] for info in info_all]
        incomeS["营业成本"] = [info["营业成本"] for info in info_all]
        incomeS["营业税金及附加"] = [info["营业税金及附加"] for info in info_all]
        incomeS["销售费用"] = [info["销售费用"] for info in info_all]
        incomeS["管理费用"] = [info["管理费用"] for info in info_all]
        incomeS["财务费用"] = [info["财务费用"] for info in info_all]
        incomeS["资产减值损失"] = [info["资产减值损失"] for info in info_all]
        incomeS["公允价值变动收益"] = [info["公允价值变动收益"] for info in info_all]
        incomeS["投资收益"] = [info["投资收益"] for info in info_all]
        incomeS["其中:对联营企业和合营企业的投资收益"] = [info["其中:对联营企业和合营企业的投资收益"] for info in info_all]
        incomeS["汇兑收益"] = [info["汇兑收益"] for info in info_all]
        incomeS["三、营业利润"] = [info["三、营业利润"] for info in info_all]
        incomeS["加:营业外收入"] = [info["加:营业外收入"] for info in info_all]
        incomeS["减：营业外支出"] = [info["减：营业外支出"] for info in info_all]
        incomeS["其中：非流动资产处置损失"] = [info["其中：非流动资产处置损失"] for info in info_all]
        incomeS["四、利润总额"] = [info["四、利润总额"] for info in info_all]
        incomeS["减：所得税费用"] = [info["减：所得税费用"] for info in info_all]
        incomeS["五、净利润"] = [info["五、净利润"] for info in info_all]
        incomeS["归属于母公司所有者的净利润"] = [info["归属于母公司所有者的净利润"] for info in info_all]
        incomeS["少数股东损益"] = [info["少数股东损益"] for info in info_all]
        incomeS["基本每股收益(元/股)"] = [info["基本每股收益(元/股)"] for info in info_all]
        incomeS["稀释每股收益(元/股)"] = [info["稀释每股收益(元/股)"] for info in info_all]
        incomeS["七、其他综合收益"] = [info["七、其他综合收益"] for info in info_all]
        incomeS["八、综合收益总额"] = [info["八、综合收益总额"] for info in info_all]
        incomeS["归属于母公司所有者的综合收益总额"] = [info["归属于母公司所有者的综合收益总额"] for info in info_all]
        incomeS["归属于少数股东的综合收益总额"] = [info["归属于少数股东的综合收益总额"] for info in info_all]


        info_all_n12 = self.getData_n12(self.scode)[0]
        '''将最近月份的信息添加到incomeS中'''

        n=2#n是2018年，上一年在list中的位置

        incomeS["一、营业总收入"][:0] = [
            info_all_n12["一、营业总收入"][n] - info_all_n12["一、营业总收入"][n + (4 - n)] + info_all_n12["一、营业总收入"][0]]
        incomeS["营业收入"][:0] = [info_all_n12["营业收入"][n] - info_all_n12["营业收入"][n + (4 - n)] + info_all_n12["营业收入"][0]]
        incomeS["二、营业总成本"][:0] = [
            info_all_n12["二、营业总成本"][n] - info_all_n12["二、营业总成本"][n + (4 - n)] + info_all_n12["二、营业总成本"][0]]
        incomeS["营业成本"][:0] = [info_all_n12["营业成本"][n] - info_all_n12["营业成本"][n + (4 - n)] + info_all_n12["营业成本"][0]]
        incomeS["营业税金及附加"][:0] = [
            info_all_n12["营业税金及附加"][n] - info_all_n12["营业税金及附加"][n + (4 - n)] + info_all_n12["营业税金及附加"][0]]
        incomeS["销售费用"][:0] = [info_all_n12["销售费用"][n] - info_all_n12["销售费用"][n + (4 - n)] + info_all_n12["销售费用"][0]]
        incomeS["管理费用"][:0] = [info_all_n12["管理费用"][n] - info_all_n12["管理费用"][n + (4 - n)] + info_all_n12["管理费用"][0]]
        incomeS["财务费用"][:0] = [info_all_n12["财务费用"][n] - info_all_n12["财务费用"][n + (4 - n)] + info_all_n12["财务费用"][0]]
        incomeS["资产减值损失"][:0] = [
            info_all_n12["资产减值损失"][n] - info_all_n12["资产减值损失"][n + (4 - n)] + info_all_n12["资产减值损失"][0]]
        incomeS["公允价值变动收益"][:0] = [
            info_all_n12["公允价值变动收益"][n] - info_all_n12["公允价值变动收益"][n + (4 - n)] + info_all_n12["公允价值变动收益"][0]]
        incomeS["投资收益"][:0] = [info_all_n12["投资收益"][n] - info_all_n12["投资收益"][n + (4 - n)] + info_all_n12["投资收益"][0]]
        incomeS["其中:对联营企业和合营企业的投资收益"][:0] = [
            info_all_n12["其中:对联营企业和合营企业的投资收益"][n] - info_all_n12["其中:对联营企业和合营企业的投资收益"][n + (4 - n)] +
            info_all_n12["其中:对联营企业和合营企业的投资收益"][0]]
        incomeS["汇兑收益"][:0] = [info_all_n12["汇兑收益"][n] - info_all_n12["汇兑收益"][n + (4 - n)] + info_all_n12["汇兑收益"][0]]
        incomeS["三、营业利润"][:0] = [
            info_all_n12["三、营业利润"][n] - info_all_n12["三、营业利润"][n + (4 - n)] + info_all_n12["三、营业利润"][0]]
        incomeS["加:营业外收入"][:0] = [
            info_all_n12["加:营业外收入"][n] - info_all_n12["加:营业外收入"][n + (4 - n)] + info_all_n12["加:营业外收入"][0]]
        incomeS["减：营业外支出"][:0] = [
            info_all_n12["减：营业外支出"][n] - info_all_n12["减：营业外支出"][n + (4 - n)] + info_all_n12["减：营业外支出"][0]]
        incomeS["其中：非流动资产处置损失"][:0] = [
            info_all_n12["其中：非流动资产处置损失"][n] - info_all_n12["其中：非流动资产处置损失"][n + (4 - n)] + info_all_n12["其中：非流动资产处置损失"][
                0]]
        incomeS["四、利润总额"][:0] = [
            info_all_n12["四、利润总额"][n] - info_all_n12["四、利润总额"][n + (4 - n)] + info_all_n12["四、利润总额"][0]]
        incomeS["减：所得税费用"][:0] = [
            info_all_n12["减：所得税费用"][n] - info_all_n12["减：所得税费用"][n + (4 - n)] + info_all_n12["减：所得税费用"][0]]
        incomeS["五、净利润"][:0] = [
            info_all_n12["五、净利润"][n] - info_all_n12["五、净利润"][n + (4 - n)] + info_all_n12["五、净利润"][0]]
        incomeS["归属于母公司所有者的净利润"][:0] = [info_all_n12["归属于母公司所有者的净利润"][n] - info_all_n12["归属于母公司所有者的净利润"][n + (4 - n)] +
                                        info_all_n12["归属于母公司所有者的净利润"][0]]
        incomeS["少数股东损益"][:0] = [
            info_all_n12["少数股东损益"][n] - info_all_n12["少数股东损益"][n + (4 - n)] + info_all_n12["少数股东损益"][0]]
        incomeS["基本每股收益(元/股)"][:0] = [
            info_all_n12["基本每股收益(元/股)"][n] - info_all_n12["基本每股收益(元/股)"][n + (4 - n)] + info_all_n12["基本每股收益(元/股)"][0]]
        incomeS["稀释每股收益(元/股)"][:0] = [
            info_all_n12["稀释每股收益(元/股)"][n] - info_all_n12["稀释每股收益(元/股)"][n + (4 - n)] + info_all_n12["稀释每股收益(元/股)"][0]]
        incomeS["七、其他综合收益"][:0] = [
            info_all_n12["七、其他综合收益"][n] - info_all_n12["七、其他综合收益"][n + (4 - n)] + info_all_n12["七、其他综合收益"][0]]
        incomeS["八、综合收益总额"][:0] = [
            info_all_n12["八、综合收益总额"][n] - info_all_n12["八、综合收益总额"][n + (4 - n)] + info_all_n12["八、综合收益总额"][0]]
        incomeS["归属于母公司所有者的综合收益总额"][:0] = [
            info_all_n12["归属于母公司所有者的综合收益总额"][n] - info_all_n12["归属于母公司所有者的综合收益总额"][n + (4 - n)] +
            info_all_n12["归属于母公司所有者的综合收益总额"][0]]
        incomeS["归属于少数股东的综合收益总额"][:0] = [
            info_all_n12["归属于少数股东的综合收益总额"][n] - info_all_n12["归属于少数股东的综合收益总额"][n + (4 - n)] +
            info_all_n12["归属于少数股东的综合收益总额"][0]]
        self.incomeS=incomeS
        # print(incomeS)

    def cashFlowStm(self):
        info_all = list(self.getData(self.scode))

        cashFlowS={}
        cashFlowS["销售商品、提供劳务收到的现金"] = [info["销售商品、提供劳务收到的现金"] for info in info_all]
        cashFlowS["收到的税费返还"] = [info["收到的税费返还"] for info in info_all]
        cashFlowS["收到的其他与经营活动有关的现金"] = [info["收到的其他与经营活动有关的现金"] for info in info_all]
        cashFlowS["经营活动现金流入小计"] = [info["经营活动现金流入小计"] for info in info_all]
        cashFlowS["购买商品、接受劳务支付的现金"] = [info["购买商品、接受劳务支付的现金"] for info in info_all]
        cashFlowS["支付给职工以及为职工支付的现金"] = [info["支付给职工以及为职工支付的现金"] for info in info_all]
        cashFlowS["支付的各项税费"] = [info["支付的各项税费"] for info in info_all]
        cashFlowS["支付的其他与经营活动有关的现金"] = [info["支付的其他与经营活动有关的现金"] for info in info_all]
        cashFlowS["经营活动现金流出小计"] = [info["经营活动现金流出小计"] for info in info_all]
        cashFlowS["经营活动产生的现金流量净额"] = [info["经营活动产生的现金流量净额"] for info in info_all]
        cashFlowS["收回投资所收到的现金"] = [info["收回投资所收到的现金"] for info in info_all]
        cashFlowS["取得投资收益所收到的现金"] = [info["取得投资收益所收到的现金"] for info in info_all]
        cashFlowS["处置固定资产、无形资产和其他长期资产所收回的现金净额"] = [info["处置固定资产、无形资产和其他长期资产所收回的现金净额"] for info in info_all]
        cashFlowS["处置子公司及其他营业单位收到的现金净额"] = [info["处置子公司及其他营业单位收到的现金净额"] for info in info_all]
        cashFlowS["收到的其他与投资活动有关的现金"] = [info["收到的其他与投资活动有关的现金"] for info in info_all]
        cashFlowS["投资活动现金流入小计"] = [info["投资活动现金流入小计"] for info in info_all]
        cashFlowS["购建固定资产、无形资产和其他长期资产所支付的现金"] = [info["购建固定资产、无形资产和其他长期资产所支付的现金"] for info in info_all]
        cashFlowS["投资所支付的现金"] = [info["投资所支付的现金"] for info in info_all]
        cashFlowS["取得子公司及其他营业单位支付的现金净额"] = [info["取得子公司及其他营业单位支付的现金净额"] for info in info_all]
        cashFlowS["支付的其他与投资活动有关的现金"] = [info["支付的其他与投资活动有关的现金"] for info in info_all]
        cashFlowS["投资活动现金流出小计"] = [info["投资活动现金流出小计"] for info in info_all]
        cashFlowS["投资活动产生的现金流量净额"] = [info["投资活动产生的现金流量净额"] for info in info_all]
        cashFlowS["吸收投资收到的现金"] = [info["吸收投资收到的现金"] for info in info_all]
        cashFlowS["其中：子公司吸收少数股东投资收到的现金"] = [info["其中：子公司吸收少数股东投资收到的现金"] for info in info_all]
        cashFlowS["取得借款收到的现金"] = [info["取得借款收到的现金"] for info in info_all]
        cashFlowS["发行债券收到的现金"] = [info["发行债券收到的现金"] for info in info_all]
        cashFlowS["收到其他与筹资活动有关的现金"] = [info["收到其他与筹资活动有关的现金"] for info in info_all]
        cashFlowS["筹资活动现金流入小计"] = [info["筹资活动现金流入小计"] for info in info_all]
        cashFlowS["偿还债务支付的现金"] = [info["偿还债务支付的现金"] for info in info_all]
        cashFlowS["分配股利、利润或偿付利息所支付的现金"] = [info["分配股利、利润或偿付利息所支付的现金"] for info in info_all]
        cashFlowS["其中：子公司支付给少数股东的股利、利润"] = [info["其中：子公司支付给少数股东的股利、利润"] for info in info_all]
        cashFlowS["支付其他与筹资活动有关的现金"] = [info["支付其他与筹资活动有关的现金"] for info in info_all]
        cashFlowS["筹资活动现金流出小计"] = [info["筹资活动现金流出小计"] for info in info_all]
        cashFlowS["筹资活动产生的现金流量净额"] = [info["筹资活动产生的现金流量净额"] for info in info_all]
        cashFlowS["四、汇率变动对现金及现金等价物的影响"] = [info["四、汇率变动对现金及现金等价物的影响"] for info in info_all]
        cashFlowS["五、现金及现金等价物净增加额"] = [info["五、现金及现金等价物净增加额"] for info in info_all]
        cashFlowS["加:期初现金及现金等价物余额"] = [info["加:期初现金及现金等价物余额"] for info in info_all]
        cashFlowS["六、期末现金及现金等价物余额"] = [info["六、期末现金及现金等价物余额"] for info in info_all]
        cashFlowS["净利润"] = [info["净利润"] for info in info_all]
        cashFlowS["未确认的投资损失"] = [info["未确认的投资损失"] for info in info_all]
        cashFlowS["资产减值准备"] = [info["资产减值准备"] for info in info_all]
        cashFlowS["固定资产折旧、油气资产折耗、生产性物资折旧"] = [info["固定资产折旧、油气资产折耗、生产性物资折旧"] for info in info_all]
        cashFlowS["无形资产摊销"] = [info["无形资产摊销"] for info in info_all]
        cashFlowS["长期待摊费用摊销"] = [info["长期待摊费用摊销"] for info in info_all]
        cashFlowS["待摊费用的减少"] = [info["待摊费用的减少"] for info in info_all]
        cashFlowS["预提费用的增加"] = [info["预提费用的增加"] for info in info_all]
        cashFlowS["处置固定资产、无形资产和其他长期资产的损失"] = [info["处置固定资产、无形资产和其他长期资产的损失"] for info in info_all]
        cashFlowS["固定资产报废损失"] = [info["固定资产报废损失"] for info in info_all]
        cashFlowS["公允价值变动损失"] = [info["公允价值变动损失"] for info in info_all]
        cashFlowS["递延收益增加（减：减少）"] = [info["递延收益增加（减：减少）"] for info in info_all]
        cashFlowS["预计负债"] = [info["预计负债"] for info in info_all]
        cashFlowS["投资损失"] = [info["投资损失"] for info in info_all]
        cashFlowS["递延所得税资产减少"] = [info["递延所得税资产减少"] for info in info_all]
        cashFlowS["递延所得税负债增加"] = [info["递延所得税负债增加"] for info in info_all]
        cashFlowS["存货的减少"] = [info["存货的减少"] for info in info_all]
        cashFlowS["经营性应收项目的减少"] = [info["经营性应收项目的减少"] for info in info_all]
        cashFlowS["经营性应付项目的增加"] = [info["经营性应付项目的增加"] for info in info_all]
        cashFlowS["已完工尚未结算款的减少(减:增加)"] = [info["已完工尚未结算款的减少(减:增加)"] for info in info_all]
        cashFlowS["已结算尚未完工款的增加(减:减少)"] = [info["已结算尚未完工款的增加(减:减少)"] for info in info_all]
        cashFlowS["其他"] = [info["其他"] for info in info_all]
        cashFlowS["经营活动产生现金流量净额"] = [info["经营活动产生现金流量净额"] for info in info_all]
        cashFlowS["债务转为资本"] = [info["债务转为资本"] for info in info_all]
        cashFlowS["一年内到期的可转换公司债券"] = [info["一年内到期的可转换公司债券"] for info in info_all]
        cashFlowS["融资租入固定资产"] = [info["融资租入固定资产"] for info in info_all]
        cashFlowS["现金的期末余额"] = [info["现金的期末余额"] for info in info_all]
        cashFlowS["现金的期初余额"] = [info["现金的期初余额"] for info in info_all]
        cashFlowS["现金等价物的期末余额"] = [info["现金等价物的期末余额"] for info in info_all]
        cashFlowS["现金等价物的期初余额"] = [info["现金等价物的期初余额"] for info in info_all]
        cashFlowS["现金及现金等价物的净增加额"] = [info["现金及现金等价物的净增加额"] for info in info_all]


        n=2
        info_all_n12 = self.getData_n12(self.scode)[0]
        '''将最近月份的信息添加到cashFlowS中'''

        cashFlowS["销售商品、提供劳务收到的现金"][:0] = [info_all_n12["销售商品、提供劳务收到的现金"][n] - info_all_n12["销售商品、提供劳务收到的现金"][n + (4 - n)] +
                                           info_all_n12["销售商品、提供劳务收到的现金"][0]]
        cashFlowS["收到的税费返还"][:0] = [
            info_all_n12["收到的税费返还"][n] - info_all_n12["收到的税费返还"][n + (4 - n)] + info_all_n12["收到的税费返还"][0]]
        cashFlowS["收到的其他与经营活动有关的现金"][:0] = [
            info_all_n12["收到的其他与经营活动有关的现金"][n] - info_all_n12["收到的其他与经营活动有关的现金"][n + (4 - n)] +
            info_all_n12["收到的其他与经营活动有关的现金"][0]]
        cashFlowS["经营活动现金流入小计"][:0] = [
            info_all_n12["经营活动现金流入小计"][n] - info_all_n12["经营活动现金流入小计"][n + (4 - n)] + info_all_n12["经营活动现金流入小计"][0]]
        cashFlowS["购买商品、接受劳务支付的现金"][:0] = [info_all_n12["购买商品、接受劳务支付的现金"][n] - info_all_n12["购买商品、接受劳务支付的现金"][n + (4 - n)] +
                                           info_all_n12["购买商品、接受劳务支付的现金"][0]]
        cashFlowS["支付给职工以及为职工支付的现金"][:0] = [
            info_all_n12["支付给职工以及为职工支付的现金"][n] - info_all_n12["支付给职工以及为职工支付的现金"][n + (4 - n)] +
            info_all_n12["支付给职工以及为职工支付的现金"][0]]
        cashFlowS["支付的各项税费"][:0] = [
            info_all_n12["支付的各项税费"][n] - info_all_n12["支付的各项税费"][n + (4 - n)] + info_all_n12["支付的各项税费"][0]]
        cashFlowS["支付的其他与经营活动有关的现金"][:0] = [
            info_all_n12["支付的其他与经营活动有关的现金"][n] - info_all_n12["支付的其他与经营活动有关的现金"][n + (4 - n)] +
            info_all_n12["支付的其他与经营活动有关的现金"][0]]
        cashFlowS["经营活动现金流出小计"][:0] = [
            info_all_n12["经营活动现金流出小计"][n] - info_all_n12["经营活动现金流出小计"][n + (4 - n)] + info_all_n12["经营活动现金流出小计"][0]]
        cashFlowS["经营活动产生的现金流量净额"][:0] = [
            info_all_n12["经营活动产生的现金流量净额"][n] - info_all_n12["经营活动产生的现金流量净额"][n + (4 - n)] + info_all_n12["经营活动产生的现金流量净额"][
                0]]
        cashFlowS["收回投资所收到的现金"][:0] = [
            info_all_n12["收回投资所收到的现金"][n] - info_all_n12["收回投资所收到的现金"][n + (4 - n)] + info_all_n12["收回投资所收到的现金"][0]]
        cashFlowS["取得投资收益所收到的现金"][:0] = [
            info_all_n12["取得投资收益所收到的现金"][n] - info_all_n12["取得投资收益所收到的现金"][n + (4 - n)] + info_all_n12["取得投资收益所收到的现金"][0]]
        cashFlowS["处置固定资产、无形资产和其他长期资产所收回的现金净额"][:0] = [
            info_all_n12["处置固定资产、无形资产和其他长期资产所收回的现金净额"][n] - info_all_n12["处置固定资产、无形资产和其他长期资产所收回的现金净额"][n + (4 - n)] +
            info_all_n12["处置固定资产、无形资产和其他长期资产所收回的现金净额"][0]]
        cashFlowS["处置子公司及其他营业单位收到的现金净额"][:0] = [
            info_all_n12["处置子公司及其他营业单位收到的现金净额"][n] - info_all_n12["处置子公司及其他营业单位收到的现金净额"][n + (4 - n)] +
            info_all_n12["处置子公司及其他营业单位收到的现金净额"][0]]
        cashFlowS["收到的其他与投资活动有关的现金"][:0] = [
            info_all_n12["收到的其他与投资活动有关的现金"][n] - info_all_n12["收到的其他与投资活动有关的现金"][n + (4 - n)] +
            info_all_n12["收到的其他与投资活动有关的现金"][0]]
        cashFlowS["投资活动现金流入小计"][:0] = [
            info_all_n12["投资活动现金流入小计"][n] - info_all_n12["投资活动现金流入小计"][n + (4 - n)] + info_all_n12["投资活动现金流入小计"][0]]
        cashFlowS["购建固定资产、无形资产和其他长期资产所支付的现金"][:0] = [
            info_all_n12["购建固定资产、无形资产和其他长期资产所支付的现金"][n] - info_all_n12["购建固定资产、无形资产和其他长期资产所支付的现金"][n + (4 - n)] +
            info_all_n12["购建固定资产、无形资产和其他长期资产所支付的现金"][0]]
        cashFlowS["投资所支付的现金"][:0] = [
            info_all_n12["投资所支付的现金"][n] - info_all_n12["投资所支付的现金"][n + (4 - n)] + info_all_n12["投资所支付的现金"][0]]
        cashFlowS["取得子公司及其他营业单位支付的现金净额"][:0] = [
            info_all_n12["取得子公司及其他营业单位支付的现金净额"][n] - info_all_n12["取得子公司及其他营业单位支付的现金净额"][n + (4 - n)] +
            info_all_n12["取得子公司及其他营业单位支付的现金净额"][0]]
        cashFlowS["支付的其他与投资活动有关的现金"][:0] = [
            info_all_n12["支付的其他与投资活动有关的现金"][n] - info_all_n12["支付的其他与投资活动有关的现金"][n + (4 - n)] +
            info_all_n12["支付的其他与投资活动有关的现金"][0]]
        cashFlowS["投资活动现金流出小计"][:0] = [
            info_all_n12["投资活动现金流出小计"][n] - info_all_n12["投资活动现金流出小计"][n + (4 - n)] + info_all_n12["投资活动现金流出小计"][0]]
        cashFlowS["投资活动产生的现金流量净额"][:0] = [
            info_all_n12["投资活动产生的现金流量净额"][n] - info_all_n12["投资活动产生的现金流量净额"][n + (4 - n)] + info_all_n12["投资活动产生的现金流量净额"][
                0]]
        cashFlowS["吸收投资收到的现金"][:0] = [
            info_all_n12["吸收投资收到的现金"][n] - info_all_n12["吸收投资收到的现金"][n + (4 - n)] + info_all_n12["吸收投资收到的现金"][0]]
        cashFlowS["其中：子公司吸收少数股东投资收到的现金"][:0] = [
            info_all_n12["其中：子公司吸收少数股东投资收到的现金"][n] - info_all_n12["其中：子公司吸收少数股东投资收到的现金"][n + (4 - n)] +
            info_all_n12["其中：子公司吸收少数股东投资收到的现金"][0]]
        cashFlowS["取得借款收到的现金"][:0] = [
            info_all_n12["取得借款收到的现金"][n] - info_all_n12["取得借款收到的现金"][n + (4 - n)] + info_all_n12["取得借款收到的现金"][0]]
        cashFlowS["发行债券收到的现金"][:0] = [
            info_all_n12["发行债券收到的现金"][n] - info_all_n12["发行债券收到的现金"][n + (4 - n)] + info_all_n12["发行债券收到的现金"][0]]
        cashFlowS["收到其他与筹资活动有关的现金"][:0] = [info_all_n12["收到其他与筹资活动有关的现金"][n] - info_all_n12["收到其他与筹资活动有关的现金"][n + (4 - n)] +
                                           info_all_n12["收到其他与筹资活动有关的现金"][0]]
        cashFlowS["筹资活动现金流入小计"][:0] = [
            info_all_n12["筹资活动现金流入小计"][n] - info_all_n12["筹资活动现金流入小计"][n + (4 - n)] + info_all_n12["筹资活动现金流入小计"][0]]
        cashFlowS["偿还债务支付的现金"][:0] = [
            info_all_n12["偿还债务支付的现金"][n] - info_all_n12["偿还债务支付的现金"][n + (4 - n)] + info_all_n12["偿还债务支付的现金"][0]]
        cashFlowS["分配股利、利润或偿付利息所支付的现金"][:0] = [
            info_all_n12["分配股利、利润或偿付利息所支付的现金"][n] - info_all_n12["分配股利、利润或偿付利息所支付的现金"][n + (4 - n)] +
            info_all_n12["分配股利、利润或偿付利息所支付的现金"][0]]
        cashFlowS["其中：子公司支付给少数股东的股利、利润"][:0] = [
            info_all_n12["其中：子公司支付给少数股东的股利、利润"][n] - info_all_n12["其中：子公司支付给少数股东的股利、利润"][n + (4 - n)] +
            info_all_n12["其中：子公司支付给少数股东的股利、利润"][0]]
        cashFlowS["支付其他与筹资活动有关的现金"][:0] = [info_all_n12["支付其他与筹资活动有关的现金"][n] - info_all_n12["支付其他与筹资活动有关的现金"][n + (4 - n)] +
                                           info_all_n12["支付其他与筹资活动有关的现金"][0]]
        cashFlowS["筹资活动现金流出小计"][:0] = [
            info_all_n12["筹资活动现金流出小计"][n] - info_all_n12["筹资活动现金流出小计"][n + (4 - n)] + info_all_n12["筹资活动现金流出小计"][0]]
        cashFlowS["筹资活动产生的现金流量净额"][:0] = [
            info_all_n12["筹资活动产生的现金流量净额"][n] - info_all_n12["筹资活动产生的现金流量净额"][n + (4 - n)] + info_all_n12["筹资活动产生的现金流量净额"][
                0]]
        cashFlowS["四、汇率变动对现金及现金等价物的影响"][:0] = [
            info_all_n12["四、汇率变动对现金及现金等价物的影响"][n] - info_all_n12["四、汇率变动对现金及现金等价物的影响"][n + (4 - n)] +
            info_all_n12["四、汇率变动对现金及现金等价物的影响"][0]]
        cashFlowS["五、现金及现金等价物净增加额"][:0] = [info_all_n12["五、现金及现金等价物净增加额"][n] - info_all_n12["五、现金及现金等价物净增加额"][n + (4 - n)] +
                                           info_all_n12["五、现金及现金等价物净增加额"][0]]
        cashFlowS["加:期初现金及现金等价物余额"][:0] = [info_all_n12["加:期初现金及现金等价物余额"][n] - info_all_n12["加:期初现金及现金等价物余额"][n + (4 - n)] +
                                           info_all_n12["加:期初现金及现金等价物余额"][0]]
        cashFlowS["六、期末现金及现金等价物余额"][:0] = [info_all_n12["六、期末现金及现金等价物余额"][n] - info_all_n12["六、期末现金及现金等价物余额"][n + (4 - n)] +
                                           info_all_n12["六、期末现金及现金等价物余额"][0]]

        '''附注'''
        cashFlowS["净利润"][:0] = [info_all_n12["净利润"][n] - info_all_n12["净利润"][n + (4 - n)] + info_all_n12["净利润"][0]]
        cashFlowS["未确认的投资损失"][:0] = [
            info_all_n12["未确认的投资损失"][n] - info_all_n12["未确认的投资损失"][n + (4 - n)] + info_all_n12["未确认的投资损失"][0]]
        cashFlowS["资产减值准备"][:0] = [
            info_all_n12["资产减值准备"][n] - info_all_n12["资产减值准备"][n + (4 - n)] + info_all_n12["资产减值准备"][0]]
        cashFlowS["固定资产折旧、油气资产折耗、生产性物资折旧"][:0] = [
            info_all_n12["固定资产折旧、油气资产折耗、生产性物资折旧"][n] - info_all_n12["固定资产折旧、油气资产折耗、生产性物资折旧"][n + (4 - n)] +
            info_all_n12["固定资产折旧、油气资产折耗、生产性物资折旧"][0]]
        cashFlowS["无形资产摊销"][:0] = [
            info_all_n12["无形资产摊销"][n] - info_all_n12["无形资产摊销"][n + (4 - n)] + info_all_n12["无形资产摊销"][0]]
        cashFlowS["长期待摊费用摊销"][:0] = [
            info_all_n12["长期待摊费用摊销"][n] - info_all_n12["长期待摊费用摊销"][n + (4 - n)] + info_all_n12["长期待摊费用摊销"][0]]
        cashFlowS["待摊费用的减少"][:0] = [
            info_all_n12["待摊费用的减少"][n] - info_all_n12["待摊费用的减少"][n + (4 - n)] + info_all_n12["待摊费用的减少"][0]]
        cashFlowS["预提费用的增加"][:0] = [
            info_all_n12["预提费用的增加"][n] - info_all_n12["预提费用的增加"][n + (4 - n)] + info_all_n12["预提费用的增加"][0]]
        cashFlowS["处置固定资产、无形资产和其他长期资产的损失"][:0] = [
            info_all_n12["处置固定资产、无形资产和其他长期资产的损失"][n] - info_all_n12["处置固定资产、无形资产和其他长期资产的损失"][n + (4 - n)] +
            info_all_n12["处置固定资产、无形资产和其他长期资产的损失"][0]]
        cashFlowS["固定资产报废损失"][:0] = [
            info_all_n12["固定资产报废损失"][n] - info_all_n12["固定资产报废损失"][n + (4 - n)] + info_all_n12["固定资产报废损失"][0]]
        cashFlowS["公允价值变动损失"][:0] = [
            info_all_n12["公允价值变动损失"][n] - info_all_n12["公允价值变动损失"][n + (4 - n)] + info_all_n12["公允价值变动损失"][0]]
        cashFlowS["递延收益增加（减：减少）"][:0] = [
            info_all_n12["递延收益增加（减：减少）"][n] - info_all_n12["递延收益增加（减：减少）"][n + (4 - n)] + info_all_n12["递延收益增加（减：减少）"][0]]
        cashFlowS["预计负债"][:0] = [info_all_n12["预计负债"][n] - info_all_n12["预计负债"][n + (4 - n)] + info_all_n12["预计负债"][0]]
        cashFlowS["投资损失"][:0] = [info_all_n12["投资损失"][n] - info_all_n12["投资损失"][n + (4 - n)] + info_all_n12["投资损失"][0]]
        cashFlowS["递延所得税资产减少"][:0] = [
            info_all_n12["递延所得税资产减少"][n] - info_all_n12["递延所得税资产减少"][n + (4 - n)] + info_all_n12["递延所得税资产减少"][0]]
        cashFlowS["递延所得税负债增加"][:0] = [
            info_all_n12["递延所得税负债增加"][n] - info_all_n12["递延所得税负债增加"][n + (4 - n)] + info_all_n12["递延所得税负债增加"][0]]
        cashFlowS["存货的减少"][:0] = [info_all_n12["存货的减少"][n] - info_all_n12["存货的减少"][n + (4 - n)] + info_all_n12["存货的减少"][0]]
        cashFlowS["经营性应收项目的减少"][:0] = [
            info_all_n12["经营性应收项目的减少"][n] - info_all_n12["经营性应收项目的减少"][n + (4 - n)] + info_all_n12["经营性应收项目的减少"][0]]
        cashFlowS["经营性应付项目的增加"][:0] = [
            info_all_n12["经营性应付项目的增加"][n] - info_all_n12["经营性应付项目的增加"][n + (4 - n)] + info_all_n12["经营性应付项目的增加"][0]]
        cashFlowS["已完工尚未结算款的减少(减:增加)"][:0] = [
            info_all_n12["已完工尚未结算款的减少(减:增加)"][n] - info_all_n12["已完工尚未结算款的减少(减:增加)"][n + (4 - n)] +
            info_all_n12["已完工尚未结算款的减少(减:增加)"][0]]
        cashFlowS["已结算尚未完工款的增加(减:减少)"][:0] = [
            info_all_n12["已结算尚未完工款的增加(减:减少)"][n] - info_all_n12["已结算尚未完工款的增加(减:减少)"][n + (4 - n)] +
            info_all_n12["已结算尚未完工款的增加(减:减少)"][0]]
        cashFlowS["其他"][:0] = [info_all_n12["其他"][n] - info_all_n12["其他"][n + (4 - n)] + info_all_n12["其他"][0]]
        cashFlowS["经营活动产生现金流量净额"][:0] = [
            info_all_n12["经营活动产生现金流量净额"][n] - info_all_n12["经营活动产生现金流量净额"][n + (4 - n)] + info_all_n12["经营活动产生现金流量净额"][0]]
        cashFlowS["债务转为资本"][:0] = [
            info_all_n12["债务转为资本"][n] - info_all_n12["债务转为资本"][n + (4 - n)] + info_all_n12["债务转为资本"][0]]
        cashFlowS["一年内到期的可转换公司债券"][:0] = [
            info_all_n12["一年内到期的可转换公司债券"][n] - info_all_n12["一年内到期的可转换公司债券"][n + (4 - n)] + info_all_n12["一年内到期的可转换公司债券"][
                0]]
        cashFlowS["融资租入固定资产"][:0] = [
            info_all_n12["融资租入固定资产"][n] - info_all_n12["融资租入固定资产"][n + (4 - n)] + info_all_n12["融资租入固定资产"][0]]
        cashFlowS["现金的期末余额"][:0] = [
            info_all_n12["现金的期末余额"][n] - info_all_n12["现金的期末余额"][n + (4 - n)] + info_all_n12["现金的期末余额"][0]]
        cashFlowS["现金的期初余额"][:0] = [
            info_all_n12["现金的期初余额"][n] - info_all_n12["现金的期初余额"][n + (4 - n)] + info_all_n12["现金的期初余额"][0]]
        cashFlowS["现金等价物的期末余额"][:0] = [
            info_all_n12["现金等价物的期末余额"][n] - info_all_n12["现金等价物的期末余额"][n + (4 - n)] + info_all_n12["现金等价物的期末余额"][0]]
        cashFlowS["现金等价物的期初余额"][:0] = [
            info_all_n12["现金等价物的期初余额"][n] - info_all_n12["现金等价物的期初余额"][n + (4 - n)] + info_all_n12["现金等价物的期初余额"][0]]
        cashFlowS["现金及现金等价物的净增加额"][:0] = [
            info_all_n12["现金及现金等价物的净增加额"][n] - info_all_n12["现金及现金等价物的净增加额"][n + (4 - n)] + info_all_n12["现金及现金等价物的净增加额"][
                0]]
        self.cashFlowS=cashFlowS
        # print(cashFlowS)

    def scheduler(self):
        self.balanceSheet()
        self.incomeStm()
        self.cashFlowStm()
        self.last12 = self.getData_n12(self.scode)[0]
        return self.balanceS ,self.incomeS,self.cashFlowS,self.last12

        # return self.balanceS


if __name__ == '__main__':
    Rd=Report_dealer("002230")
    # Rd.incomeStm()
    r=Rd.scheduler()
    print(r)


