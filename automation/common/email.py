# -*- coding: utf-8 -
import sys,os
sys.path.append("../../case_config")
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.log_tool import logger
from config.runconfig import email_account,report_path,email_secret,email_to,email_ccto_info,email_to_info,email_from_info,email_from,email_server,email_server_port,email_Ccto,mail_msg




def send_email():
    try:
        '''定义一个邮件'''
        msgroot = MIMEMultipart('related')
        send_time = time.strftime("%Y_%m_%d-%H:%M:%S")

        '''set email info'''
        msgroot['subject'] = u'search相关自动化测试报告' + ' ' + send_time
        msgroot['from'] = email_from_info
        msgroot['to'] = email_to_info
        msgroot['cc'] = email_ccto_info

        '''set email content'''
        content = MIMEText(mail_msg, 'html', 'utf-8')
        msgroot.attach(content)

        '''set email attachments '''
        for fn in os.listdir(report_path):  # 返回字符串文件名
            attach = MIMEText(open(os.path.join(report_path, fn), 'rb').read(), 'base64', 'utf-8')
            attach["Content-Type"] = 'application/octet-stream'
            attach["Content-Disposition"] = 'attachment; filename=' + fn
            msgroot.attach(attach)

        '''start send email'''
        try:
            smtp = smtplib.SMTP_SSL(email_server, email_server_port)
            smtp.login(email_account, email_secret)
            smtp.sendmail(email_from, email_to+email_Ccto,msgroot.as_string())
            logger.debug('email has send out!')
            smtp.quit()
            smtp.close()
        except smtplib.SMTPException as e:
            smtp.quit()
            smtp.close()
            logger.debug('邮件发送异常')
            logger.debug(e)
    except Exception as e:
        logger.debug('邮件数据准备异常')
        logger.debug(e)