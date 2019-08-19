# -*- coding : utf-8 -*- #

__author__ = "Gallen_qiu"

from 重要财务指标 import Report_index


class Dupont:
    def __init__(self):
        self.info={}
        self.get_data()

        self.index={}


    def get_data(self):
        Ri=Report_index()
        self.info=Ri.scheduler()[0]


    def index_(self):
        index={}
        index["ROE"]=self.info["盈利能力"]["ROE=净资产收益率(%)"]

        index["权益乘数"]=1/(1-self.info["财务结构"]["资产负债率(%)"])
        index["资产周转率"] =self.info["运营能力"]["总资产周转率(次/年)"]
        index["净利率"] =self.info["盈利能力"]["净利率(%)"]

        '''财务能力'''
        index["负债比率"] =self.info["财务结构"]["资产负债率(%)"]
        index["流动比"] =self.info["偿债能力"]["流动比率(%)"]
        index["速动比"] =self.info["偿债能力"]["速动比率(%)"]
        index["利息保障倍数"] =self.info["偿债能力"]["利息保障倍数"]

        '''运营能力'''
        # index["流动资产比率"] =
        # index["非流动资产比率"] =
        index["存货周转率"] =self.info["运营能力"]["存货周转率(次/年)"]
        index["存货在库天数"] =self.info["运营能力"]["存货周转天数(天)"]
        index["应收帐款周转率"] =self.info["运营能力"]["应收款项周转率(次/年)"]
        index["应收款项周转天数"] =self.info["运营能力"]["应收款项周转天数(天)"]

        '''盈利能力'''
        index["毛利率"] =self.info["盈利能力"]["毛利率(%)"]
        index["营业利润率"] =self.info["盈利能力"]["营业利润率(%)"]
        # print(index)
        self.index=index

    def analysis(self):
        '''净利率 x 总资产周转率  x 杠杆倍数 = ROE '''
        netIncomeE=(self.index["净利率"][0]*self.index["资产周转率"][-1]*self.index["权益乘数"][-1])-(self.index["净利率"][-1]*self.index["资产周转率"][-1]*self.index["权益乘数"][-1])
        tofTotalE=(self.index["净利率"][0]*self.index["资产周转率"][0]*self.index["权益乘数"][-1])-(self.index["净利率"][0]*self.index["资产周转率"][-1]*self.index["权益乘数"][-1])
        leverageE=(self.index["净利率"][0]*self.index["资产周转率"][0]*self.index["权益乘数"][0])-(self.index["净利率"][0]*self.index["资产周转率"][0]*self.index["权益乘数"][-1])
        region=(self.index["净利率"][-1] * self.index["资产周转率"][-1] * self.index["权益乘数"][-1])
        now=(self.index["净利率"][0]*self.index["资产周转率"][0]*self.index["权益乘数"][0])
        if now-region >=0:
            print("正增长：2015 ~ 2019 年的 ROE 从 {}% 改变至 {}%".format(round(region*100,2),round(now*100,2)))
            if netIncomeE == max(netIncomeE, tofTotalE, leverageE):
                print("净利率")
                gpr = (self.index["毛利率"][0] - self.index["毛利率"][-1]) / self.index["毛利率"][-1]
                oppr = (self.index["营业利润率"][0] - self.index["营业利润率"][-1]) / self.index["营业利润率"][-1]
                if gpr == max(gpr, oppr):
                    print("主要原因为【毛利率】的改变。 毛利率变化 {}%".format(round(gpr * 100, 2)))
                else:
                    print("主要原因为【营业利润率】的改变。 营业利润率变化 {}%".format(round(oppr * 100, 2)))
            elif tofTotalE == max(netIncomeE, tofTotalE, leverageE):
                print("总资产周转率")
                # self.index["存货周转率"]

                invDay = (self.index["存货在库天数"][0] - self.index["存货在库天数"][-1]) / self.index["存货在库天数"][-1]

                # self.index["应收帐款周转率"]
                rbleDay = (self.index["应收款项周转天数"][0] - self.index["应收款项周转天数"][-1]) / self.index["应收款项周转天数"][-1]
                # self.index["应收款项周转天数"]
                if invDay == max(invDay, rbleDay):
                    print("主要原因为【存货周转率】的改变。 存货在库天数从 {} 天 变为 {} 天".format(self.index["存货在库天数"][-1],
                                                                         self.index["存货在库天数"][0]))
                else:
                    print("主要原因为【应收账款周转率】的改变。 应收款项周转天数从 {} 天 变为 {} 天".format(self.index["应收款项周转天数"][-1],
                                                                             self.index["应收款项周转天数"][0]))

            else:
                print("杠杆倍数")
        else:
            print("负增长：2015 ~ 2019 年的 ROE 从 {}% 改变至 {}%".format(round(region*100,2),round(now*100,2)))
            if netIncomeE == min(netIncomeE, tofTotalE, leverageE):
                print("净利率")
                gpr = (self.index["毛利率"][0] - self.index["毛利率"][-1]) / self.index["毛利率"][-1]
                oppr = (self.index["营业利润率"][0] - self.index["营业利润率"][-1]) / self.index["营业利润率"][-1]
                if gpr == min(gpr, oppr):
                    print("主要原因为【毛利率】的改变。 毛利率变化 {%}".format(round(gpr * 100, 2)))
                else:
                    print("主要原因为【营业利润率】的改变。 营业利润率变化 {}%".format(round(oppr * 100, 2)))
            elif tofTotalE == min(netIncomeE, tofTotalE, leverageE):
                print("总资产周转率")
                # self.index["存货周转率"]

                invDay = (self.index["存货在库天数"][0] - self.index["存货在库天数"][-1]) / self.index["存货在库天数"][-1]

                # self.index["应收帐款周转率"]
                rbleDay = (self.index["应收款项周转天数"][0] - self.index["应收款项周转天数"][-1]) / self.index["应收款项周转天数"][-1]
                # self.index["应收款项周转天数"]
                if invDay == min(invDay, rbleDay):
                    print("主要原因为【存货周转率】的改变。 存货在库天数从 {} 天 变为 {} 天".format(self.index["存货在库天数"][-1],
                                                                         self.index["存货在库天数"][0]))
                else:
                    print("主要原因为【应收账款周转率】的改变。 应收款项周转天数从 {} 天 变为 {} 天".format(self.index["应收款项周转天数"][-1],
                                                                             self.index["应收款项周转天数"][0]))

            else:
                print("杠杆倍数")




if __name__ == '__main__':
    Dp=Dupont()
    Dp.index_()
    Dp.analysis()





