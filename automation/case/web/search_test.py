import os, sys, time
import unittest
from common.log_tool import logger
from config.case_config.search_test_config import etc,itf
from common import HTMLTestReportCN
from config.runconfig import report_path
import requests
import json

print('开始search_test')
logger.debug('开始search_test')
class test(unittest.TestCase):
    def setUp(self):
        time.sleep(3)
        print("先休息3秒钟！！！")
        print('测试开始')
        '''用例内部配置'''
        global timeout, cookie, dfp
        timeout = etc.Timeout
        dfp = etc.Dfp
        try:
            getCaseCookie =  requests.post(etc.env+itf.getcookie)
        except Exception as e:
            print("getCaseCookie失败")
            print(e)
            logger.debug("getCaseCookie失败")
            logger.debug(e)
        Cookie = getCaseCookie.headers["Set-Cookie"].split('=', 1)[1].split(';', 1)[0]
        cookie = {'SESSION': Cookie, 'dfp': dfp}
        print("当前使用的cooke：%s" % cookie)
        data = {
            'username': etc.user,
            'pwd': etc.pwd
        }
        try:
            getCaseloginCookie = requests.post(etc.env + itf.getlogin, params=data, cookies=cookie)
            rt=getCaseloginCookie.text
            print('当前使用的账号信息：%s' % rt)
        except Exception as e:
            print("getCaseloginCookie失败")
            print(e)
            logger.debug("getCaseloginCookie失败")
            logger.debug(e)


    def test_search_sku_sofaCategory_comprehensive_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key":"沙发",
            "keywords": "沙发",
            "fPrice":"",
            "fColor":"",
            "fStyle":"",
            "fPurchase":"0|0|0|0",
            "sortType": 0,
            "asc":"false",
            "searchInCanvas":0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_sku, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_new_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key": "沙发",
            "keywords": "沙发",
            "fPrice": "",
            "fColor": "",
            "fStyle": "",
            "fPurchase": "0|0|0|0",
            "sortType": 1,
            "asc": "false",
            "searchInCanvas": 0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_sku, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_priceDescending_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key": "沙发",
            "keywords": "沙发",
            "fPrice": "",
            "fColor": "",
            "fStyle": "",
            "fPurchase": "0|0|0|0",
            "sortType": 2,
            "asc": "false",
            "searchInCanvas": 0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_sku, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_priceAscending_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key": "沙发",
            "keywords": "沙发",
            "fPrice": "",
            "fColor": "",
            "fStyle": "",
            "fPurchase": "0|0|0|0",
            "sortType": 2,
            "asc": "true",
            "searchInCanvas": 0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_sku, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_comprehensive_memberPurchase_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key":"沙发",
            "keywords": "沙发",
            "fPrice":"",
            "fColor":"",
            "fStyle":"",
            "fPurchase":"1|1|0|0",
            "sortType": 0,
            "asc":"false",
            "searchInCanvas":0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_sku, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_new_memberPurchase_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key":"沙发",
            "keywords": "沙发",
            "fPrice":"",
            "fColor":"",
            "fStyle":"",
            "fPurchase":"1|1|0|0",
            "sortType": 1,
            "asc":"false",
            "searchInCanvas":0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_sku, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_priceDescending_memberPurchase_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key":"沙发",
            "keywords": "沙发",
            "fPrice":"",
            "fColor":"",
            "fStyle":"",
            "fPurchase":"1|1|0|0",
            "sortType": 2,
            "asc":"false",
            "searchInCanvas":0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_sku, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_priceAscending_memberPurchase_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key":"沙发",
            "keywords": "沙发",
            "fPrice":"",
            "fColor":"",
            "fStyle":"",
            "fPurchase":"1|1|0|0",
            "sortType": 2,
            "asc":"true",
            "searchInCanvas":0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_sku, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_comprehensive_fColorWhite_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key":"沙发",
            "keywords": "沙发",
            "fPrice":"",
            "fColor":"2",
            "fStyle":"",
            "fPurchase":"0|0|0|0",
            "sortType": 0,
            "asc":"false",
            "searchInCanvas":0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_sku, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_comprehensive_fStyleSimple_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key":"沙发",
            "keywords": "沙发",
            "fPrice":"",
            "fColor":"",
            "fStyle":"1",
            "fPurchase":"0|0|0|0",
            "sortType": 0,
            "asc":"false",
            "searchInCanvas":0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_sku, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_comprehensive_result_hasproduct(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key":"沙发",
            "keywords": "沙发",
            "fPrice":"",
            "fColor":"",
            "fStyle":"",
            "fPurchase":"0|0|0|0",
            "sortType": 0,
            "asc":"false",
            "searchInCanvas":0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        hasproduct = False
        try:
            rt = requests.post(etc.env+itf.search_sku, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            objectNum = len(rt_json['r']['list'])
                            print("正常:存在%d个对象" % objectNum)
                            for i in range(objectNum):
                                objecttype = rt_json['r']['list'][i]['type']
                                if objecttype == 2:
                                    hasproduct = True
                            if hasproduct:
                                case_desc = '第一页数据中存在商品对象'
                                print('第一页数据中存在商品对象')
                            else:
                                case_state = False
                                case_desc = '第一页数据中不存在商品对象'
                                print('第一页数据中没有商品对象')
                                print(rt_json['r']['list'])
                                logger.debug('r.list字段返回值异常')
                                logger.debug(rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_sku_sofaCategory_comprehensive_memberPurchase_result_hasproduct(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 48,
            "key":"沙发",
            "keywords": "沙发",
            "fPrice":"",
            "fColor":"",
            "fStyle":"",
            "fPurchase":"1|1|0|0",
            "sortType": 0,
            "asc":"false",
            "searchInCanvas":0,
            "aggr": "false"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        hasproduct = False
        try:
            rt = requests.post(etc.env+itf.search_sku, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            objectNum = len(rt_json['r']['list'])
                            print("正常:存在%d个对象" % objectNum)
                            for i in range(objectNum):
                                objecttype = rt_json['r']['list'][i]['type']
                                if objecttype == 2:
                                    hasproduct = True
                            if hasproduct:
                                case_desc = '第一页数据中存在商品对象'
                                print('第一页数据中存在商品对象')
                            else:
                                case_state = False
                                case_desc = '第一页数据中不存在商品对象'
                                print('第一页数据中没有商品对象')
                                print(rt_json['r']['list'])
                                logger.debug('r.list字段返回值异常')
                                logger.debug(rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])



    def test_search_brands_directPurchase_all_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'key': '直采',
            'member': 'false',
            'limit': 32,
            'offset': 0,
            'fCountry': '',
            'fStyle': '',
            'fCollection': '',
            'fLetter': '',
            'onlyShowCompleteFaceItems':'true'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brands, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brands_directPurchase_Member_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'key': '直采',
            'member': 'true',
            'limit': 32,
            'offset': 0,
            'fCountry': '',
            'fStyle': '',
            'fCollection': '',
            'fLetter': '',
            'onlyShowCompleteFaceItems': 'true'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brands, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brands_directPurchase_all_fCountryChinaAndAmerica_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'key': '直采',
            'member': 'true',
            'limit': 32,
            'offset': 0,
            'fCountry': '1|3',
            'fStyle': '',
            'fCollection': '',
            'fLetter': '',
            'onlyShowCompleteFaceItems': 'true'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brands, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brands_directPurchase_all_fStyleSimpleAndAvantGarde_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'key': '直采',
            'member': 'true',
            'limit': 32,
            'offset': 0,
            'fCountry': '',
            'fStyle': '1|2',
            'fCollection': '',
            'fLetter': '',
            'onlyShowCompleteFaceItems': 'true'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brands, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brands_directPurchase_all_fCollectionSofaAndlanterns_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'key': '直采',
            'member': 'true',
            'limit': 32,
            'offset': 0,
            'fCountry': '',
            'fStyle': '',
            'fCollection': '10003|10010',
            'fLetter': '',
            'onlyShowCompleteFaceItems': 'true'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brands, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brands_directPurchase_all_fCountryChinaAmerica_fStyleSimpleAndAvantGarde_fCollectionSofaAndlanterns_Y_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'key': '直采',
            'member': 'true',
            'limit': 32,
            'offset': 0,
            'fCountry': '1|3',
            'fStyle': '1|2',
            'fCollection': '10003|10010',
            'fLetter': 'Y',
            'onlyShowCompleteFaceItems': 'true'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brands, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])



    def test_search_boards_a_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'limit': 40,
            'offset': 0,
            'fScene':'',
            'fStyle':'',
            'searchInCanvas': 0,
            'aggr': 'false',
            'key': 'a'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_boards, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_boards_a_fSceneLivingRoom_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'limit': 40,
            'offset': 0,
            'fScene':'101',
            'fStyle':'',
            'searchInCanvas': 0,
            'aggr': 'false',
            'key': 'a'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_boards, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_boards_a_fSceneLivingRoomAndDiningRoom_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'limit': 40,
            'offset': 0,
            'fScene':'101|102',
            'fStyle':'',
            'searchInCanvas': 0,
            'aggr': 'false',
            'key': 'a'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_boards, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_boards_a_fStyleSimple_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'limit': 40,
            'offset': 0,
            'fScene': '',
            'fStyle': '1',
            'searchInCanvas': 0,
            'aggr': 'false',
            'key': 'a'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_boards, params=data, cookies=cookie, headers=header,
                               timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_boards_a_fStyleSimpleAndAvantGarde_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'limit': 40,
            'offset': 0,
            'fScene': '',
            'fStyle': '1|2',
            'searchInCanvas': 0,
            'aggr': 'false',
            'key': 'a'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_boards, params=data, cookies=cookie, headers=header,
                               timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_boards_a_fSceneLivingRoomAndDiningRoom_fStyleSimpleAndAvantGarde_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'limit': 40,
            'offset': 0,
            'fScene':'101|102',
            'fStyle':'1|2',
            'searchInCanvas': 0,
            'aggr': 'false',
            'key': 'a'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_boards, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])



    def test_search_myDesigns_recentChanges_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_myDesigns, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_myDesigns_newlyCreated_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'sortType':'1'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_myDesigns, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_myDesigns_recentChanges_folder_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'folder':etc.boardFolderId
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_myDesigns, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_myDesigns_newlyCreated_folder_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'folder': etc.boardFolderId,
            'sortType':'1'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_myDesigns, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])



    def test_search_collect_product_all_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_collect_product_all_fPriceSixThousand_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fPrice': '0|600000'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_collect_product_all_fColorBlack_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fColor': '1'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_collect_product_all_fStyleSimpleAndAvantGarde_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fStyle':'1|2'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_collect_product_all_fPriceSixThousand_fColorBlack_fStyleSimpleAndAvantGarde_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fPrice': '0|600000',
            'fColor': '1',
            'fStyle': '1|2'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_collect_product_fFolder_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fFolder':etc.itemFolderId
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_collect_product_fFolder_fPriceSixThousand_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fPrice': '0|600000',
            'fFolder': etc.itemFolderId
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_collect_product_fFolder_fColorBlack_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fColor': '1',
            'fFolder': etc.itemFolderId
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_collect_product_fFolder_fStyleSimpleAndAvantGarde_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fStyle':'1|2',
            'fFolder': etc.itemFolderId
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_collect_product_fFolder_fPriceSixThousand_fColorBlack_fStyleSimpleAndAvantGarde_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fPrice': '0|600000',
            'fColor': '1',
            'fStyle': '1|2',
            'fFolder': etc.itemFolderId
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_collect_product, params=data, cookies=cookie, headers=header,timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])


    def test_search_user_public_product_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'fUserId': etc.PersonalCenterUserId
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_user_public_product, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_userDesigns_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            'offset': 0,
            'limit': 36,
            'userId': etc.PersonalCenterUserId
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_userDesigns, params = data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])



    def test_search_brandItems_comprehensive_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp,'bundleversion':'3.0.7'}
        data = {
            "brandContainerId":etc.BrandpageUserId,
            "offset":0,
            "limit":48,
            'fCategory': '',
            'fCollection': '',
            'fSeries': '',
            'fColor': '',
            'fStyle': '',
            'key': '休闲椅',
            'sortType':0,
            'asc': 'false'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brandItems, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brandItems_new_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp,'bundleversion':'3.0.7'}
        data = {
            "brandContainerId":etc.BrandpageUserId,
            "offset":0,
            "limit":5,
            'searchInCanvas': 0,
            'sortType':1
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brandItems, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brandItems_fCollectionChair_fCategoryRecreationalChair_comprehensive_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp,'bundleversion':'3.0.7'}
        data = {
            "brandContainerId":etc.BrandpageUserId,
            "offset":0,
            "limit":48,
            'fCategory': '117',
            'fCollection': '10004',
            'fSeries': '',
            'fColor': '',
            'fStyle': '',
            'key': '',
            'sortType':0,
            'asc': 'false'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brandItems, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brandItems_fCollectionChair_fCategoryRecreationalChair_fSeries_comprehensive_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp,'bundleversion':'3.0.7'}
        data = {
            "brandContainerId":etc.BrandpageUserId,
            "offset":0,
            "limit":48,
            'fCategory': '117',
            'fCollection': '10004',
            'fSeries': '洛基纳',
            'fColor': '',
            'fStyle': '',
            'key': '',
            'sortType':0,
            'asc': 'false'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brandItems, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brandItems_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_comprehensive_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp,'bundleversion':'3.0.7'}
        data = {
            "brandContainerId":etc.BrandpageUserId,
            "offset":0,
            "limit":48,
            'fCategory': '117',
            'fCollection': '10004',
            'fSeries': '洛基纳',
            'fColor': '1|4|100|106',
            'fStyle': '',
            'key': '',
            'sortType':0,
            'asc': 'false'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brandItems, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brandItems_RecreationalChair_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_fStyle_comprehensive_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp,'bundleversion':'3.0.7'}
        data = {
            "brandContainerId":etc.BrandpageUserId,
            "offset":0,
            "limit":48,
            'fCategory': '117',
            'fCollection': '10004',
            'fSeries': '洛基纳',
            'fColor': '1|4|100|106',
            'fStyle': '7',
            'key': '休闲椅',
            'sortType':0,
            'asc': 'false'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brandItems, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brandItems_RecreationalChair_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_fStyle_new_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp,'bundleversion':'3.0.7'}
        data = {
            "brandContainerId":etc.BrandpageUserId,
            "offset":0,
            "limit":48,
            'fCategory': '117',
            'fCollection': '10004',
            'fSeries': '洛基纳',
            'fColor': '1|4|100|106',
            'fStyle': '7',
            'key': '休闲椅',
            'sortType':1,
            'asc': 'false'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brandItems, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brandItems_RecreationalChair_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_fStyle_priceDescending_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp,'bundleversion':'3.0.7'}
        data = {
            "brandContainerId":etc.BrandpageUserId,
            "offset":0,
            "limit":48,
            'fCategory': '117',
            'fCollection': '10004',
            'fSeries': '洛基纳',
            'fColor': '1|4|100|106',
            'fStyle': '7',
            'key': '休闲椅',
            'sortType':2,
            'asc': 'false'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brandItems, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_search_brandItems_RecreationalChair_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_fStyle_priceAscending_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp,'bundleversion':'3.0.7'}
        data = {
            "brandContainerId":etc.BrandpageUserId,
            "offset":0,
            "limit":48,
            'fCategory': '117',
            'fCollection': '10004',
            'fSeries': '洛基纳',
            'fColor': '1|4|100|106',
            'fStyle': '7',
            'key': '休闲椅',
            'sortType':2,
            'asc': 'true'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.search_brandItems, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])



    def test_mall_order_getPage_all_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 10
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.mall_order_getPage, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_mall_order_getPage_all_Decorate_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "key": "摆件",
            "offset": 0,
            "limit": 10
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.mall_order_getPage, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_mall_order_getPage_nonPayment_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 10,
            "state":10
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.mall_order_getPage, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_mall_order_getPage_toBeShipped_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 10,
            "state":11
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.mall_order_getPage, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_mall_order_getPage_toBeReceived_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 10,
            "state":12
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.mall_order_getPage, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])

    def test_mall_order_getPage_drawBack_result(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':dfp}
        data = {
            "offset": 0,
            "limit": 10,
            "hasRefund": "true"
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.mall_order_getPage, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:",rt_json['ok'])
                if rt_json['c']== 0:
                    print("正常:",rt_json['c'])
                    if rt_json['m'] =='success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:",rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state=False
                case_desc='ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False :
            self.assertTrue(case_state, [case_desc])



    def test_search_tools_board_keyModernStyle_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'fCategory': '73',
            'fScene': '',
            'fStyle': '',
            'key': '现代风',
            'limit': 32,
            'offset': 0
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_tools_board, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_tools_board_keyModernStyle_fSceneLivingRoomAndDiningRoom_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'fCategory': '73',
            'fScene': '101|104',
            'fStyle': '',
            'key': '现代风',
            'limit': 32,
            'offset': 0
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_tools_board, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_tools_board_keyModernStyle_fStyleSimpleAndAvantGarde_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'fCategory': '73',
            'fScene': '',
            'fStyle': '1|2',
            'key': '现代风',
            'limit': 32,
            'offset': 0
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_tools_board, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])

    def test_search_tools_board_keyModernStyle_fSceneLivingRoomAndDiningRoom_fStyleSimpleAndAvantGarde_result(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json', 'dfp': dfp}
        data = {
            'fCategory': '73',
            'fScene': '101|104',
            'fStyle': '1|2',
            'key': '现代风',
            'limit': 32,
            'offset': 0
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env + itf.search_tools_board, params=data, cookies=cookie, headers=header, timeout=timeout)
            print("测试使用cookie为：%s" % str(cookie))
            print("测试接口url：%s" % rt.url)
            # print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug(e)
            case_state = False
            case_desc = "请求url异常"
        try:
            if rt.status_code == 200:
                print("状态头为200，正常继续执行")
                logger.debug("状态头为200，正常继续执行")
            else:
                print('error：不正常的请求状态code：%s' % rt.status_code)
                logger.debug('error：不正常的请求code：%s' % rt.status_code)
                case_state = False
                case_desc = 'error：不正常的请求code：%s' % rt.status_code
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析状态头异常"
        try:
            rt_json = json.loads(json.dumps(rt.json()))
            if rt_json['ok']:
                print("正常:", rt_json['ok'])
                if rt_json['c'] == 0:
                    print("正常:", rt_json['c'])
                    if rt_json['m'] == 'success':
                        print("正常:", rt_json['m'])
                        if rt_json['r']['list']:
                            print("正常:", rt_json['r']['list'])
                        else:
                            case_state = False
                            case_desc = 'r.list字段返回值异常'
                            print("r.list字段返回值异常")
                            print(rt_json['r']['list'])
                            logger.debug("r.list字段返回值异常")
                            logger.debug(rt_json['r']['list'])
                    else:
                        case_state = False
                        case_desc = 'm字段返回值异常'
                        print("m字段返回值异常")
                        print(rt_json['m'])
                        logger.debug("m字段返回值异常")
                        logger.debug(rt_json['m'])
                else:
                    case_state = False
                    case_desc = 'c字段返回值异常'
                    print("c字段返回值异常")
                    print(rt_json['c'])
                    logger.debug("c字段返回值异常")
                    logger.debug(rt_json['c'])
            else:
                case_state = False
                case_desc = 'ok字段返回值异常'
                print("ok字段返回值异常")
                print(rt_json['ok'])
                logger.debug("ok字段返回值异常")
                logger.debug(rt_json['ok'])
        except Exception as e:
            print("解析json异常")
            print(e)
            logger.debug("解析json异常")
            logger.debug(e)
            case_state = False
            case_desc = "解析json异常"
        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, [case_desc])
        elif case_state == False:
            self.assertTrue(case_state, [case_desc])







    def tearDown(self):
        print('测试结束')

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
    # suite.addTest(test("test_search_sku_sofaCategory_comprehensive_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_new_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_priceDescending_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_priceAscending_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_comprehensive_memberPurchase_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_new_memberPurchase_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_priceDescending_memberPurchase_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_priceAscending_memberPurchase_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_comprehensive_fColorWhite_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_comprehensive_fStyleSimple_result"))
    # suite.addTest(test("test_search_sku_sofaCategory_comprehensive_result_hasproduct"))
    # suite.addTest(test("test_search_sku_sofaCategory_comprehensive_memberPurchase_result_hasproduct"))

    # suite.addTest(test("test_search_brands_directPurchase_all_result"))
    # suite.addTest(test("test_search_brands_directPurchase_Member_result"))
    # suite.addTest(test("test_search_brands_directPurchase_all_fCountryChinaAndAmerica_result"))
    # suite.addTest(test("test_search_brands_directPurchase_all_fStyleSimpleAndAvantGarde_result"))
    # suite.addTest(test("test_search_brands_directPurchase_all_fCollectionSofaAndlanterns_result"))
    # suite.addTest(test("test_search_brands_directPurchase_all_fCountryChinaAmerica_fStyleSimpleAndAvantGarde_fCollectionSofaAndlanterns_Y_result"))



    # suite.addTest(test("test_search_boards_a_result"))
    # suite.addTest(test("test_search_boards_a_fSceneLivingRoom_result"))
    # suite.addTest(test("test_search_boards_a_fSceneLivingRoomAndDiningRoom_result"))
    # suite.addTest(test("test_search_boards_a_fStyleSimple_result"))
    # suite.addTest(test("test_search_boards_a_fStyleSimpleAndAvantGarde_result"))
    # suite.addTest(test("test_search_boards_a_fSceneLivingRoomAndDiningRoom_fStyleSimpleAndAvantGarde_result"))

    # suite.addTest(test("test_search_myDesigns_recentChanges_result"))
    # suite.addTest(test("test_search_myDesigns_newlyCreated_result"))
    # suite.addTest(test("test_search_myDesigns_recentChanges_folder_result"))
    # suite.addTest(test("test_search_myDesigns_newlyCreated_folder_result"))

    # suite.addTest(test("test_search_collect_product_all_result"))
    # suite.addTest(test("test_search_collect_product_all_fPriceSixThousand_result"))
    # suite.addTest(test("test_search_collect_product_all_fColorBlack_result"))
    # suite.addTest(test("test_search_collect_product_all_fStyleSimpleAndAvantGarde_result"))
    # suite.addTest(test("test_search_collect_product_all_fPriceSixThousand_fColorBlack_fStyleSimpleAndAvantGarde_result"))
    # suite.addTest(test("test_search_collect_product_fFolder_result"))
    # suite.addTest(test("test_search_collect_product_fFolder_fPriceSixThousand_result"))
    # suite.addTest(test("test_search_collect_product_fFolder_fColorBlack_result"))
    # suite.addTest(test("test_search_collect_product_fFolder_fStyleSimpleAndAvantGarde_result"))
    # suite.addTest(test("test_search_collect_product_fFolder_fPriceSixThousand_fColorBlack_fStyleSimpleAndAvantGarde_result"))

    # suite.addTest(test("test_search_user_public_product_result"))
    # suite.addTest(test("test_search_userDesigns_result"))

    # suite.addTest(test("test_search_brandItems_comprehensive_result"))
    # suite.addTest(test("test_search_brandItems_new_result"))
    # suite.addTest(test("test_search_brandItems_fCollectionChair_fCategoryRecreationalChair_comprehensive_result"))
    # suite.addTest(test("test_search_brandItems_fCollectionChair_fCategoryRecreationalChair_fSeries_comprehensive_result"))
    # suite.addTest(test("test_search_brandItems_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_comprehensive_result"))
    # suite.addTest(test("test_search_brandItems_RecreationalChair_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_fStyle_comprehensive_result"))
    # suite.addTest(test("test_search_brandItems_RecreationalChair_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_fStyle_new_result"))
    # suite.addTest(test("test_search_brandItems_RecreationalChair_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_fStyle_priceDescending_result"))
    # suite.addTest(test("test_search_brandItems_RecreationalChair_fCollectionChair_fCategoryRecreationalChair_fSeries_fColor_fStyle_priceDescending_result"))

    # suite.addTest(test("test_mall_order_getPage_all_result"))
    # suite.addTest(test("test_mall_order_getPage_all_Decorate_result"))
    # suite.addTest(test("test_mall_order_getPage_nonPayment_result"))
    # suite.addTest(test("test_mall_order_getPage_toBeShipped_result"))
    # suite.addTest(test("test_mall_order_getPage_toBeReceived_result"))
    # suite.addTest(test("test_mall_order_getPage_drawBack_result"))

    # suite.addTest(test("test_search_tools_board_keyModernStyle_result"))
    # suite.addTest(test("test_search_tools_board_keyModernStyle_fSceneLivingRoomAndDiningRoom_result"))
    # suite.addTest(test("test_search_tools_board_keyModernStyle_fStyleSimpleAndAvantGarde_result"))
    # suite.addTest(test("test_search_tools_board_keyModernStyle_fSceneLivingRoomAndDiningRoom_fStyleSimpleAndAvantGarde_result"))
    # suite.addTest(test(""))









# pyfilename = os.path.basename(__file__).replace(".py","")
# rptcreatetime = time.strftime("%Y-%m-%d", time.localtime())
# filename = report_path +pyfilename+'_'+rptcreatetime+'.html'
# fp = open(filename, 'wb')
#
# '''
# HTMLTestRunner配置项
#     title：自动化测试报告标题
#     description：自动化测试报告描述
#     tester：自动化测试编写人员
# '''
# runner = HTMLTestReportCN.HTMLTestRunner(
#     stream=fp,
#     title=pyfilename+u'自动化测试报告',
#     description=pyfilename+u'自动化测试报告',
#     tester='QA_dgj'
# )
# '''不生成报告，调试用'''
# # runner = unittest.TextTestRunner()
# '''生成报告'''
# runner.run(suite)
# fp.close()
