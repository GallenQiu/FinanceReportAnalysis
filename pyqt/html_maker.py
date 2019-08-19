import math
from indexData import Report_index
from bs4 import BeautifulSoup
import numpy as np

class HtmlMaker():

    def __init__(self,scode):
        self.scode=scode
        self.getData1()
        self.index_maker()
        self.comment_maker()
        self.zfb_maker()

    '''倒序化百分比化'''
    def reverse(self,L):
        j=[]
        for i in L[::-1]:

            if np.isinf(i):
                if i>0:
                    i = "∞"
                else:
                    i="-∞"

            elif isinstance(i,float):
                i = round(i * 100, 2)
            else:
                i=i
            j.append(i)
        return j

    '''倒序化'''
    def reverse_(self,L):
        j=[]
        for i in L[::-1]:

            if np.isinf(i):

                if i > 0:
                    i = "∞"
                else:
                    i = "-∞"

            elif isinstance(i,float):
                i = round(i , 2)
            else:
                i=i
            j.append(i)
        return j

    '''倒序化百分比化2资产百分比部分用'''
    def reverse2(self, L):
        j = []
        for i in L[::-1]:

            if np.isinf(i):
                if i > 0:
                    i = "∞"
                else:
                    i = "-∞"

            elif isinstance(i, float):
                i = round(i * 100, 2)
            else:
                i = i
            j.append(i)
        return j

    '''倒序化3现金流量部分用'''
    def reverse3(self, L):
        j = []
        for i in L[::-1]:

            if np.isinf(i):
                if i > 0:
                    i = "∞"
                else:
                    i = "-∞"

            elif isinstance(i, float):
                i=i*10000#数据以万为单位
                if abs(i) >100000000:
                    i = str(round(i / 100000000, 2)) + "亿"
                elif abs(i) > 10000000:
                    i = str(round(i / 10000000, 2)) + "千万"
                elif abs(i) > 1000000:
                    i = str(round(i / 1000000, 2)) + "百万"
                elif abs(i) >10000:
                    i= str(round(i/10000,2))+"万"
                else:
                    i =round(i/10000,2)
            else:
                i = i
            j.append(i)
        return j

    '''获取数据集合'''
    def getData1(self):
        Ri = Report_index(self.scode)
        self.data = Ri.scheduler()[0]
        self.data_ = Ri.scheduler()
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

    '''生成画图的参数'''
    def polyline_maker(self,li):
        '''

        :param li: [96,90,21,23,89,80]
        :return:
        '''
        li2=li

        while "∞" in li2:
            li2.remove("∞")
        while "-∞" in li2:
            li2.remove("-∞")

        if li2!=None:
            try:
                c1_max = max(li2)  # 取出最大值
            except:
                print(li2)
            try:
                d14 = 15 - (15 / c1_max) * li[4] + 0.5
            except:
                d14 = 0.5
            try:
                d13 = 15 - (15 / c1_max) * li[3] + 0.5
            except:
                d13 = 0.5
            try:
                d12 = 15 - (15 / c1_max) * li[2] + 0.5
            except:
                d12 = 0.5
            try:
                d11 = 15 - (15 / c1_max) * li[1] + 0.5
            except:
                d11 = 0.5
            try:
                d10 = 15 - (15 / c1_max) * li[0] + 0.5
            except:
                d10 = 0.5
        else:
            d10=0.5
            d11=0.5
            d12=0.5
            d13=0.5
            d14=0.5

        polyline= '0 {} 8 {} 16 {} 24 {} 32 {}'.format(d10, d11, d12, d13, d14)
        polygon = '0 15.5 {} 32 15.5'.format(polyline)
        return polyline,polygon

    '''Index_Html生成'''
    def index_maker(self):

        '''财务结构'''
        data01 = self.reverse(self.data["财务结构"]["资产负债率(%)"])
        data02 = self.reverse(self.data["财务结构"]["长期资金占重资产比率(%)"])
        '''偿债能力'''
        data11 = self.reverse(self.data["偿债能力"]["流动比率(%)"])
        data12 = self.reverse(self.data["偿债能力"]["速动比率(%)"])
        data13 = self.reverse_(self.data["偿债能力"]["利息保障倍数"])
        '''运营能力'''
        data21 = self.reverse_(self.data["运营能力"]["应收款项周转率(次/年)"])
        data22 = self.reverse_(self.data["运营能力"]["应收款项周转天数(天)"])
        data23 = self.reverse_(self.data["运营能力"]["存货周转率(次/年)"])
        data24 = self.reverse_(self.data["运营能力"]["存货周转天数(天)"])
        data25 = self.reverse_(self.data["运营能力"]["固定资产周转率(次/年)"])
        data26 = self.reverse_(self.data["运营能力"]["应付款项周转天数(天)"])
        data27 = self.reverse_(self.data["运营能力"]["总资产周转率(次/年)"])
        '''盈利能力'''
        data31 = self.reverse(self.data["盈利能力"]["ROA=资产收益率(%)"])
        data32 = self.reverse(self.data["盈利能力"]["ROE=净资产收益率(%)"])
        data34 = self.reverse(self.data["盈利能力"]["毛利率(%)"])
        data35 = self.reverse(self.data["盈利能力"]["营业利润率(%)"])
        data36 = self.reverse(self.data["盈利能力"]["净利率(%)"])
        data37 = self.reverse(self.data["盈利能力"]["营业费用率(%)"])
        data38 = self.reverse(self.data["盈利能力"]["经营安全边际率(%)"])
        data39 = self.reverse_(self.data["盈利能力"]["EPS=基本每股收益(元)"])
        '''成长能力'''
        data41 = self.reverse(self.data["成长能力"]["营收增长率(%)"])
        data42 = self.reverse(self.data["成长能力"]["营业利润增长率(%)"])
        data43 = self.reverse(self.data["成长能力"]["净资产增长率(%)"])
        data51 = self.reverse(self.data["现金流量"]["现金流量比率(%)"])

        '''html文本'''
        html_region='''
        <html><head></head><body><div class="shadow-box">
<div class="sheet-header">
<h3 class="sheet-header__title" style="color:#495057;font-weight: 500;margin: 0;width: auto;">五大财务比率(+成长能力)</h3>
    <h3 class="sheet-header__title" style="color:#495057;font-weight: 500;margin: 0;width: auto;">  </h3>
</div>
<div class="scroll-container">
<div class="tab-content" id="alkeyTabContent">
<!-- 年 -->
<div aria-labelledby="alkey-alyearly-tab" class="tab-pane al-description fade active show" id="alkey-yearly" role="tabpanel">
<table class="table table-hover table-scroll">
<thead>
<tr>
<th class="p-1">  类别</th>
<th class="p-1">财务比率</th>
<th class="p-1">趋势</th>
<th class="p-1">
            2015
          </th>
<th class="p-1">
            2016
          </th>
<th class="p-1">
            2017
          </th>
<th class="p-1">
            2018
          </th>
<th class="p-1">
            近12个月
          </th>
</tr>
</thead>
<!-- 下面部分填数据-->
<!-- 下面部分填数据-->
<!-- 下面部分填数据-->
<!-- 下面部分填数据-->
<!-- 下面部分填数据-->
<!-- 下面部分填数据-->
<tbody>
<tr>
<th class="p-1" rowspan="2">
<span data-original-title="经营杠杆,看公司是否有破产危机" data-placement="top" data-toggle="tooltip" title="财务结构">
            财务结构
          </span>
</th>
<td class="p-1"><span><a class="wiki-terms">负债占资产比率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data01}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon01}"></polygon><polyline fill="none" points="{polyline01}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data01_0}</td><td class="p-1">{data01_1}</td><td class="p-1">{data01_2}</td><td class="p-1">{data01_3}</td><td class="p-1">{data01_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">长期资金占重资产比率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data02}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon02}"></polygon><polyline fill="none" points="{polyline02}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data02_0}</td><td class="p-1">{data02_1}</td><td class="p-1">{data02_2}</td><td class="p-1">{data02_3}</td><td class="p-1">{data02_4}</td>
</tr>
<tr class="tr-split-border">
<th class="p-1" rowspan="3">
<span data-original-title="危机情况下的企业清偿能力" data-placement="top" data-toggle="tooltip" title="偿债能力">
            偿债能力
          </span>
</th>
<td class="p-1"><span><a class="wiki-terms">流动比率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data11}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon11}"></polygon><polyline fill="none" points="{polyline11}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data11_0}</td><td class="p-1">{data11_1}</td><td class="p-1">{data11_2}</td><td class="p-1">{data11_3}</td><td class="p-1">{data11_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">速动比率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data12}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon12}"></polygon><polyline fill="none" points="{polyline12}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data12_0}</td><td class="p-1">{data12_1}</td><td class="p-1">{data12_2}</td><td class="p-1">{data12_3}</td><td class="p-1">{data12_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">利息保障倍数</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data13}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon13}"></polygon><polyline fill="none" points="{polyline13}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data13_0}</td><td class="p-1">{data13_1}</td><td class="p-1">{data13_2}</td><td class="p-1">{data13_3}</td><td class="p-1">{data13_4}</td>
</tr>
<tr class="tr-split-border">
<th class="p-1" rowspan="7">
<span data-original-title="企业自身的运营水平,通常取决于管理水平" data-placement="top" data-toggle="tooltip" title="运营能力">运营能力</span>
</th>
<td class="p-1"><span><a class="wiki-terms">应收款项周转率(次/年)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data21}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon21}"></polygon><polyline fill="none" points="{polyline21}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data21_0}</td><td class="p-1">{data21_1}</td><td class="p-1">{data21_2}</td><td class="p-1">{data21_3}</td><td class="p-1">{data21_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">应收款项周转天数(天)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data22}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon22}"></polygon><polyline fill="none" points="{polyline22}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data22_0}</td><td class="p-1">{data22_1}</td><td class="p-1">{data22_2}</td><td class="p-1">{data22_3}</td><td class="p-1">{data22_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">存货周转率(次/年)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data23}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon23}"></polygon><polyline fill="none" points="{polyline23}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data23_0}</td><td class="p-1">{data23_1}</td><td class="p-1">{data23_2}</td><td class="p-1">{data23_3}</td><td class="p-1">{data23_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">存货周转天数(天)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data24}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon24}"></polygon><polyline fill="none" points="{polyline24}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data24_0}</td><td class="p-1">{data24_1}</td><td class="p-1">{data24_2}</td><td class="p-1">{data24_3}</td><td class="p-1">{data24_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">固定资产周转率(次/年)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data25}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon25}"></polygon><polyline fill="none" points="{polyline25}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data25_0}</td><td class="p-1">{data25_1}</td><td class="p-1">{data25_2}</td><td class="p-1">{data25_3}</td><td class="p-1">{data25_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">应付款项周转天数(天)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data26}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon26}"></polygon><polyline fill="none" points="{polyline26}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data26_0}</td><td class="p-1">{data26_1}</td><td class="p-1">{data26_2}</td><td class="p-1">{data26_3}</td><td class="p-1">{data26_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">总资产周转率(次/年)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data27}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon27}"></polygon><polyline fill="none" points="{polyline27}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data27_0}</td><td class="p-1">{data27_1}</td><td class="p-1">{data27_2}</td><td class="p-1">{data27_3}</td><td class="p-1">{data27_4}</td>
</tr>
<tr class="tr-split-border">
<th class="p-1" rowspan="8">
<span data-original-title="行业,产品与服务的利润水平,取决于同行竞争力度" data-placement="top" data-toggle="tooltip" title="盈利能力">盈利能力</span>
</th>
<td class="p-1"><span><a class="wiki-terms">ROA=资产收益率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data31}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon31}"></polygon><polyline fill="none" points="{polyline31}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data31_0}</td><td class="p-1">{data31_1}</td><td class="p-1">{data31_2}</td><td class="p-1">{data31_3}</td><td class="p-1">{data31_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">ROE=净资产收益率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data32}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon32}"></polygon><polyline fill="none" points="{polyline32}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data32_0}</td><td class="p-1">{data32_1}</td><td class="p-1">{data32_2}</td><td class="p-1">{data32_3}</td><td class="p-1">{data32_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">毛利率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data34}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon34}"></polygon><polyline fill="none" points="{polyline34}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data34_0}</td><td class="p-1">{data34_1}</td><td class="p-1">{data34_2}</td><td class="p-1">{data34_3}</td><td class="p-1">{data34_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">营业利润率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data35}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon35}"></polygon><polyline fill="none" points="{polyline35}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data35_0}</td><td class="p-1">{data35_1}</td><td class="p-1">{data35_2}</td><td class="p-1">{data35_3}</td><td class="p-1">{data35_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">净利率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data36}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon36}"></polygon><polyline fill="none" points="{polyline36}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data36_0}</td><td class="p-1">{data36_1}</td><td class="p-1">{data36_2}</td><td class="p-1">{data36_3}</td><td class="p-1">{data36_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">营业费用率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data37}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon37}"></polygon><polyline fill="none" points="{polyline37}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data37_0}</td><td class="p-1">{data37_1}</td><td class="p-1">{data37_2}</td><td class="p-1">{data37_3}</td><td class="p-1">{data37_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">经营安全边际率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data38}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon38}"></polygon><polyline fill="none" points="{polyline38}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data38_0}</td><td class="p-1">{data38_1}</td><td class="p-1">{data38_2}</td><td class="p-1">{data38_3}</td><td class="p-1">{data38_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">EPS=基本每股收益(元)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data39}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon39}"></polygon><polyline fill="none" points="{polyline39}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data39_0}</td><td class="p-1">{data39_1}</td><td class="p-1">{data39_2}</td><td class="p-1">{data39_3}</td><td class="p-1">{data39_4}</td>
</tr>
<tr class="tr-split-border">
<th class="p-1" rowspan="3">
<span data-original-title="企业的成长速度" data-placement="top" data-toggle="tooltip" title="成长能力">成长能力</span>
</th>
<td class="p-1"><span><a class="wiki-terms">营收增长率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data41}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon41}"></polygon><polyline fill="none" points="{polyline41}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data41_0}</td><td class="p-1">{data41_1}</td><td class="p-1">{data41_2}</td><td class="p-1">{data41_3}</td><td class="p-1">{data41_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">营业利润增长率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data42}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon42}"></polygon><polyline fill="none" points="{polyline42}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data42_0}</td><td class="p-1">{data42_1}</td><td class="p-1">{data42_2}</td><td class="p-1">{data42_3}</td><td class="p-1">{data42_4}</td>
</tr>
<tr>
<td class="p-1"><span><a class="wiki-terms">净资本增长率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data43}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon43}"></polygon><polyline fill="none" points="{polyline43}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data43_0}</td><td class="p-1">{data43_1}</td><td class="p-1">{data43_2}</td><td class="p-1">{data43_3}</td><td class="p-1">{data43_4}</td>
</tr>
<tr class="tr-split-border">
<th class="p-1" rowspan="1">
<span data-original-title="企业的现金流状况,取决于公司的自身财务管理水平" data-placement="top" data-toggle="tooltip" title="现金流量">现金流量</span>
</th>
<td class="p-1"><span><a class="wiki-terms">现金流量比率(%)</a></span></td><td class="p-1 trend"><span class="line" style="display: none;">{data51}</span><svg class="peity" height="16" width="32"><polygon fill="#c6d9fd" points="{polygon51}"></polygon><polyline fill="none" points="{polyline51}" stroke="#4d89f9" stroke-linecap="square" stroke-width="1"></polyline></svg></td><td class="p-1">{data51_0}</td><td class="p-1">{data51_1}</td><td class="p-1">{data51_2}</td><td class="p-1">{data51_3}</td><td class="p-1">{data51_4}</td>
</tr>

</tbody>
</table>
</div>
</div>
</div>
</div></body></html> '''.format(
                                data01=data01,data01_0=data01[0],data01_1=data01[1],data01_2=data01[2],data01_3=data01[3],data01_4=data01[4],
                                data02=data02,data02_0=data02[0],data02_1=data02[1],data02_2=data02[2],data02_3=data02[3],data02_4=data02[4],

                                data11=data11,data11_0=data11[0],data11_1=data11[1],data11_2=data11[2],data11_3=data11[3],data11_4=data11[4],
                                data12=data12,data12_0=data12[0],data12_1=data12[1],data12_2=data12[2],data12_3=data12[3],data12_4=data12[4],
                                data13=data13,data13_0=data13[0],data13_1=data13[1],data13_2=data13[2],data13_3=data13[3],data13_4=data13[4],

                                data21=data21,data21_0=data21[0],data21_1=data21[1],data21_2=data21[2],data21_3=data21[3],data21_4=data21[4],
                                data22=data22,data22_0=data22[0],data22_1=data22[1],data22_2=data22[2],data22_3=data22[3],data22_4=data22[4],
                                data23=data23,data23_0=data23[0],data23_1=data23[1],data23_2=data23[2],data23_3=data23[3],data23_4=data23[4],
                                data24=data24,data24_0=data24[0],data24_1=data24[1],data24_2=data24[2],data24_3=data24[3],data24_4=data24[4],
                                data25=data25,data25_0=data25[0],data25_1=data25[1],data25_2=data25[2],data25_3=data25[3],data25_4=data25[4],
                                data26=data26,data26_0=data26[0],data26_1=data26[1],data26_2=data26[2],data26_3=data26[3],data26_4=data26[4],
                                data27=data27,data27_0=data27[0],data27_1=data27[1],data27_2=data27[2],data27_3=data27[3],data27_4=data27[4],

                                data31=data31,data31_0=data31[0],data31_1=data31[1],data31_2=data31[2],data31_3=data31[3],data31_4=data31[4],
                                data32=data32,data32_0=data32[0],data32_1=data32[1],data32_2=data32[2],data32_3=data32[3],data32_4=data32[4],
                                data34=data34,data34_0=data34[0],data34_1=data34[1],data34_2=data34[2],data34_3=data34[3],data34_4=data34[4],
                                data35=data35,data35_0=data35[0],data35_1=data35[1],data35_2=data35[2],data35_3=data35[3],data35_4=data35[4],
                                data36=data36,data36_0=data36[0],data36_1=data36[1],data36_2=data36[2],data36_3=data36[3],data36_4=data36[4],
                                data37=data37,data37_0=data37[0],data37_1=data37[1],data37_2=data37[2],data37_3=data37[3],data37_4=data37[4],
                                data38=data38,data38_0=data38[0],data38_1=data38[1],data38_2=data38[2],data38_3=data38[3],data38_4=data38[4],
                                data39=data39,data39_0=data39[0],data39_1=data39[1],data39_2=data39[2],data39_3=data39[3],data39_4=data39[4],

                                data41=data41,data41_0=data41[0],data41_1=data41[1],data41_2=data41[2],data41_3=data41[3],data41_4=data41[4],
                                data42=data42,data42_0=data42[0],data42_1=data42[1],data42_2=data42[2],data42_3=data42[3],data42_4=data42[4],
                                data43=data43,data43_0=data43[0],data43_1=data43[1],data43_2=data43[2],data43_3=data43[3],data43_4=data43[4],
                                data51=data51,data51_0=data51[0],data51_1=data51[1],data51_2=data51[2],data51_3=data51[3],data51_4=data51[4],

                                polyline01 =self.polyline_maker(data01)[0], polygon01 = self.polyline_maker(data01)[1],
                                polyline02=self.polyline_maker(data02)[0],polygon02=self.polyline_maker(data02)[1],
                                polyline11=self.polyline_maker(data11)[0],polygon11=self.polyline_maker(data11)[1],
                                polyline12=self.polyline_maker(data12)[0],polygon12=self.polyline_maker(data12)[1],
                                polyline13=self.polyline_maker(data13)[0],polygon13=self.polyline_maker(data13)[1],

                                polyline21=self.polyline_maker(data21)[0],polygon21=self.polyline_maker(data21)[1],
                                polyline22=self.polyline_maker(data22)[0],polygon22=self.polyline_maker(data22)[1],
                                polyline23=self.polyline_maker(data23)[0],polygon23=self.polyline_maker(data23)[1],
                                polyline24=self.polyline_maker(data24)[0],polygon24=self.polyline_maker(data24)[1],
                                polyline25=self.polyline_maker(data25)[0],polygon25=self.polyline_maker(data25)[1],
                                polyline26=self.polyline_maker(data26)[0],polygon26=self.polyline_maker(data26)[1],
                                polyline27=self.polyline_maker(data27)[0],polygon27=self.polyline_maker(data27)[1],

                                polyline31=self.polyline_maker(data31)[0],polygon31=self.polyline_maker(data31)[1],
                                polyline32=self.polyline_maker(data32)[0],polygon32=self.polyline_maker(data32)[1],
                                polyline34=self.polyline_maker(data34)[0],polygon34=self.polyline_maker(data34)[1],
                                polyline35=self.polyline_maker(data35)[0],polygon35=self.polyline_maker(data35)[1],
                                polyline36=self.polyline_maker(data36)[0],polygon36=self.polyline_maker(data36)[1],
                                polyline37=self.polyline_maker(data37)[0],polygon37=self.polyline_maker(data37)[1],
                                polyline38=self.polyline_maker(data38)[0],polygon38=self.polyline_maker(data38)[1],
                                polyline39=self.polyline_maker(data39)[0],polygon39=self.polyline_maker(data39)[1],

                                polyline41=self.polyline_maker(data41)[0],polygon41=self.polyline_maker(data41)[1],
                                polyline42=self.polyline_maker(data42)[0],polygon42=self.polyline_maker(data42)[1],
                                polyline43=self.polyline_maker(data43)[0],polygon43=self.polyline_maker(data43)[1],
                                polyline51=self.polyline_maker(data51)[0],polygon51=self.polyline_maker(data51)[1])
        with open('HTML/rate_index.html','w',encoding="utf8") as f:
            f.write(html_region)

    '''Comment_Html生成'''
    def comment_maker(self):
        data = self.data_
        '''现金能力'''
        # 现金与约当现金(占总资产%)
        value = data[2]["资产部分"]["现金与约当现金(%)"][0] * 100
        evaluate0 = []
        if np.isinf(value):
            evaluate0.append(("现金无法评价",""))
        elif float(value) < 10:
            print("现金很少")
            evaluate0.append(("现金很少 ","worse"))
        elif float(value) < 15:
            print("现金一般")
            evaluate0.append(("现金一般","normal"))
        elif float(value) < 25:
            print("现金充足")
            evaluate0.append(("现金充足","good"))
        else:
            print("现金超级多")
            evaluate0.append(("现金超级多","best"))

        # 现金流量比率(%)
        value = data[0]["现金流量"]["现金流量比率(%)"][0]*100
        if value < 0 :
            print("现金流状况不佳")
            evaluate0.append(("现金流状况不佳.","worse"))
        else:
            print("现金流状况一般")
            evaluate0.append(("现金流状况一般.","normal"))
        # 应收款项周转天数(天)
        value = data[0]["运营能力"]["应收款项周转天数(天)"][0]
        if value < 15:
            print("天天收现金")
            evaluate0.append(("天天收现金!","best"))
        elif value < 80:
            print("收款很快")
            evaluate0.append(("收款很快","good"))
        elif value < 100:
            print("收款速度一般")
            evaluate0.append(("收款速度一般.","normal"))
        elif value < 150:
            print("收款速度很慢！")
            evaluate0.append(("收款速度很慢!",""))
        else:
            print("收款速度也太慢了吧！")
            evaluate0.append(("收款速度也太慢了吧!","worse"))

        '''运营能力'''
        # 总资产周转率(次/年)
        evaluate1 = []
        value = data[0]["运营能力"]["总资产周转率(次/年)"][0]
        if value < 1:
            p="重资产,周转很慢，风险高!"
            if data[2]["资产部分"]["现金与约当现金(%)"][0] * 100 < 10:
                print("而且现金水位过低!")
                p=p+"而且现金水位过低!"
            elif data[2]["资产部分"]["现金与约当现金(%)"][0] * 100 < 15:
                print("而且现金比率偏低!")
                p=p+"而且现金比率偏低!"
            elif data[2]["资产部分"]["现金与约当现金(%)"][0] * 100 < 25:
                print("好在现金还算充足!")
                p=p+"好在现金还算充足!"
            else:
                print("还好现金超级多!")
                p=p+"还好现金超级多!"
            evaluate1.append((p,"normal"))
        elif value < 1.5:
            print("经营稳健,还不错.")
            evaluate1.append(("经营稳健,还不错.","good"))
        elif value < 2:
            print("经营效率优异")
            evaluate1.append(("经营效率优异.","better"))
        else:
            print("团队运营超一流")
            evaluate1.append(("团队运营超一流!","best"))
        # 存货周转天数
        value = data[0]["运营能力"]["存货周转天数(天)"][0]
        if value < 10:
            print("基本无存货,产品火爆")
            evaluate1.append(("基本无存货,产品火爆.","best"))
        elif value < 30:
            print("货卖的很快,口碑好")
            evaluate1.append(("货卖的很快,口碑好.","better"))
        elif value < 60:
            print("货卖的不错")
            evaluate1.append(("货卖的不错.","good"))
        elif value < 100:
            print("货卖的一般")
            evaluate1.append(("货卖的一般.","normal"))
        elif value < 150:
            print("卖货很慢,属于原物料或低频消费品.")
            evaluate1.append(("卖货很慢,属于原物料或低频消费品.",""))
        else:
            print("产品可能不好卖,特殊产业除外(酒类,地产等).")
            evaluate1.append(("产品可能不好卖,特殊产业除外(酒类,地产等).","worse"))

        # 完整生意周期
        value = data[0]["运营能力"]["存货周转天数(天)"][0]+data[0]["运营能力"]["应收款项周转天数(天)"][0]
        if value > 200:
            print("一轮生意要{0:.1f}天.生意完整周期偏长.".format(float(value)))
            p="一轮生意要{0:.1f}天.生意完整周期偏长.".format(float(value))
            if data[2]["资产部分"]["现金与约当现金(%)"][0] * 100 < 10:
                print("而且现金水位过低!")
                p=p+"而且现金水位过低!"
                if data[0]["盈利能力"]["毛利率(%)"][0]*100 > 30:
                    print("还好毛利足够高!")
                    p=p+"还好毛利足够高!"
            elif data[2]["资产部分"]["现金与约当现金(%)"][0] * 100 < 15:
                print("而且现金比率偏低!")
                p=p+"而且现金比率偏低!"
            elif data[2]["资产部分"]["现金与约当现金(%)"][0] * 100 < 25:
                print("好在现金还算充足!")
                p=p+"好在现金还算充足!"
            else:
                print("还好现金超级多!")
                p=p+"还好现金超级多!"
            evaluate1.append((p,"normal"))
        else:
            # print("一轮生意要{0:.1f}天.".format(float(value)))
            evaluate1.append(("一轮生意要{0:.1f}天.".format(float(value)),"good"))


        '''盈利能力'''
        # 毛利率
        evaluate2 = []
        value = data[0]["盈利能力"]["毛利率(%)"][0]*100
        if value < 10:
            # print("生意很难做,费用率{0:.1f}个点".format(float(value)))
            evaluate2.append(("生意很难做,毛利率{0:.1f}个点".format(float(value)),"worse"))
        elif value < 20:
            # print("生意很艰辛,费用率{0:.1f}个点".format(float(value)))
            evaluate2.append(("生意很艰辛,毛利率{0:.1f}个点".format(float(value)),""))
        elif value < 30:
            # print("毛利还可以,费用率{0:.1f}个点".format(float(res[28][i])))
            evaluate2.append(("毛利还可以,毛利率{0:.1f}个点".format(float(value)),""))
        elif value < 40:
            # print("毛利还不错,费用率{0:.1f}个点".format(float(res[28][i])))
            evaluate2.append(("毛利还不错,毛利率{0:.1f}个点".format(float(value)),"normal"))
        elif value < 55:
            # print("毛利很高,费用率{0:.1f}个点".format(float(res[28][i])))
            evaluate2.append(("毛利很高,毛利率{0:.1f}个点".format(float(value)),"good"))
        elif value < 70:
            # print("毛利超高,费用率{0:.1f}个点".format(float(res[28][i])))
            evaluate2.append(("毛利超高,毛利率{0:.1f}个点".format(float(value)),"better"))
        else:
            # print("毛利堪比卖白粉,费用率{0:.1f}个点".format(float(res[28][i])))
            evaluate2.append(("毛利堪比卖白粉,毛利率{0:.1f}个点".format(float(value)),"best"))
        # 营业费用率
        value = data[0]["盈利能力"]["营业费用率(%)"][0]*100
        if value < 5:
            # print("可能是营运超牛的公司!")
            evaluate2.append("可能是营运超牛的公司!")
        elif float(value) < 9:
            # print("生意又大又省钱!")
            evaluate2.append("生意又大又省钱!")
        elif float(value) < 13:
            # print("市场规模很大!")
            evaluate2.append("市场规模很大!")
        else:
            evaluate2.append(("费用率{}个点".format(round(value,0)),""))
        # 净利率
        value = data[0]["盈利能力"]["净利率(%)"][0] * 100
        if value < 0:
            # print("这个生意赚不到钱!")
            evaluate2.append(("这个生意赚不到钱!","worse"))
        elif value < 10:
            # print("税后利润一般,")
            evaluate2.append(("税后利润一般,","normal"))
        elif value < 20:
            # print("税后利润不错,")
            evaluate2.append(("税后利润不错,","good"))
        elif value < 30:
            # print("税后利润优异")
            evaluate2.append(("税后利润优异,","better"))
        else:
            # print("即使税后也非常赚钱,")
            evaluate2.append(("即使税后也非常赚钱,","best"))
        # ROE
        value = data[0]["盈利能力"]["ROE=净资产收益率(%)"][0] * 100
        if value < 0:
            print("股东在亏损!")
            evaluate2.append(("股东在亏损!","worse"))
        elif value < 10:
            print("收益率不高.")
            evaluate2.append(("收益率不高.",""))
        elif value < 15:
            print("还可以收益的.")
            evaluate2.append(("还可以的收益.","normal"))
        elif value < 20:
            print("不错的回报率.")
            evaluate2.append(("不错的回报率.","good"))
        elif value < 30:
            # print("能够打败巴菲特的回报率.")
            evaluate2.append(("能够打败巴菲特的回报率.","better"))
        elif value < 40:
            # print("很牛逼的回报率.")
            evaluate2.append(("很牛逼的回报率.","best"))
        # EPS
        value = data[0]["盈利能力"]["EPS=基本每股收益(元)"][0]
        if value < 0:
            # print("每一股在去年赔了{0:.2f}元钱".format(float(res[30][i])))
            evaluate2.append(("每一股在去年赔了{0:.2f}元钱".format(float(value)),""))
        else:
            # print("每一股在去年为公司赚了{0:.2f}元钱".format(float(res[30][i])))
            evaluate2.append(("每一股在去年为公司赚了{0:.2f}元钱".format(float(value)),"normal"))

        # 负债占资产比率
        evaluate3 = []
        value = data[0]["财务结构"]["资产负债率(%)"][0]*100
        if value < 30:
            # print("基本没什么杆杠，看来股东非常看好公司,")
            evaluate3.append(("基本没什么杆杠，看来股东非常看好公司,","best"))
        elif value < 40:
            # print("不用举债就能存活很好.")
            evaluate3.append(("不用举债就能存活很好,","better"))
        elif value < 60:
            # print("杆杠稳健,")
            evaluate3.append(("杆杠稳健,","normal"))
        elif value < 80:
            # print("杆杠偏高,")
            evaluate3.append(("杆杠偏高,",""))
        else:
            # print("杆杠过大,风险偏高,")
            evaluate3.append(("杆杠过大,风险偏高,","worse"))

        # 长期资金占不动及设备比例
        value = data[0]["财务结构"]["长期资金占重资产比率(%)"][0] * 100
        if value < 100:
            # print("长期资金来源缺乏.")
            evaluate3.append(("长期资金来源缺乏.",""))
        elif value < 200:
            # print("长期资金来源稳健.")
            evaluate3.append(("长期资金来源稳健.","good"))
        elif value < 300:
            # print("长期资金来源充足.")
            evaluate3.append(("长期资金来源充足.","better"))
        else:
            # print("长期资金源源不断!")
            evaluate3.append(("长期资金源源不断!","best"))
        # 速动比率
        evaluate4 = []
        value = data[0]["偿债能力"]["速动比率(%)"][0]
        if value < 100:
            if float(data[2]["资产部分"]["现金与约当现金(%)"][0] * 100) < 100:
                # print("短期外债偏高,公司目前有{0:d}成是现金资产.".format(math.floor(float(res[0][i]) / 10)))
                evaluate4.append(("短期外债偏高,公司目前有{0:d}成是现金资产.".format(math.floor(float(data[2]["资产部分"]["现金与约当现金(%)"][0] * 100) / 10)),"worse"))
            else:
                # print("如果发生债务纠纷,可能缺乏立即清偿能力.")
                evaluate4.append(("如果发生债务纠纷,可能缺乏立即清偿能力.",""))
        elif value < 150:
            # print("即使发生债务纠纷,公司清偿问题不大.")
            evaluate4.append(("即使发生债务纠纷,公司清偿问题不大.","better"))
        else:
            # print("即使发生债务纠纷,公司也能立即清偿.")
            evaluate4.append(("即使发生债务纠纷,公司也能立即清偿.","best"))

        # print(evaluate0)#现金流量：3
        # print(evaluate1)#运营能力：3
        # print(evaluate2)#盈利能力：5
        # print(evaluate3)#财务结构;2
        # print(evaluate4)#偿债能力:1

        html_text='''
        <html><head></head><body><table class="table table-sm">
    <!-- 现金流 !-->
    <tbody><tr>
  <th class="td_w">
    <a class="text-secondary"  target="_blank" rel="noopener noreferrer nofollow">现金流</a>
  </th>
  <td>
    <div class="cash_part">
      <span class="span_l {lev01}" title="" data-placement="top" data-toggle="tooltip" data-original-title="现金与约当现金比率(>25%)">
  {data01}
</span>

      <span class="span_m {lev02}" title="" data-placement="top" data-toggle="tooltip" data-original-title="现金流量比率(有任意项<0)">
  {data02}
</span>

      <span class="span_m {lev03}" title="" data-placement="top" data-toggle="tooltip" data-original-title="应收款项周转天数(15~80)">
  {data03}
</span>


    </div>
  </td>
</tr>

    <!-- 盈利能力 !-->
    <tr>
  <th class="td_w">
    <a class="text-secondary"  target="_blank" rel="noopener noreferrer nofollow">盈利能力</a>
  </th>
  <td>
    <div class="profit_part">

        <span class="span_l {lev21}" title="" data-placement="top" data-toggle="tooltip" data-original-title="毛利率(>70%)">
  {data21}
</span>

        <span class="span_m {lev22}" title="" data-placement="top" data-toggle="tooltip" data-original-title="费用率">
  {data22}
</span>


        <span class="span_l {lev23}" title="" data-placement="top" data-toggle="tooltip" data-original-title="净利率(<0)">
  {data23}
</span>


        <span class="span_m {lev24}" title="" data-placement="top" data-toggle="tooltip" data-original-title="ROE(<0)">
  {data24}
</span>

        <span class="span_m {lev25}" title="" data-placement="top" data-toggle="tooltip" data-original-title="eps < 0">
  {data25}
</span>


    </div>
  </td>
</tr>

    <!-- 营运能力 !-->
    <tr>
  <th class="td_w">
    <a class="text-secondary"  target="_blank" rel="noopener noreferrer nofollow">营运能力</a>
  </th>
  <td>
    <div class="management_part">
        <span class="span_l {lev11}" title="" data-placement="top" data-toggle="tooltip" data-original-title="总资产周转率(1.5~2)">
  {data11}
</span>

        <span class="span_m {lev12}" title="" data-placement="top" data-toggle="tooltip" data-original-title="现金与约当现金比率(>25%)">
  {data12}
</span>

        <span class="span_m {lev13}" title="" data-placement="top" data-toggle="tooltip" data-original-title="应收款项周转天数(15~80)">
  {data13}
</span>

<!--        <span class="span_s best" title="" data-placement="top" data-toggle="tooltip" data-original-title="应收款项周转天数(~)">-->
<!--  无需存货.-->
<!--</span>-->

<!--        <span class="span_s" title="" data-placement="top" data-toggle="tooltip" data-original-title="完整生意周期">-->
<!--  做一轮生意要 20 天.-->
<!--</span>-->

<!--        <span class="span_s best" title="" data-placement="top" data-toggle="tooltip" data-original-title="缺钱天数(0~15)">-->
<!--  缺钱天数为 -18 天,不需要资金就可以做生意哦.-->
<!--</span>-->


    </div>
  </td>
</tr>

    <!-- 财务结构 !-->
    <tr>
  <th class="td_w">
    <a class="text-secondary"  target="_blank" rel="noopener noreferrer nofollow">财务结构</a>
  </th>
  <td>

    <div class="structure_part">

      <span class="span_l {lev31}" title="" data-placement="top" data-toggle="tooltip" data-original-title="负债占资产比率(0%~30%)">
  {data31}
</span>

      <span class="span_m {lev32}" title="" data-placement="top" data-toggle="tooltip" data-original-title="长期资金占不动产及设备比率(>300%)">
  {data32}
</span>

    </div>
  </td>
</tr>

    <!-- 偿债能力 !-->
    <tr>
  <th class="td_w"><a class="text-secondary"  target="_blank" rel="noopener noreferrer nofollow">偿债能力</a></th>
  <td>
    <span class="span_m {lev41}" title="" data-placement="top" data-toggle="tooltip" data-original-title="速动比率(>150%)">
  {data41}
</span>

  </td>
</tr>

    <!-- 审计意见 !-->
  </tbody></table></body></html>'''.format(
            data01=evaluate0[0][0],data02=evaluate0[1][0],data03=evaluate0[2][0],
            data11=evaluate1[0][0], data12=evaluate1[1][0], data13=evaluate1[2][0],
            data21=evaluate2[0][0], data22=evaluate2[1][0], data23=evaluate2[2][0], data24=evaluate2[3][0], data25=evaluate2[4][0],
            data31=evaluate3[0][0], data32=evaluate3[1][0],
            data41=evaluate4[0][0],
            lev01=evaluate0[0][1], lev02=evaluate0[1][1], lev03=evaluate0[2][1],
            lev11=evaluate1[0][1], lev12=evaluate1[1][1], lev13=evaluate1[2][1],
            lev21=evaluate2[0][1], lev22=evaluate2[1][1], lev23=evaluate2[2][1], lev24=evaluate2[3][1], lev25=evaluate2[4][1],
            lev31=evaluate3[0][1], lev32=evaluate3[1][1],
            lev41=evaluate4[0][1],
        )

        with open('HTML/comment.html','w',encoding="utf8") as f:
            f.write(html_text)

    '''资产百分比、现金流_Html生成'''
    def zfb_maker(self):
        data = self.data_

        zc_percent=[]

        # print(data[1])
        for key in data[2]:
            # print(key)
            for index_list in data[2][key]:
                # print(index_list)
                # print(self.reverse2(data[2][key][index_list])[1:])
                zc_percent.extend(self.reverse2(data[2][key][index_list])[1:])

        cash_list=[]
        for key in data[1]:
            cash_list.extend(self.reverse3(data[1][key])[1:])
        all_li=[]
        all_li.extend(zc_percent)
        all_li.extend(cash_list)

        html_text='''
    <html><head></head><body><div class="col-md-12 col-lg-6 full-screen-col">
    <div class="shadow-box">
      <div class="sheet-header">
        <h3 class="sheet-header__title">资产负债比率(重要科目)</h3>
      </div>
      <div class="scroll-container">
        <div class="tab-content" id="albsTabContent">
          <!-- 年 -->
          <div class="tab-pane al-description fade active show" id="albs-yearly" role="tabpanel" aria-labelledby="albs-yearly-tab">
              <table class="table table-hover table-scroll">
    <thead>
      <tr>
        <th class="p-1 text-center">类别</th>
        <th class="p-1 text-left">比率(占总资产%)</th>
          <th class="p-1 text-center">2015</th>
          <th class="p-1 text-center">2016</th>
          <th class="p-1 text-center">2017</th>
          <th class="p-1 text-center">2018</th>
          <th class="p-1 text-center">2019-06</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th class="p-1 text-center" rowspan="7">
          <span class="bar total-assets-trends" style="display: none;">
            86301463422.77,112934538280.41,134610116875.08,159846674736.01,165121648977.73
          </span>

          <span>资产</span>
        </th>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">现金与约当现金(%)</a>
  </span>
</td>
  <td class="text-center p-1">

    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">59.2/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">65.3/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">70.1/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">70.0/100</span>
    <span>{}</span>
  </td>

      </tr>
      <tr>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">应收款项(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">9.9/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.7/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.9/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.4/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.4/100</span>
    <span>{}</span>
  </td>

      </tr>
      <tr>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">存货(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">20.9/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">18.3/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">16.4/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">14.7/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">14.5/100</span>
    <span>{}</span>
  </td>

      </tr>

      <tr>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">其他流动资产(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">--/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.2/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.0/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.1/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.0/100</span>
    <span>{}</span>
  </td>

      </tr>
      <tr>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">流动资产(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">75.3/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">79.9/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">83.4/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">86.2/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">86.3/100</span>
    <span>{}</span>
  </td>

      </tr>

      <tr>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">商誉(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">--/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">--/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">--/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">--/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">--/100</span>
    <span>{}</span>
  </td>

      </tr>
      <tr>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">非流动资产(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">24.7/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">20.1/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">16.6/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">13.8/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">13.7/100</span>
    <span>{}</span>
  </td>

      </tr>


      <tr class="tr-split-border">
        <th class="p-1 text-center" rowspan="3">
          <span class="bar total-debts-trends" style="display: none;">
            20067293001.48,37035995425.69,38590489400.0,42438186813.48,45514872823.37
          </span>

          <span>负债</span>
        </th>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">应付款项(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">1.0/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.9/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.7/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.7/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.8/100</span>
    <span>{}</span>
  </td>

      </tr>
      <tr>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">流动负债(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">23.2/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">32.8/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">28.7/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">26.5/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">27.5/100</span>
    <span>{}</span>
  </td>

      </tr>
      <tr>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">非流动负债(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.0/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.0/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.0/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">--/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">0.0/100</span>
    <span>{}</span>
  </td>

      </tr>
      <tr class="tr-split-border">
        <th class="p-1 text-center" rowspan="1">


          <span>权益</span>
        </th>
        <td class="text-left p-1">
  <span>
      <a class="wiki-terms">股东权益(%)</a>
  </span>
</td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">76.7/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">67.2/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">71.3/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">73.5/100</span>
    <span>{}</span>
  </td>
  <td class="text-center p-1">
    <span class="pie" style="display: none;">72.4/100</span>
    <span>{}</span>
  </td>

      </tr>
    </tbody>


  </table>
          </div>
          <!-- 季度 -->
          <!-- <div class="tab-pane al-description fade" id="albs-quarterly" role="tabpanel" aria-labelledby="albs-quarterly-tab"> -->
          <!-- </div> -->
        </div>
      </div>
    </div>

    <div class="shadow-box my-3">
      <div class="sheet-header">
        <h3 class="sheet-header__title">现金流量表</h3>
      </div>
      <div class="scroll-container">
        <div class="tab-content" id="alcfTabContent">
          <!-- 年 -->
          <div class="tab-pane al-description fade active show" id="alcf-yearly" role="tabpanel" aria-labelledby="alcf-alyearly-tab">
              <table class="table table-hover table-scroll">
    <thead>
      <tr>
        <th class="p-1">类别</th>
        <th class="p-1">
          </th><th class="p-1">
            2015
          </th>
          <th class="p-1">
            2016
          </th>
          <th class="p-1">
            2017
          </th>
          <th class="p-1">
            2018
          </th>
          <th class="p-1">
            近12个月
          </th>

      </tr>
    </thead>

    <tbody>
      <tr class="table-secondary">
        <td class="p-1">
  <span>
    期初现金
    <br>
    <span class="small">

    </span>
  </span>
</td>
<td class="p-1 trend">
  <span class="bar" style="display: none;">
    24997229197.76,34780485904.57,62794794812.99,74928080750.58,78068393291.94
  </span>
</td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>

      </tr>
      <tr>
        <td class="p-1">
  <span>
    <a class="wiki-terms">+ 营业活动现金流量</a>
    <br>
    <span class="small">
       (from 损益表)
    </span>
  </span>
</td>
<td class="p-1 trend">
  <span class="bar" style="display: none;">
    17436340141.72,37451249647.05,22153036084.13,41385234406.72,47737123590.96
  </span>
</td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>

      </tr>
      <tr>
        <td class="p-1">
  <span>
    <a class="wiki-terms">+ 投资活动现金流量</a>
    <br>
    <span class="small">
       (from 资产负债表左)
    </span>
  </span>
</td>
<td class="p-1 trend">
  <span class="bar" style="display: none;">
    -2048790264.59,-1102500804.2,-1120645214.6,-1628962704.56,-2025564645.33
  </span>
</td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>

      </tr>
      <tr>
        <td class="p-1">
  <span>
    <a class="wiki-terms">+ 融资活动现金流量</a>
    <br>
    <span class="small">
       (from 资产负债表右)
    </span>
  </span>
</td>
<td class="p-1 trend">
  <span class="bar" style="display: none;">
    -5588019638.61,-8334512252.23,-8899177880.8,-16441093160.06,-21618403387.19
  </span>
</td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>

      </tr>
      <tr class="table-secondary">
        <td class="p-1">
  <span>
    期末现金
    <br>
    <span class="small">

    </span>
  </span>
</td>
<td class="p-1 trend">
  <span class="bar" style="display: none;">
    34780485904.57,62794794812.99,74928080750.58,98243288299.54,102161564884.69
  </span>
</td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>

      </tr>
      <tr>
        <td class="p-1">
  <span>
    <a class="wiki-terms">自由现金流(FCF)</a>
    <br>
    <span class="small">

    </span>
  </span>
</td>
<td class="p-1 trend">
  <span class="bar" style="display: none;">
    15374869660.4,36432071510.13,21028018891.68,39778484180.44,45722221215.1
  </span>
</td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>
  <td class="p-1">
    {}
  </td>

      </tr>
    </tbody>
  </table>
          </div>
          <!-- 季度 -->
          <!-- <div class="tab-pane al-description fade" id="alcf-quarterly" role="tabpanel" aria-labelledby="alcf-alquarterly-tab"> -->
          <!-- </div> -->
        </div>
      </div>
    </div>
  </div></body></html>
    '''.format(*all_li)

        with open('HTML/zfb_index.html', 'w', encoding="utf8") as f:
            f.write(html_text)

if __name__ == '__main__':
    h=HtmlMaker("000502")