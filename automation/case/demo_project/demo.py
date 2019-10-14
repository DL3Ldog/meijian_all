import sys

sys.path.append('../../automation')
import unittest
from common.log_tool import logger
from config.case_config.demo_test_config import etc,itf
import requests

print("开始demo")
logger.debug("开始demo")

class demo(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        '''配置超时'''
        global timeout
        timeout = 1
    def test_demo(self):
        case_state =True
        case_name = sys._getframe().f_code.co_name
        case_desc = '测试通过'
        header = {'content-type': 'application/json','dfp':etc.Dfp}
        data = {}
        print("test on：%s" % case_name)
        logger.debug("test on：%s" % case_name)
        try:
            rt = requests.post(etc.env+itf.demo,data,headers = header,timeout=timeout)
            print("测试接口url：%s" % rt.url)
            print("请求头：%s" % rt.headers)
            print("返回结果：%s" % rt.text)
            logger.debug("测试接口url：%s" % rt.url)
            logger.debug("请求头：%s" % rt.headers)
            logger.debug("返回结果：%s" % rt.text)
        except Exception as e:
            print("error：接口请求异常")
            print("开始测试：%s" % rt.url)
            print("请求头：%s" % rt.headers)
            print(e)
            logger.debug("error：接口请求异常")
            logger.debug("开始测试：%s" % rt.url)
            logger.debug("请求头：%s" % rt.headers)
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

        '''
        你的用例验证代码
        try:
            
            json化返回结果
            rt_json = json.loads(json.dumps(rt.json()))
            ......
        except:
            ......
        '''



        print("test end %s" % case_name)
        logger.debug("test end %s" % case_name)
        if case_state:
            self.assertTrue(case_state, ['测试通过'])
        elif case_state == False :
            self.assertTrue(case_state, ['测试不通过'])


    def tearDown(self):
        print('测试结束')

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(demo_project("test_demo"))
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
