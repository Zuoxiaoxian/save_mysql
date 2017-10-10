#-*-coding:utf-8 -*-
import sys
import redis
reload(sys)
sys.setdefaultencoding("utf-8")



class RedisSave(object):
    def __init__(self,**kwargs):
        '''
        连接redis数据库
        '''
        self.handler = redis.Redis(host='localhost', port=6379, db= 1)
    def redissave(self, *args):
        print 'Redis数据库已连接,正在保存....'
        self.handler.set('name',args,ex=60*5)
        print '数据保存成功  !'


if __name__ == '__main__':
    print "在保存之前,请确保存在数据库 !"
    resave = RedisSave()
    a = ['123', 'qq', 'ww', 'ee', 'rr', 'aa', 'ss', 'dd']
    resave.redissave(a)
