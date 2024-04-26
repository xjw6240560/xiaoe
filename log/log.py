# 创建时间  2023-06-29 17:19
# 作者  小酒窝

# -*-coding:utf-8 -*-
import os
import shutil
import logging
from logging.handlers import RotatingFileHandler

# 定义项目的绝对路径
base_url = os.path.abspath(os.path.dirname(__file__)).split('base')[0]


class Logger:
    def __init__(self, path=os.path.join(base_url, 'logTest.log'), clevel=logging.DEBUG, Flevel=logging.DEBUG):
        # 确保日志文件夹存在
        dir_name = 'log'
        create_path = os.path.join(base_url, dir_name)
        if not os.path.exists(create_path):
            os.makedirs(create_path)

        # 设置日志记录器
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # 防止重复添加处理程序
        if not self.logger.handlers:
            fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

            # 设置控制台处理程序
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clevel)

            # 设置文件处理程序，并启用文件轮换
            fh = RotatingFileHandler(path, maxBytes=1024 * 1024, backupCount=3, encoding='utf-8')
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)

            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    def debugText(self, projectNumber='', errorText='', bidder='', otherText=''):
        if errorText:
            if "element not interactable" in errorText:
                self.logger.debug(f"项目编号：{projectNumber}  投标人or专家：{bidder} - 元素不可交互 - {errorText}")
            else:
                self.logger.debug(f"项目编号：{projectNumber}  投标人or专家：{bidder} - {errorText}")
        elif otherText:
            self.logger.debug(f"项目编号：{projectNumber}  投标人or专家：{bidder} - {otherText}")

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
