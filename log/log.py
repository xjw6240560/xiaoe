#创建时间  2023-06-29 17:19
#作者  小酒窝

# -*-coding:utf-8 -*-
import os
import logging

# 定义了blog_ui项目的绝对路径
base_url = r"E:\PycharmProjects\xiaoe"

class Logger:
    def __init__(self, path=base_url+'\\log\\logsest.log', clevel=logging.DEBUG, Flevel=logging.DEBUG):
        # 判断log文件夹是否存在，不存在的话创建文件夹以及日志文件
        project_dir = os.listdir(base_url)
        dir_name = 'log'  # log文件夹
        if dir_name not in project_dir:
            create_path = base_url + '/' + dir_name
            os.makedirs(create_path)
            file = open(create_path + '/autotest.log,','w',encoding='utf-8')
            file.close()
        # 创建logger
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        # 防止创建多个logger对象
        if not self.logger.handlers:
            # 设置日志格式
            fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
            # 设置CMD日志
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clevel)
            # 设置文件日志
            fh = logging.FileHandler(path)
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    def debugText(self,projectNumber = '',errorText = '',bidder = '',otherText=''):
        if errorText is not None:
            if errorText.find('成功') < 0:
                if errorText.find("element not interactable") > 0:
                    self.logger.debug("项目编号："+projectNumber+"  投标人or专家："+bidder+"\n"+'元素不可交互'+"\n"+errorText)
                else:
                    self.logger.debug("项目编号："+projectNumber+"  投标人or专家："+bidder+"\n"+errorText)
        else:
            if otherText != '':
                self.logger.debug("项目编号："+projectNumber+"  投标人or专家："+bidder+"\n"+otherText)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)
