#获取数据库连接
import pymysql.cursors

connection = pymysql.connect(
    host='192.168.21.10',
    user='root',
    password='root',
    db='yaolhPython',
    charset='utf8mb4'
)

try:
    #获取绘画指针
    with connection.cursor() as curser:
        #创建sql语句
        sql="select `urlname`,`urlhref` from `urls` where `id` is not null"
        #执行sql语句
        rs=curser.execute(sql)
        print(rs)
        #提交
        # result=curser.fetchall()
        result=curser.fetchmany(2)
        print(result)
finally:
    connection.close()