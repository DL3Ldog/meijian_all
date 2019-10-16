import os,sys,time

sys.path.append('../../automation')
import unittest,requests
from common import HTMLTestReportCN
from common.log_tool import logger
from config.case_config.tms_api_test_config import etc, itf,user
from config.runconfig import report_path



print("开始demo")
logger.debug("开始demo")
class tms_login(unittest.TestCase):
    def setUp(self):
        print("test start")
        case_state = True
        case_desc = '测试通过'

    def test_admin_login(self):
        case_state = True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json'}
        data = {
            'username':'dgj',
            'password':'dgjkyo'
        }
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.admin_login_islogin, params = data, cookies=cookie, headers=header, timeout=timeout)
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
        except Exception as e:
            print("获取请求状态code异常")
            print(e)
            logger.debug("获取请求状态code异常")
            logger.debug(e)

        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, ['测试通过'])
        elif case_state == False:
            self.assertTrue(case_state, ['测试不通过'])

    def tearDown(self):
        print('测试结束')

class tms_schema(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        '''配置超时'''
        global timeout,cookie
        timeout = 1
        try:
            getCaseCookie = requests.post(etc.env + itf.admin_login_islogin)
        except Exception as e:
            print("getCaseCookie失败")
            print(e)
            logger.debug("getCaseCookie失败")
            logger.debug(e)
        Cookie = getCaseCookie.headers["Set-Cookie"].split('=', 1)[1].split(';', 1)[0]
        cookie = {'SESSION': Cookie}
        print("当前使用的cooke：%s" % cookie)
        data = {
            'username': user.user,
            'pwd': user.pwd
        }
        try:
            getCaseloginCookie = requests.post(etc.env + itf.admin_login, params=data, cookies=cookie)
            rt = getCaseloginCookie.text
            print('当前使用的账号信息：%s' % rt)
        except Exception as e:
            print("getCaseloginCookie失败")
            print(e)
            logger.debug("getCaseloginCookie失败")
            logger.debug(e)

    def test_go(self):
        print(1)

    def tearDown(self):
        print('测试结束')
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(tms_schema("test_admin_login"))
#
#
# pyfilename = os.path.basename(__file__).replace(".py","")
# rptcreatetime = time.strftime("%Y-%m-%d", time.localtime())
# filename = report_path +pyfilename+'_'+rptcreatetime+'.html'
# fp = open(filename, 'wb')
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
