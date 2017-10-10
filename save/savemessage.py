#-*-coding:utf-8 -*-
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding("utf-8")

class MysqlSave(object):
    '''
    mysql:mysql数据库
    redis:redis数据库
    csv:csv文件
    sqllite3:sqllite数据库
    '''
    def __init__(self):
        self.db = MySQLdb.connect(host='localhost', passwd='123456', user='root',charset='utf8',use_unicode=True, db='boledb')
        self.cursor = self.db.cursor()
        #title,time,ji_shu,fen_lei,dian_zan,shu_cang,ping_lun
        sql = "create table if not exists bole(id INTEGER primary key auto_increment NOT NULL , title VARCHAR (100), `time` VARCHAR (20),ji_shu VARCHAR (10), fen_lei VARCHAR (20),dian_zan VARCHAR (20), shu_cang VARCHAR (20),ping_lun VARCHAR (20),message MEDIUMTEXT)"
        self.cursor.execute(sql)
        self.db.commit()
    def mysql(self,*arge):
        print "数据库已连接,正在存储...."
        sql = "insert into bole(title,`time`,ji_shu,fen_lei,dian_zan,shu_cang,ping_lun,message) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql,arge)
        self.db.commit()

    def __del__(self):
        print "保存完成 !"
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    print "保存之前,请检查你的数据库是否创建了"
    mysqlsave = MysqlSave()
    a = ['123','qq','ww','ee','rr','aa','ss','dd']
    mysqlsave.mysql(*a)