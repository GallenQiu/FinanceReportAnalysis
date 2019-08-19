# -*- coding : utf-8 -*- #
import codecs
import numpy as np
__author__ = "Gallen_qiu"
from PyQt5.Qt import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from regionRp import Report_dealer
from indexData import Report_index
from html_maker import HtmlMaker
import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)

'''导入所需要的包'''

class Window(QTabWidget):

    def __init__(self,scode):
        super().__init__()
        self.scode=scode
        #生成html
        HtmlMaker(self.scode)


        # 获取数据
        self.data = {}
        self.data1 = {}
        self.getData1()
        self.getData2()
        self.score_ = {}  # cbs评分
        self.score()


        self.setWindowTitle("主窗口")
        self.resize(500, 500)
        self.move(400, 200)  # 在显示器上移动
        self.setTabPosition(QTabWidget.South)
        tabbar=QTabBar()
        tabbar.setShape(QTabBar.Shape(5))
        # tabbar.setStyleSheet("color:cyan;")
        self.setTabBar(tabbar)

        #最大化
        self.showMaximized()

        # 创建3个选项卡小控件窗口
        self.tab1 = QWidget()
        # self.tab1.setStyleSheet("background-color:cyan;")
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # 将三个选项卡添加到顶层窗口中
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.setTabText(0, '主页面')
        self.setTabText(1, '杜邦分析')
        self.setTabText(2, '财报分析')

        #调用子控件
        self.setup_tab1()
        self.setup_tab3()


    '''获取原始报表数据集合'''
    def getData1(self):
        Ri=Report_dealer(self.scode)

        self.data=Ri.scheduler()[0]
        '''
        return self.balanceS ,self.incomeS,self.cashFlowS,self.last12
        '''

    '''获取重要指标数据集合'''
    def getData2(self):
        Ri=Report_index(self.scode)

        self.data1=Ri.scheduler()
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

    '''各项能力的评分'''
    def score(self):
        '''
        "现金占比权重（去年）30%
        "经营能力权重（去年）30%
        "获利能力权重（去年）20%
        "财务结构权重（去年）10%
        "偿债能力权重（去年）10%
        '''
        # 求股票的气
        # 现金占比
            # 现金与约当现金占比->7分
        score={"现金占比":0,"运营能力":0,"盈利能力":0,"财务结构":0,"偿债能力":0,"Total":0}

        data = self.data1
        value = data[2]["资产部分"]["现金与约当现金(%)"][0]*100
        if value >= 10:
            score["现金占比"] += 7
        else:
            score["现金占比"] += value * 7 / 25
            # 求股票的应收款周转天数->2分
        value = data[0]["运营能力"]["应收款项周转天数(天)"][0]
        if value <= 15:
            score["现金占比"] += 2
        else:
            score["现金占比"] +=2 * 15 / value
            # 现金的三大比例->1分
        # i = 0
        value=data[0]["现金流量"]["现金流量比率(%)"][0]*100
        if value >= 100:  # 现金流量比率
            i = 1
        else:
            i = value / 100
        # if data[35, j] >= 100:  # 现金允当比例
        #     i = i + 1
        # else:
        #     i = (data[35, j] / 100) + i
        # if data[36, j] >= 10:  # 现金在投资比例
        #     i = i + 1
        # else:
        #     i = i + (data[36, j] / 100)
        # score[0, j] = score[0, j] + i / 3
        score["现金占比"]=score["现金占比"]+i/1
        if score["现金占比"] == -np.inf:
            score["现金占比"] = 0

        # 经营能力
            # 资产周转率->5分
        value = data[0]["运营能力"]["总资产周转率(次/年)"][0]
        if value < 1:
            score["运营能力"] = score["现金占比"]#????
        else:
            score["运营能力"] += 5

            value = data[0]["运营能力"]["存货周转天数(天)"][0]
            if value <= 30:  # 存货周转天数->2.5
                score["运营能力"] += 2.5
            else:
                score["运营能力"] += 2.5 * 30 / value

            value = data[0]["运营能力"]["应收款项周转天数(天)"][0]
            if value <= 90:  # 应收款项周转天数->2.5
                score["运营能力"]  += 2.5
            else:
                score["运营能力"]  += 2.5 * 60 / value

        # 获利能力
            # 毛利率->2
        value = data[0]["盈利能力"]["毛利率(%)"][0]*100
        if value >= 32:
            score["盈利能力"] += 2
        else:
            score["盈利能力"] += 2 * value / 30
            # 营业利益率->2
        value = data[0]["盈利能力"]["营业利润率(%)"][0] * 100
        if value >= 10:
            score["盈利能力"] += 2
        else:
            score["盈利能力"] += 2 * value / 10
            # 经营安全边界->2
        value = data[0]["盈利能力"]["经营安全边际率(%)"][0] * 100
        if value >= 60:
            score["盈利能力"] += 2
        else:
            score["盈利能力"] += 2 * value / 60
            # 净利率->1
        value = data[0]["盈利能力"]["净利率(%)"][0] * 100
        if value >= 2:
            score["盈利能力"] += 1
        else:
            score["盈利能力"] += value / 2
            # EPS->1
        value = data[0]["盈利能力"]["EPS=基本每股收益(元)"][0]
        if value >= 1:
            score["盈利能力"] += 1
        else:
            score["盈利能力"] +=value
        value = data[0]["盈利能力"]["ROE=净资产收益率(%)"][0] * 100
        if value >= 20:  # ROE
            score["盈利能力"] += 1
        else:
            score["盈利能力"] += value / 20

        if score["盈利能力"] == -np.inf:
            score["盈利能力"] = 0

        # 财务结构
            # 负债占资产比例->5
        value = data[0]["财务结构"]["资产负债率(%)"][0] * 100
        if (value >= 25) and (value <= 70):
            score["财务结构"] += 5
        elif value < 25:
            score["财务结构"] += 5 * value / 25
        else:
            pass
            # 长期资金占不动产比率->5
        value = data[0]["财务结构"]["长期资金占重资产比率(%)"][0] * 100
        if value >= 100:
            score["财务结构"] += 5
        else:
            score["财务结构"] += 5 * value / 100

        # 偿债能力
            # 流动比率->5
        value = data[0]["偿债能力"]["流动比率(%)"][0] * 100
        if value >= 300:
            score["偿债能力"] += 5
        else:
            score["偿债能力"] += 5 * value / 300
            # 速动比率
        value = data[0]["偿债能力"]["速动比率(%)"][0] * 100
        if value >= 150:
            score["偿债能力"] += 5
        else:
            score["偿债能力"] += 5 * value / 100

        score["Total"] = score["现金占比"] * 3 + score["运营能力"] * 3 + score["盈利能力"] * 2 + score["偿债能力"] + score["财务结构"]
        self.score_=score

    '''第一个页面：主页面展示'''
    def setup_tab1(self):
        self.layout00 = QVBoxLayout()
        # self.label0_1 = QWidget()
        self.setup_label0()

        self.layout01=QHBoxLayout()
        self.setup_label1()
        '''第一个布局'''
        layout0=QHBoxLayout()
        layout0.addLayout(self.layout00, 1)
        layout0.addLayout(self.layout01, 3)
        # layout0.addWidget(label0_3, 1)
        # layout0.addWidget(label0_4, 1)
        # layout0.addWidget(label0_5, 1)
        # layout0.addWidget(label0_6, 1)
        # layout0.addWidget(label0_7, 1)


        # label1_1 = QLabel()
        # label1_1.setStyleSheet("border;")
        label1_1 = Comment()
        label1_1.comment()
        label1_1.setContentsMargins(0, 0, 0, 0)
        '''重要财务比率'''
        label1_2 = Rate_index()
        label1_2.rate_index()
        label1_2.setContentsMargins(0,0,0,0)

        label1_3_1 = Rate_index_zfb()
        label1_3_1.rate_index()
        label1_3_1.setContentsMargins(0, 0, 0, 0)


        '''第二个布局'''
        layout1 = QHBoxLayout()
        layout1.addWidget(label1_1, 4)
        layout1.addWidget(label1_2, 7)
        layout1.addWidget(label1_3_1,5)
        '''创建布局管理器'''
        layout_main = QVBoxLayout()  # 垂直排列布局
        '''添加layout'''
        layout_main.addSpacing(50)
        layout_main.addLayout(layout0,10)
        layout_main.addLayout(layout1,35)
        '''插入空白'''
        # layout.insertSpacing(3,30)
        '''布局管理器设置'''
        # 外边框
        layout_main.setContentsMargins(2, 2, 2, 2)  # 左，上，右，下
        # 内边框
        layout_main.setSpacing(2)

        self.tab1.setLayout(layout_main)

        # self.tab1.setLayoutDirection(Qt.LeftToRight)  # Qt.RightToLeft Qt.LayoutDirectionAuto
    '''第一个页面：上半部分布局-左'''
    def setup_label0(self):

        info=self.data
        l_Qlabel00=QLabel()
        l_Qlabel00.setText('     ')  # 股票名称
        l_Qlabel00.setStyleSheet("font-size : 50px;font-family : fantasy;font-variant : normal;font-weight : 600;font-style : normal;background-color:#5F9EA0;")
        l_Qlabel0 = QLabel()
        l_Qlabel0.setText('    '+info["SECNAME"])#股票名称
        l_Qlabel0.setStyleSheet("font-size : 50px;font-family : fantasy;font-variant : normal;font-weight : 600;font-style : normal;background-color:#B0E0E6;")
        l_Qlabel1 = QLabel()
        l_Qlabel1.setText('        '+info["SECCODE"])  # 股票代码
        l_Qlabel1.setStyleSheet("font-size : 38px;background-color:#B0E0E6;")

        l_Qlabel2 = QLabel()

        l_Qlabel2.setText('    行业分类：{}-{}-{}'.format(info["f_kind"],info["s_kind"],info["t_kind"]))  # 股票代码
        l_Qlabel2.setStyleSheet("font-size : 22px;background-color:#B0E0E6;")
        # self.layout00.addStretch(1)
        self.layout00.addWidget(l_Qlabel00, 1)
        self.layout00.addWidget(l_Qlabel0,1)
        self.layout00.addWidget(l_Qlabel1,1)
        self.layout00.addWidget(l_Qlabel2,1)
        self.layout00.setContentsMargins(0,0,0,0)
        self.layout00.setSpacing(0)
        color_label = QLabel()
        color_label.setStyleSheet("background-color:#B0E0E6;")

    '''第一个页面：上半部分布局-右'''
    def setup_label1(self):
        score=self.score_

        label0 = QLabel("   现金流量(30%)")
        label0.setStyleSheet("font-size : 22px;")
        # label0.setContentsMargins()
        label1 = QLabel(' {}/100.00'.format(round(score["现金占比"]*10,2)))
        label1.setStyleSheet("font-size : 30px;border:1px solid; border-bottom-color : #B0C4DE;border-top-color : #FFFFFF;border-left-color : #FFFFFF;border-right-color : #FFFFFF;")

        box0=QVBoxLayout()
        box0.addStretch(1)
        box0.addWidget(label0, 2)
        box0.addWidget(label1, 4)

        label0 = QLabel("   运营能力(30%)")
        label0.setStyleSheet("font-size : 22px;")
        label1 = QLabel(' {}/100.00'.format(round(score["运营能力"] * 10, 2)))
        label1.setStyleSheet("font-size : 30px;border:1px solid; border-bottom-color : #B0C4DE;border-top-color : #FFFFFF;border-left-color : #FFFFFF;border-right-color : #FFFFFF;")

        box1 = QVBoxLayout()
        box1.addStretch(1)
        box1.addWidget(label0, 2)
        box1.addWidget(label1, 4)

        label0 = QLabel("   盈利能力(20%)")
        label0.setStyleSheet("font-size : 22px;")
        label1 = QLabel('  {}/100.00'.format(round(score["盈利能力"] * 10, 2)))
        label1.setStyleSheet("font-size : 30px;border:1px solid; border-bottom-color : #B0C4DE;border-top-color : #FFFFFF;border-left-color : #FFFFFF;border-right-color : #FFFFFF;")

        box2 = QVBoxLayout()
        box2.addStretch(1)
        box2.addWidget(label0, 2)
        box2.addWidget(label1, 4)

        label0 = QLabel("   财务结构(10%)")
        label0.setStyleSheet("font-size : 22px;")
        label1 = QLabel(' {}/100.00'.format(round(float('%.3f' % score["财务结构"]) * 10, 3)))
        label1.setStyleSheet("font-size :30px;border:1px solid; border-bottom-color : #B0C4DE;border-top-color : #FFFFFF;border-left-color : #FFFFFF;border-right-color : #FFFFFF;")

        box3 = QVBoxLayout()
        box3.addStretch(1)
        box3.addWidget(label0, 2)
        box3.addWidget(label1, 4)

        label0 = QLabel("    偿债能力(10%)")
        label0.setStyleSheet("font-size : 22px;")
        label1 = QLabel('  {}/100.00'.format(round(score["偿债能力"] * 10, 2)))
        label1.setStyleSheet("font-size : 30px;border:1px solid; border-bottom-color : #B0C4DE;border-top-color : #FFFFFF;border-left-color : #FFFFFF;border-right-color : #FFFFFF;")

        box4 = QVBoxLayout()
        box4.addStretch(1)
        box4.addWidget(label0, 2)
        box4.addWidget(label1, 4)

        label0 = QLabel("\n           加权评分")
        label0.setStyleSheet("background-color:#5F9EA0;font-size : 22px;font-weight : bold;")

        label1 = QLabel('  {}/100.00'.format(round(score["Total"], 2)))
        label1.setStyleSheet("background-color:#B0E0E6;font-size : 40px;font-weight : 900;border:1px ; border-bottom-color : #B0C4DE;border-top-color : #FFFFFF;border-left-color : #FFFFFF;border-right-color : #FFFFFF;")
        # label1.setMargin(100)
        box5 = QVBoxLayout()
        box5.setSpacing(0)

        # box5.addStretch(1)
        box5.addWidget(label0,1)
        box5.addWidget(label1,3)
        self.layout01.addLayout(box0,2)
        self.layout01.addLayout(box1,2)
        self.layout01.addLayout(box2,2)
        self.layout01.addLayout(box3,2)
        self.layout01.addLayout(box4,2)
        self.layout01.addLayout(box5,3)




    '''第三个页面：财报分析展示'''
    def setup_tab3(self):
        layout=QVBoxLayout()

        self.view = QWebEngineView()

        layout.addWidget(self.view,10)
        with codecs.open("cb.html", "r", "utf-8") as f:
            html = f.read()
        self.view.setHtml(html)
        # self.time = QTimer()

        self.tab3.setLayout(layout)

'''重要财务比率窗口'''
class Rate_index(QWidget):

   def rate_index(self):
        layout = QVBoxLayout()

        view = QWebEngineView()
        # layout.addStretch(1)
        layout.addWidget(view,24)

        with codecs.open("HTML/rate_index.html", "r", "utf-8") as f:
           html = f.read()
        view.setHtml(html)
        self.setLayout(layout)

        self.loadCSS(view, "HTML/rate_index.css", "alkeyTabContent")


   def loadCSS(self,view, path, name):
       path = QFile(path)
       if not path.open(QFile.ReadOnly | QFile.Text):
           return
       css = path.readAll().data().decode("utf-8")
       SCRIPT = """
        (function() {
        css = document.createElement('style');
        css.type = 'text/css';
        css.id = "%s";
        document.head.appendChild(css);
        css.innerText = `%s`;
        })()
        """ % (name, css)

       script = QWebEngineScript()
       view.page().runJavaScript(SCRIPT,QWebEngineScript.ApplicationWorld)
       script.setName(name)
       script.setSourceCode(SCRIPT)
       script.setInjectionPoint(QWebEngineScript.DocumentReady)
       script.setRunsOnSubFrames(True)
       script.setWorldId(QWebEngineScript.ApplicationWorld)
       view.page().scripts().insert(script)

'''资产负债表百分比比率窗口、现金流量比率窗口'''
class Rate_index_zfb(QWidget):

   def rate_index(self):
       layout = QVBoxLayout()

       view = QWebEngineView()
       layout.addWidget(view)
       with codecs.open("HTML/zfb_index.html", "r", "utf-8") as f:
           html = f.read()
       view.setHtml(html)
       self.setLayout(layout)
       self.loadCSS(view, "HTML/zfb_index.css", "albsTabContent")

   def loadCSS(self,view, path, name):
       path = QFile(path)
       if not path.open(QFile.ReadOnly | QFile.Text):
           return
       css = path.readAll().data().decode("utf-8")
       SCRIPT = """
        (function() {
        css = document.createElement('style');
        css.type = 'text/css';
        css.id = "%s";
        document.head.appendChild(css);
        css.innerText = `%s`;
        })()
        """ % (name, css)

       script = QWebEngineScript()
       view.page().runJavaScript(SCRIPT,QWebEngineScript.ApplicationWorld)
       script.setName(name)
       script.setSourceCode(SCRIPT)
       script.setInjectionPoint(QWebEngineScript.DocumentReady)
       script.setRunsOnSubFrames(True)
       script.setWorldId(QWebEngineScript.ApplicationWorld)
       view.page().scripts().insert(script)

'''评论窗口'''
class Comment(QWidget):
    def comment(self):
        layout = QVBoxLayout()
        view = QWebEngineView()
        layout.addStretch(1)
        layout.addWidget(view, 24)
        with codecs.open("HTML/comment.html", "r", "utf-8") as f:
            html = f.read()
        view.setHtml(html)
        self.setLayout(layout)

        self.loadCSS(view, "HTML/comment.css", "alkeyTabContent")

    def loadCSS(self, view, path, name):
        path = QFile(path)
        if not path.open(QFile.ReadOnly | QFile.Text):
            return
        css = path.readAll().data().decode("utf-8")
        SCRIPT = """
         (function() {
         css = document.createElement('style');
         css.type = 'text/css';
         css.id = "%s";
         document.head.appendChild(css);
         css.innerText = `%s`;
         })()
         """ % (name, css)

        script = QWebEngineScript()
        view.page().runJavaScript(SCRIPT, QWebEngineScript.ApplicationWorld)
        script.setName(name)
        script.setSourceCode(SCRIPT)
        script.setInjectionPoint(QWebEngineScript.DocumentReady)
        script.setRunsOnSubFrames(True)
        script.setWorldId(QWebEngineScript.ApplicationWorld)
        view.page().scripts().insert(script)



if __name__ == '__main__':

    app=QApplication(sys.argv)##############创建程序，接收外部参数
    window=Window()#window是第一个控件，也是顶层控件；会自动添加窗口上沿（缩小、关闭、title）
    window.show()
    sys.exit(app.exec_())####################结束程序，返回结束参数；app.exec_()进入消息循环