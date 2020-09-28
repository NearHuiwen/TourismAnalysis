# -*- coding: utf-8 -*-
# @Author : 李惠文
# @Email : 2689022897@qq.com
# @Time : 2020/9/19 9:57
import copy
import json
import queue
import re
import time
from threading import Lock

import requests

from utils.db_controller_mongo import MongoDB_Utils

from utils.user_agent_utils import UA_Utils

'''
    ‘携程旅行’爬虫，requests版本
'''


class ProductSp():

    def __init__(self):
        # 自定义头文件
        self.headers = {
            'Connection': 'keep-alive',
            'Content-Length': '554',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': '_ga=GA1.2.1336207059.1596010111; MKT_CKID=1596010110605.kd1op.71ns; _RSG=kb47gmK6Fo83HM8I2JS_49; _RDG=28e3cfac99ded9234b014391878bc6aa64; _RGUID=8c8f194c-2a1c-496e-913f-713092216443; _abtest_userid=4451d590-caf5-47f1-aa43-486138fd21cd; nfes_isSupportWebP=1; _RF1=183.234.184.72; hoteluuid=UMQpVH3pA5TOVDXF; _gid=GA1.2.1422206227.1600678127; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&createtime=1600678127&Expires=1601282927377; MKT_CKID_LMT=1600678127388; MKT_Pagesource=PC; GUID=09031010212176594427; StartCity_Pkg=PkgStartCity=32; appFloatCnt=5; _jzqco=%7C%7C%7C%7C1600678127944%7C1.602522804.1596010110616.1600678534886.1600678743080.1600678534886.1600678743080.undefined.0.0.42.42; __zpspc=9.14.1600678127.1600678743.7%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _bfi=p1%3D290510%26p2%3D290510%26v1%3D109%26v2%3D108; U_TICKET_SELECTED_DISTRICT_CITY=%7B%22value%22%3A%7B%22districtid%22%3A%22152%22%2C%22districtname%22%3A%22%E5%B9%BF%E5%B7%9E%22%2C%22isOversea%22%3Anull%7D%2C%22createTime%22%3A1600679160478%2C%22updateDate%22%3A1600679160478%7D; _bfa=1.1596010105844.227khb.1.1600070314807.1600679160673.25.114.10650038368',
        }

        # useragent工具类
        self.ua_utils = UA_Utils()

        # 加载延时（主线程堵塞），防止被封IP，无法爬虫（单位：秒）
        self.LOAD_DELAY = 2

        # 请求失败后睡眠多久，重新请求
        self.LOAD_FAIL_DELAY = 10

        # 爬取总数
        self.totalCount = 0
        self.mutex = Lock()  # 线程锁保证线程安全

    def add_totalCount(self, count):
        '''
        添加总数
        :param count:
        :return:
        '''
        self.mutex.acquire()
        self.totalCount += count
        self.mutex.release()

    def executeTasksToClimb(self, q, keyword, districtId, city_type="domesticcity"):
        '''执行爬虫任务
        :param q: 队列
        :param keyword: 城市
        :param city_type: 城市类型（国内/国外）
        :return:
        '''
        pageIndex = q.get()
        print(f"分配爬虫任务，准备爬取[{keyword}]第{pageIndex}页数据\n")
        res_json = self.getRequestsTask(districtId, pageIndex)
        q.task_done()
        print(
            f'执行保存数据任务，正在保存[{keyword}]第[{pageIndex}]页数据')
        self.saveProductList(keyword, res_json.get("data", {}).get("productList", []), city_type)

    def assignTasksToClimb(self, sumPage, keyword, city_type="domesticcity"):
        '''分配爬虫任务
        :param sumPage: 总页数
        :param keyword: 城市
        :param city_type: 城市类型（国内/国外）
        :return:
        '''
        if ("domesticcity" == city_type):
            districtId = MongoDB_Utils.get_domesticcity_by_city(keyword).get("districtId")
        else:
            districtId = MongoDB_Utils.get_overseascity_by_city(keyword).get("districtId")
        q = queue.Queue()
        for i in range(sumPage):
            q.put(i + 1)
            self.executeTasksToClimb(q, keyword, districtId, city_type)
            if (self.LOAD_DELAY > 0):
                print(f'睡眠[{self.LOAD_DELAY}]秒\n')
                time.sleep(self.LOAD_DELAY)
        q.join()
        print('执行爬虫任务完成\n')
        print(f"城市[{keyword}]已爬取共[{self.totalCount}]条数据\n")

    def getRequestsTask(self, districtId, pageIndex):
        '''根据keyword, pageIndex构建requests任务
        :param keyword: 城市
        :param pageIndex: 页码
        :return:
        '''
        req_url = 'https://m.ctrip.com/restapi/soa2/14580/json/ProductSearch'
        req_headers = copy.deepcopy(self.headers)
        req_headers["User-Agent"] = self.ua_utils.getUaByPoll()

        req_json = {"head": {"cid": "09031010212176594427", "syscode": "999"}, "ver": "8.3.2", "debug": "false",
                    "pageid": "10650038368", "contentType": "json",
                    "clientInfo": {"pageId": "10650038368", "platformId": "null", "crnVersion": "2020-09-03 17:22:34",
                                   "location": {"lat": "", "lon": "", "cityId": "", "locatedCityId": "",
                                                "districtId": str(districtId), "locatedDistrictId": "", "cityType": ""},
                                   "locale": "zh-CN", "currency": "CNY"}, "bizLineType": 1, "pshowcode": "Ticket2",
                    "needUpStream": "false", "pidx": pageIndex, "sort": "5", "qsids": "", "psize": 20,
                    "imgsize": "C_568_320",
                    "extras": [], "traceid": "7704c7c6-5408-c682-a034-1600683dd781"}

        print(f'执行爬取数据任务，正在爬取第{pageIndex}页数据\n')
        try:
            return json.loads(requests.post(req_url, json=req_json, headers=req_headers, verify=False).text)
        except:
            if (self.LOAD_FAIL_DELAY > 0):
                print(f"加载失败,请求频率过高,睡眠[{self.LOAD_FAIL_DELAY}]秒后重新请求\n")
                time.sleep(self.LOAD_FAIL_DELAY)
            return self.getRequestsTask(districtId, pageIndex)

    def saveProductList(self, keyword, productList, city_type="domesticcity"):
        '''结果列表，保存数据
       :param keyword:城市
       :param productList: 返回列表
       :param city_type: 城市类型（国内/国外）
       :return:
       '''
        for product in productList:
            productId = product.get("id", 0)  # 景区ID
            name = product.get("name", "")  # 景区名称

            productDesc = product.get("productDesc", "0")
            saleCount = int(re.findall(r"\d+", productDesc)[0])
            if ("K" in productDesc):
                saleCount = saleCount * 1000
            item = {
                "productId": productId,
                "keyword": keyword,
                "product": product,
                "saleCount": saleCount
            }

            if ("domesticcity" == city_type):
                MongoDB_Utils.replace_dom_product(item)
            else:
                MongoDB_Utils.replace_ove_product(item)

            self.add_totalCount(1)
            print(f"获取ID=[{productId}]，景区名称=[{name}]的信息成功，目前城市[{keyword}]已爬取共[{self.totalCount}]条数据\n")
        return True


if __name__ == '__main__':
    productSp = ProductSp()
    citys = set([
        "北京",
        "上海",
        "深圳",
        "成都",
        "三亚",
        "西安",
        "厦门",
        "重庆",
        "杭州",
        "广州",
        "哈尔滨",
        "苏州",
        "武汉",
        "大连",
        "南京",
        "丽江",
        "肇庆",
        "香港"])
    # 国内
    for i in citys:
        productSp.assignTasksToClimb(3, i,"domesticcity")

    citys = set([
        "普吉岛",
        "曼谷",
        "清迈",
        "巴厘岛",
        "东京",
        "沙巴",
        "芭堤雅",
        "大阪",
        "芽庄",
        "新加坡",
        "迪拜",
        "墨尔本",
        "吉隆坡",
        "仙本那", ])
    # 国外
    for i in citys:
        productSp.assignTasksToClimb(3, i, "overseascity")
