import logging
import time
global logger
timetmp = time.strftime("%Y-%m-%d", time.localtime())
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(filename="../logs/%s_logs.log"% timetmp,encoding='utf-8',mode='a')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)