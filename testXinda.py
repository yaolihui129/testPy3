from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pymysql
import re
resp=urlopen("http://www.zhihuixinda.com").read().decode("utf-8")
soup=bs(resp,"html.parser")
listUrls=soup.findAll("a",href=re.compile("^/index.php/"))
for url in listUrls:
    if not re.search("\.(jpg|JPG)$",url["href"]):
        print(url.get_text(),"<----->",url["href"])
        #获取数据库连接
        connection = pymysql.connect(
            host='192.168.21.10',
            user='root',
            password='root',
            db='yaolhPython',
            charset='utf8mb4'
        )

        try:
            with connection.cursor() as curser:
                #创建sql语句
                sql="insert into `urls`(`urlname`,`urlhref`)values(%s,%s)"
                #执行sql语句
                curser.execute(sql,(url.get_text(),url["href"]))
                #提交
                connection.commit()
        finally:
            connection.close()