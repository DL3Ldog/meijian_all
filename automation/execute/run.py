# -*- coding: utf-8 -
import sys, os, time
sys.path.append('../../automation')
from config.runconfig import report_path,rpt_date_path,actuator,email_on_off
from common.log_tool import logger
from common import email
from selenium import webdriver


# 当前脚本所在的文件绝对路径
cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)
# 将当前路径设置为python的临时环境变量，用于命令执行,需要设置是因为项目存在多处相互调用
os.putenv("PYTHONPATH", cur_path)
error_count = 0
def run_case():
    global email_on_off
    global error_count
    logger.debug("")
    logger.debug("")
    logger.debug("----------------------------------------------------------------------------------------------")
    try:
        today = time.strftime("%Y_%m_%d-%H:%M:%S").split('-', 1)[0]
        if os.path.exists("../reports/%s" % today):
            logger.debug("已经有reportdate文件夹：%s" % today)
        else:
            os.mkdir(report_path)
            logger.debug("新建了reportdate文件夹：%s" % today)
    except:
        logger.debug("当天reportdate文件夹目录失败")
    try:
        '''
        不使用全局执行所有case

            # 使用os.path.join拼接地址
            case_path = os.path.join(cur_path, "../case")

            # 获取当前目录下所有的文件名
            lst = os.listdir(case_path)
            for c in lst:
                # 判断文件名是以.py结尾的;添加and c.find("DemoGet") == -1就是去掉DemoGet.py文件
                if os.path.splitext(c)[1] == '.py' and c.find("__init__") == -1 and c.find("demo_project") == -1 :
                    try:
                        # 查看文件名
                        logger.debug(c)
                        # 相当于在终端执行文件  python main.py
                        os.system('python3 {}'.format(os.path.join(case_path, c)))
                    except Exception as e:
                        logger.debug("用例执行失败")
                        logger.debug(e)
        '''
        for i in range(len(actuator)):
            os.system('python3 {}'.format(os.path.join("../actuator", actuator[i])))
        try:
            opt = webdriver.ChromeOptions()
            # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
            opt.set_headless(True)
            # 创建chrome无界面对象
            checkresult = webdriver.Chrome(options=opt)
            for i in range(len(os.listdir(report_path))):
                check_report_path = 'file://'+cur_path.replace("execute","reports/")+rpt_date_path+'/'+ os.listdir(report_path)[i]
                print(check_report_path)
                checkresult.get(check_report_path)
                string1 = checkresult.find_element_by_xpath("//*[@id='result_table']/tbody/tr[2]/td[4]").text
                string2 = checkresult.find_element_by_xpath("//*[@id='result_table']/tbody/tr[2]/td[5]").text
                Fcount = int(string1)
                Ecount = int(string2)
                print("Fcount:" + string1 + "  " + "Ecount:" + string2)
                all_Error_count = Fcount + Ecount
                error_count = error_count + all_Error_count
                print("error_count:%d" % error_count)

        except Exception as ex:
            logger.debug("检查错误识别失败")
            logger.error(ex)
            print(ex)
    except Exception as exx:
        logger.debug("运行出问题了")
        logger.error(str(exx))
        email_on_off = 0
    finally:
        logger.info("*********TEST END*********")
        # send test report by email
        if email_on_off == 1 and error_count != 0:
            email.send_email()
            logger.info("email on and has error ,Doesn't send report email to developer.")
        elif email_on_off == 1 and error_count == 0:
            logger.info("email on but no error ,Doesn't send report email to developer.")
        elif email_on_off == 0 and error_count != 0:
            logger.info("has error but email off ,Doesn't send report email to developer.")
        elif email_on_off == 0 and error_count == 0:
            logger.info("no error and email off ,Doesn't send report email to developer.")
        else:
            logger.info("Unknow state.")
        logger.debug("")
        logger.debug("")

if __name__ == "__main__":
    run_case()



