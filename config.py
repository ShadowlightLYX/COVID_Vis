# -*- coding: utf-8 -*-

DIALECT = 'mysql'  # 要用的什么数据库
DRIVER = 'pymysql' # 连接数据库驱动
USERNAME = 'root'  # 用户名
PASSWORD ='111111'  # 密码
HOST = '127.0.0.1'  # 服务器
PORT ='3306' # 端口
DATABASE = 'cov' # 数据库名
 
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False