# -*- coding: utf-8 -*-
# @Author : 李惠文
# @Email : 2689022897@qq.com
# @Time : 2020/9/21 17:08
import json

import requests

from utils.db_controller_mongo import MongoDB_Utils

'''
    城市爬虫
'''


class CitySpider:
    def get_cityList(self):
        '''
        接口爬取城市
        :return:
        '''
        req_headers = {
            'Connection': 'keep-alive',
            'Content-Length': '2157',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': '_ga=GA1.2.1336207059.1596010111; MKT_CKID=1596010110605.kd1op.71ns; _RSG=kb47gmK6Fo83HM8I2JS_49; _RDG=28e3cfac99ded9234b014391878bc6aa64; _RGUID=8c8f194c-2a1c-496e-913f-713092216443; _abtest_userid=4451d590-caf5-47f1-aa43-486138fd21cd; nfes_isSupportWebP=1; _RF1=183.234.184.72; hoteluuid=UMQpVH3pA5TOVDXF; _gid=GA1.2.1422206227.1600678127; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&createtime=1600678127&Expires=1601282927377; MKT_CKID_LMT=1600678127388; MKT_Pagesource=PC; GUID=09031010212176594427; StartCity_Pkg=PkgStartCity=32; appFloatCnt=5; _jzqco=%7C%7C%7C%7C1600678127944%7C1.602522804.1596010110616.1600678534886.1600678743080.1600678534886.1600678743080.undefined.0.0.42.42; __zpspc=9.14.1600678127.1600678743.7%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _bfi=p1%3D290510%26p2%3D290510%26v1%3D109%26v2%3D108; U_TICKET_SELECTED_DISTRICT_CITY=%7B%22value%22%3A%7B%22districtid%22%3A%22152%22%2C%22districtname%22%3A%22%E5%B9%BF%E5%B7%9E%22%2C%22isOversea%22%3Anull%7D%2C%22createTime%22%3A1600683669950%2C%22updateDate%22%3A1600683669950%7D; _bfa=1.1596010105844.227khb.1.1600070314807.1600683670272.26.117.10650038368',
        }
        req_json = {"head": {
            "pageInfo": {"page": "", "hybrid": "", "prevpage": "", "sid": "", "pvid": "", "clientcode": "", "vid": ""},
            "cid": "09031010212176594427", "vid": "1596010105844.227khb",
            "union": {"sid": "130026", "aid": "4897", "ouid": ""},
            "url": "https://huodong.ctrip.com/things-to-do/list?pagetype=city&citytype=dt&id=152&name=%E5%B9%BF%E5%B7%9E&pshowcode=Ticket2",
            "referrer": "https://huodong.ctrip.com/things-to-do/list?pagetype=city&citytype=dt&id=1&name=%E5%8C%97%E4%BA%AC&pshowcode=Ticket2",
            "language": "zh-CN", "currency": "CNY",
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "cookie": "_ga=GA1.2.1336207059.1596010111; MKT_CKID=1596010110605.kd1op.71ns; _RSG=kb47gmK6Fo83HM8I2JS_49; _RDG=28e3cfac99ded9234b014391878bc6aa64; _RGUID=8c8f194c-2a1c-496e-913f-713092216443; _abtest_userid=4451d590-caf5-47f1-aa43-486138fd21cd; nfes_isSupportWebP=1; _RF1=183.234.184.72; _gid=GA1.2.1422206227.1600678127; Session=smartlinkcode=U130026&smartlinklanguage=zh&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=; Union=AllianceID=4897&SID=130026&OUID=&createtime=1600678127&Expires=1601282927377; MKT_CKID_LMT=1600678127388; MKT_Pagesource=PC; GUID=09031010212176594427; StartCity_Pkg=PkgStartCity=32; appFloatCnt=5; _jzqco=%7C%7C%7C%7C1600678127944%7C1.602522804.1596010110616.1600678534886.1600678743080.1600678534886.1600678743080.undefined.0.0.42.42; __zpspc=9.14.1600678127.1600678743.7%232%7Cwww.baidu.com%7C%7C%7C%7C%23; _bfi=p1%3D290510%26p2%3D290510%26v1%3D109%26v2%3D108; U_TICKET_SELECTED_DISTRICT_CITY=%7B%22value%22%3A%7B%22districtid%22%3A%221%22%2C%22districtname%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22isOversea%22%3Anull%7D%2C%22createTime%22%3A1600683626334%2C%22updateDate%22%3A1600683626334%7D; _gat=1; _bfa=1.1596010105844.227khb.1.1600070314807.1600683669166.26.117.10650038368",
            "isMiniProgram": "false", "width": 1920, "height": 721, "traceId": "16006836695149931",
            "offset": {"height": 721, "width": 1247}, "isBot": "false", "isInApp": "false", "platform": "Online",
            "enviroment": "PROD", "channel": "ctrip", "log_version": "", "syscode": "09", "pageId": "10650038368",
            "netState": "4G", "randomId": 7}, "source": 0, "cityId": "152", "type": 0}
        req_url = 'https://m.ctrip.com/restapi/soa2/14580/json/cityList'
        res = requests.post(req_url, json=req_json, headers=req_headers, verify=False)

        data = json.loads(res.text).get("data", {})
        # 国内
        self.get_city_by_data(data.get("domesticcity"), "domesticcity")
        # 国外
        self.get_city_by_data(data.get("overseascity"), "overseascity")

    def get_city_by_data(self, domesticcity, city_type):
        '''
        获取城市后，保存数据
        :param domesticcity:
        :param city_type:
        :return:
        '''
        recommendcities = domesticcity.get("recommendcities")
        for i in recommendcities:
            item = {"districtId": i.get("id"), "name": i.get("name")}
            if ("domesticcity" == city_type):
                MongoDB_Utils.replace_domesticcity(item)
            else:
                MongoDB_Utils.replace_overseascity(item)
            print(f"插入数据成功：" + str(item))
        cities = domesticcity.get("cities")
        for city in cities:
            for i in city.get("cities"):
                item = {"districtId": i.get("id"), "name": i.get("name")}
                if ("domesticcity" == city_type):
                    MongoDB_Utils.replace_domesticcity(item)
                else:
                    MongoDB_Utils.replace_overseascity(item)
                print(f"插入数据成功：" + str(item))


if __name__ == '__main__':
    ctripSpider = CitySpider()
    ctripSpider.get_cityList()
