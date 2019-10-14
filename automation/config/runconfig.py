# -*- coding: utf-8 -
import time

#定义需要跑的执行器actuator = []
actuator = ['search_actuator.py']

# from config.case_config.config import actuator
#报告存储路径
rpt_createtime = time.strftime("%Y_%m_%d-%H:%M:%S")
rpt_date_path = rpt_createtime.split('-',1)[0]
# report_path = r"../reports/%s/%s" % (rpt_date_path,rpt_createtime)
report_path = r"../reports/%s/" % rpt_date_path


#邮件开关 0:不发送 1：发送
email_on_off = 0
#邮件服务
email_server = "smtp.qq.com"
#邮件服务
email_server_port = "465"
#邮件服务账号
email_account = "867821548@qq.com"
#邮件secretkey
email_secret = "qdndfbseqqqibfea"



#邮件发送对象
email_from = "867821548@qq.com"
#邮件接收对象
email_to = ["867821548@qq.com"]
#邮件抄送对象
email_Ccto = ['dongguojun@imeijian.cn','2371361399@qq.com']


#邮件发送信息info
'''发件人'''
email_from_info = email_from
'''收件人'''
email_to_info = '%s' % ','.join(email_to)
'''抄送人'''
email_ccto_info = '%s' % ','.join(email_Ccto)

#邮件内容
'''set email attachments HTML'''
mail_msg = """
        <p>黄天保佑测试结果如附件</p>
        <p><a href="http://www.baidu.com">这是一个链接</a></p>
        """