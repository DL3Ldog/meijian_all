import os,sys,time,unittest
sys.path.append('../../automation')
from config.runconfig import report_path
from common import HTMLTestReportCN

print(os.path.dirname(os.path.realpath(__file__)))
#执行器执行的case的工程
# path = '../case/web'
path = ['../case/tms/']

for i in range(len(path)):
    all_cases = unittest.TestLoader().discover(path[i], pattern='*.py')
    # all_cases = unittest.defaultTestLoader.discover(path,pattern='*.py')
    # all_cases = unittest.TestLoader().discover(path,pattern='*.py')
    print("case集合为:",all_cases)
    if __name__ == "__main__":
        pyfilename = os.path.basename(__file__).replace(".py","")
        projectname = path[i].replace("../case/", "")
        print(pyfilename)
        rptcreatetime = time.strftime("%Y-%m-%d", time.localtime())
        filename = report_path +pyfilename+'_'+projectname+'_'+rptcreatetime+'.html'
        fp = open(filename, 'wb')

        '''
        HTMLTestRunner配置项
            title：自动化测试报告标题
            description：自动化测试报告描述
            tester：自动化测试编写人员
        '''
        runner = HTMLTestReportCN.HTMLTestRunner(
            stream=fp,
            title=projectname+u'自动化测试报告',
            description=projectname+u'自动化测试报告',
            tester='QA_dgj'
        )
        '''不生成报告，调试用'''
        # runner = unittest.TextTestRunner()
        '''生成报告'''
        runner.run(all_cases)
        fp.close()