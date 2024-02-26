# -*- coding: utf-8 -*-
# @Time : 2024-01-25 9:38
# @Author : 皮卡丘

import traceback
import pymysql
from log.log import Logger


class Mysql:
    logger = Logger()

    def connect_mysql(self):
        """连接mysql数据库"""
        try:
            conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='root',
                db='ceshi',
                charset='utf8'
            )
            cursor = conn.cursor()  # 创建游标
            return conn, cursor
        except (Exception, BaseException):
            error = traceback.format_exc()
            self.logger.info(error)

    @staticmethod
    def close_conn(conn, cursor):
        conn.close()
        cursor.close()

    def insert_and_update_sql(self, sql, *args):  # 添加数据
        conn, cursor = self.connect_mysql()  # 连接数据库
        try:
            cursor.execute(sql, args)
            conn.commit()
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.info(error)
            conn.rollback()
        self.close_conn(conn=conn, cursor=cursor)

    def query_sql(self, sql, *args):  # 查询数据查询
        conn, cursor = self.connect_mysql()  # 连接数据库
        try:
            cursor.execute(sql, args)
            result = cursor.fetchall()
            return result
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.info(error)
        self.close_conn(conn=conn, cursor=cursor)

    def query_now_date(self):  # 获取专家抽取时间
        sql = 'select nowdate,hour from get_now_date'
        try:
            result = self.query_sql(sql)
            return result[0]
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(error)

    def insert_expertData(self, projectNumber, username, password, judgeName):  # 插入专家账号密码
        conn, cursor = self.connect_mysql()
        sql = 'insert into expert (projectNumber,username,password,judgeName) values(%s,%s,%s,%s)'
        try:
            cursor.execute(sql, (projectNumber, username, password, judgeName))
            conn.commit()
        except (Exception, BaseException) as e:
            error = traceback.format_exc()
            if str(e).find('Duplicate entry') > 0:
                self.logger.debugText(projectNumber, '评委已经添加！')
            else:
                self.logger.debugText(projectNumber, error)
            conn.rollback()
        conn.close()
        cursor.close()

    def update_evaluationBidWay(self, evaluationBidWay, judgeNumber, projectNumber):  # 更新评标办法类型和评委个数
        conn, cursor, = self.connect_mysql()
        sql = 'update project set evaluationBidWay = %s , judgeNumber = %s where projectNumber = %s'
        try:
            cursor.execute(sql, (evaluationBidWay, judgeNumber, projectNumber))
            conn.commit()
            print("评标类型和评委个数更新成功！")
        except (Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)
            conn.rollback()
        conn.close()
        cursor.close()  #

    def update_isAgree(self, isAgree, username, projectNumber):  # 更新专家协议是否确认
        sql = 'update expert set isAgree = %s where username = %s and projectNumber = %s'
        try:
            self.insert_and_update_sql(sql, isAgree, username, projectNumber)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def insert_projectData(self, projectNumber, projectType, tenderOrganizationType, tenderWay):  # 插入项目数据
        self.connect_mysql()
        sql = 'insert into project (projectNumber,projectType,tenderOrganizationType,tenderWay) values(%s,%s,%s,%s)'
        try:
            self.insert_and_update_sql(sql, projectNumber, projectType, tenderOrganizationType, tenderWay)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber=projectNumber, errorText=error)

    def update_now_date(self, nowdate, hour=0):
        sql = 'update get_now_date set nowdate = %s,hour = %s  where id = 0'
        try:
            self.insert_and_update_sql(sql, nowdate, hour)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(error)

    def update_enterprise_count(self, enterpriseCount, projectNumber):  # 更新企业数量
        sql = 'update project set enterpriseCount = %s where projectNumber = %s'
        try:
            self.insert_and_update_sql(sql, enterpriseCount, projectNumber)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def update_evaluationReportNumber(self, evaluationReportNumber, projectNumber):  # 更新评标报告
        result = self.query_projectData(projectNumber=projectNumber)
        sql = 'update project set evaluationReportNumber = %s where projectNumber = %s'
        try:
            if result[7] < evaluationReportNumber:
                self.insert_and_update_sql(sql, evaluationReportNumber, projectNumber)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def update_applyNumber(self, applyNumber, projectNumber):  # 更新报名人数
        result = self.query_projectData(projectNumber=projectNumber)
        number = result[5]  # 报名人数
        sql = 'update project set applyNumber = %s where projectNumber = %s'
        try:
            if number < applyNumber:
                self.insert_and_update_sql(sql, applyNumber, projectNumber)
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def query_projectData(self, projectNumber):  # 查询项目数据
        sql = 'select projectType,tenderOrganizationType,evaluationBidWay,judgeNumber,tenderWay,applyNumber,enterpriseCount,evaluationReportNumber from project where projectNumber = %s'
        try:
            result = self.query_sql(sql, projectNumber)
            return result[0]
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)

    def select_expert(self, projectNumber):  # 查询专家数据库
        expert_name = []
        expert_username = []
        expert_password = []
        conn, cursor = self.connect_mysql()  # 连接数据库
        sql = 'select username,password,judgeName from expert where projectNumber = %s'
        try:
            cursor.execute(sql, projectNumber)
            result = cursor.fetchall()
            for i in result:
                expert_username.append(i[0])
                expert_password.append(i[1])
                expert_name.append(i[2])
            return expert_username, expert_password, expert_name
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)
        conn.close()
        cursor.close()

    def select_expert_username(self, projectNumber, judgeName):  # 查询专家身份证号
        conn, cursor = self.connect_mysql()  # 连接数据库
        sql = 'select username from expert where projectNumber = %s and judgeName = %s'
        try:
            cursor.execute(sql, (projectNumber, judgeName))
            expert_username = cursor.fetchone()
            return expert_username
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)
        conn.close()
        cursor.close()

    def select_isAgree(self, username, projectNumber):
        conn, cursor = self.connect_mysql()  # 连接数据库
        sql = 'select isAgree from expert where username = %s and projectNumber = %s'
        try:
            cursor.execute(sql, (username, projectNumber))
            expert_isAgree = cursor.fetchone()
            return expert_isAgree
        except(Exception, BaseException):
            error = traceback.format_exc()
            self.logger.debugText(projectNumber, error)
        conn.close()
        cursor.close()
