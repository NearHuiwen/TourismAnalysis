# -*- coding: utf-8 -*-
# @Author : 李惠文
# @Email : 2689022897@qq.com
# @Time : 2020/8/6 17:47


from utils.db_manager_mongo import Operation_Mongo

"""
    MongoDB工具类
"""


class MongoDB_Utils:
    @staticmethod
    def replace_dom_product(item):
        '''
        保存国内景点信息到MongoDB
        :param item:
        :return:
        '''
        with Operation_Mongo() as om:
            om.replace_collection('dom_products', {'productId': item.get("productId", 0)}, item)
            return True
        return False

    @staticmethod
    def replace_ove_product(item):
        '''
        保存国外景点信息到MongoDB
        :param item:
        :return:
        '''
        with Operation_Mongo() as om:
            om.replace_collection('ove_products', {'productId': item.get("productId", 0)}, item)
            return True
        return False

    @staticmethod
    def replace_overseascity(item):
        '''
        保存国外城市信息到MongoDB
        :param item:
        :return:
        '''
        with Operation_Mongo() as om:
            om.replace_collection('overseascities', {'districtId': item.get("districtId", 0)}, item)
            return True
        return False

    @staticmethod
    def get_domesticcity_by_city(city):
        '''
        根据城市名，获取国内景点id
        :param city: 城市
        :return:
        '''
        with Operation_Mongo() as om:
            data = om.select_one_collection(collection_name='domesticcities', search_col={'name': city})
            return data
        return False

    @staticmethod
    def get_overseascity_by_city(city):
        '''
        根据城市名，获取国外景点id
        :param city: 城市
        :return:
        '''
        with Operation_Mongo() as om:
            data = om.select_one_collection(collection_name='overseascities', search_col={'name': city})
            return data
        return False

    @staticmethod
    def get_saleCount_china():
        '''
        获取全国排行前20
        :return:
        '''
        with Operation_Mongo() as om:
            data = om.select_all_collection(collection_name='dom_products', sort_col='saleCount', sort='desc',
                                            limit_num=20)
            return data
        return False


    @staticmethod
    def get_saleCount_abroad():
        '''
        获取国外排行前20
        :return:
        '''
        with Operation_Mongo() as om:
            data = om.select_all_collection(collection_name='ove_products', sort_col='saleCount', sort='desc',
                                            limit_num=20)
            return data
        return False

    @staticmethod
    def get_saleCount_by_dom_city(city):
        '''
         获取国内某城市排行前20
        :param city: 城市
        :return:
        '''
        with Operation_Mongo() as om:
            data = om.select_all_collection(collection_name='dom_products', search_col={'keyword': city},
                                            sort_col='saleCount', sort='desc', limit_num=20)
            return data
        return False

# if __name__ == '__main__':
    # data = MongoDB_Utils.get_ticket_china()
    # data=MongoDB_Utils.get_ticket_by_city("广州")
    # pass
