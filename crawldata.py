# encoding:utf-8
import os
import re
import requests
import time
import traceback
from bs4 import BeautifulSoup

dest = 'Dict_data/eywedu.txt'
file = open(dest,'a')
errorLog = 'Dict_data/errorlog.txt'
error=open(errorLog,'a')
#dest.writelines("test route")
class CrawlData:
    def getPageFromEywedu(self):
        for i in range(1,3891):
            try:
                headers = {
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Connection':'keep-alive',
                    'Accept-Encoding':'gzip,deflate',
                    'Accept-Language':'zh-CN;zh;q=0.9',
                    'Cache-Control':'no-cache',
                    'Cookie':'yunsuo_session_verify=8acc0e490871ca1890f055c098802b99; srcurl=687474703a2f2f67772e6579776564752e636f6d2f; security_session_mid_verify=33db8cd4f01f007881baabc207de6fef; ASPSESSIONIDSAQRSBDA=DHODJFBCBKLFIHPPCIKOFGDG; bdshare_firstime=1521792963606; UM_distinctid=16251edd47551c-0762ab8b2cc3d7-b34356b-1fa400-16251edd476434; __51cke__=; CNZZDATA1253626516=1912009951-1521790879-http%253A%252F%252Fgw.eywedu.com%252F%7C1521801679; __tins__5086540=%7B%22sid%22%3A%201521804104217%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201521806423782%7D; __tins__4317214=%7B%22sid%22%3A%201521804104223%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201521806423788%7D; __51laig__=42',
                    'Pragma':'no-cache',
                    'Upgrade-Insecure-Requests':'1',
                    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
                }
                link = "http://gw.eywedu.com/cat.asp?id=" + str(i)
                # req = requests.get(link,headers=headers).decoding('gb2312')
                req = requests.get(link, headers=headers)
                req = req.content.decode('gbk')
                # print(req)
                soup = BeautifulSoup(req, 'html.parser')
                # print(soup.prettify())
                lists = soup.find_all(align='left')
                lists = lists[0:2]
                wenzi = lists[0].string
                shiyi = lists[1].contents
                # print(wenzi)
                shiyi = shiyi[0::2]
                # print(type(shiyi))
                file.writelines(wenzi + '\n')
                print(shiyi)
                for j in shiyi:
                    file.writelines('  ' + j + '\n')
                success = True
                if(i%19==0):
                    time.sleep(5)
                else:
                    time.sleep(0.1)
            except UnicodeDecodeError:
                print(UnicodeDecodeError)
            except UnicodeEncodeError:
                print(UnicodeEncodeError)
            except UnicodeError:
                print(UnicodeError)
                error.writelines("UnicodeError")
            except Exception :
                error.writelines('Errors occur on page '+str(i) +'\n')
        file.close()
        error.close()
if __name__ == '__main__':
    one_Instance = CrawlData()
    one_Instance.getPageFromEywedu()