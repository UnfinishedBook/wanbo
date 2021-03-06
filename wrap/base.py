# -*- coding: utf-8 -*-

from gl import *
import pymysql.cursors

class DB:

    def __init__(self, host='localhost', port=3306, db=None, user='root', pwd='root'):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db, 
                charset='utf8', cursorclass=pymysql.cursors.DictCursor) 
        self.name = '%s.%d.%s' % (host,port,db)
        GL.LOG.info('数据库连接(%s)已建立' % self.name)
        self.count_success = 0
        self.count_failed = 0

    def __del__(self):
        self.conn.close()
        GL.LOG.info('数据库连接(%s)已断开' % self.name)

    def resetCount(self):
        self.count_success = 0
        self.count_failed = 0

    def getCount(self):
        return (self.count_success,self.count_failed)

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def exec(self, sql, commit=True):
        #GL.LOG.debug('sql: ' + sql)
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                if commit:
                    self.conn.commit()
                self.count_success += 1
                return True
        except:
            self.count_failed += 1
            GL.LOG.error('在数据库(%s)执行语句(%s)失败\n%s' % (self.name,sql,traceback.format_exc()))
            self.conn.rollback()
            return False

    def query(self, sql):
        #GL.LOG.debug('sql: ' + sql)
        result = []
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
                result.extend(cur.fetchall())
                self.count_success += 1
                return result
        except:
            self.count_failed += 1
            GL.LOG.error('在数据库(%s)执行语句(%s)失败\n%s' % (self.name,sql,traceback.format_exc()))
            return False

