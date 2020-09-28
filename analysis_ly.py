# -*- coding: utf-8 -*-
# @Author : 李惠文
# @Email : 2689022897@qq.com
# @Time : 2020/9/19 10:37

from pylab import *

from utils.db_controller_mongo import MongoDB_Utils





'''
统计分析
'''
def show_products(products,title):
    '''
        根据列表，展示景点排行
    :param ticket_list: 列表
    :param title: 标题
    :return:
    '''

    # 设置字体
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    # x,y轴数据
    x_arr = []  # 景区名称
    y_arr = []  # 销量
    for i in products:
        x_arr.append(i['product']['name'])
        y_arr.append(i['saleCount'])

    """
    携程月销量排行榜
    """
    plt.bar(x_arr, y_arr, color='rgb')  # 指定color，不然所有的柱体都会是一个颜色
    plt.gcf().autofmt_xdate()  # 旋转x轴，避免重叠
    plt.xlabel(u'景点名称')  # x轴描述信息
    plt.ylabel(u'月销量')  # y轴描述信息

    plt.tick_params(labelsize=8)
    plt.title(title)  # 指定图表描述信息
    max_top=products[0]['saleCount']
    plt.ylim(0, max_top+(max_top*0.01))  # 指定Y轴的高度
    plt.savefig(title,dpi=300, bbox_inches = 'tight')  # 保存为图片
    plt.show()

if __name__ == '__main__':
    products= MongoDB_Utils.get_saleCount_china()
    show_products(products,'十一大家最想去哪玩预估统计表（全国）')

    products= MongoDB_Utils.get_saleCount_by_dom_city('广州')
    show_products(products,'十一大家最想去哪玩预估统计表（广州）')

    products= MongoDB_Utils.get_saleCount_by_dom_city('北京')
    show_products(products,'十一大家最想去哪玩预估统计表（北京）')

    products= MongoDB_Utils.get_saleCount_by_dom_city('上海')
    show_products(products,'十一大家最想去哪玩预估统计表（上海）')

    products= MongoDB_Utils.get_saleCount_by_dom_city('深圳')
    show_products(products,'十一大家最想去哪玩预估统计表（深圳）')

    products= MongoDB_Utils.get_saleCount_by_dom_city('武汉')
    show_products(products,'十一大家最想去哪玩预估统计表（武汉）')

    products= MongoDB_Utils.get_saleCount_by_dom_city('肇庆')
    show_products(products,'十一大家最想去哪玩预估统计表（肇庆）')

    products= MongoDB_Utils.get_saleCount_abroad()
    show_products(products,'十一大家最想去哪玩预估统计表（国外）')