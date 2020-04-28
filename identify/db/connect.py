from typing import Dict

import redis
import pymysql
from pydantic import BaseModel




pool = redis.ConnectionPool(host='127.0.0.1')
red = redis.Redis(connection_pool=pool)





def read(num):
    '''读取数据库'''
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='identify',
                           charset='utf8')

    # 创建一个游标
    cursor = conn.cursor()
    # 查询数据
    sql = "select code from pics where num = %s "
    cursor.execute(sql, str(num))  # 执行sql
    result_1 = cursor.fetchone()
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result_1[0]


if __name__ == '__main__':
    d = read(1)
    print(d)
