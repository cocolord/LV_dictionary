# encoding:utf-8
import os
import re
import requests
import time
import traceback
from bs4 import BeautifulSoup
from selenium import webdriver

errorLog = 'errorlog.txt'
error=open(errorLog,'w')
#dest.writelines("test route")
class CrawlData:
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN;zh;q=0.9',
        'Cache-Control': 'no-cache',
        'referer': 'https: // so.gushiwen.org / guwen / book_5.aspx',
        'Cookie': 'ASP.NET_SessionId=4eldiva2okx4sqsz4yj2rohj; Hm_lvt_04660099568f561a75456483228a9516=1523426768; Hm_lpvt_04660099568f561a75456483228a9516=1523429161',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    def getPageFromYuanwen(self):
        for i in range(1,18000):
            try:
                Adest = 'Article/'+str(i)+'.txt'
                with open(Adest, 'w',encoding='utf-8')  as Afile:
                    Alink = "https://so.gushiwen.org/guwen/bookv_" + str(i) +'.aspx'
                    Areq = requests.get(Alink, headers=self.headers).text
                    Asoup = BeautifulSoup(Areq, 'html.parser')
                    AA=Asoup.find('div',class_="contson")
                    AA = AA.get_text()
                    Afile.writelines(AA)
                    try:
                        Ttag = Asoup.find(id=re.compile("leftbtn"))['id']
                        Ttag = Ttag[7:]

                        Tlink = "https://so.gushiwen.org/guwen/ajaxbfanyi.aspx?id=" + Ttag
                        Treq = requests.get(Tlink, headers=headers).text
                        Tsoup = BeautifulSoup(Treq, 'html.parser')
                        Tsoup = Tsoup.get_text()
                        # print(Tsoup)
                        res_tr1 = r'全屏\n\n\n(.*)参考资料'
                        Tsoup = re.findall(res_tr1, Tsoup, re.S | re.M)
                        Tdest = 'Translation/' +str(i) + 'trans' + '.txt'
                        if(Tsoup):
                            with open(Tdest, 'w', encoding="utf-8") as Tfile:
                                Tfile.writelines(Tsoup)
                    except:
                        pass
            except Exception :
                error.writelines('Errors occur on page '+str(i) +'\n')

    def getShiWen(self):
        try:
            count = 1
            for i in range(1,1000):
                url = "https://www.gushiwen.org/shiwen/default_0A0A" + str(i) + ".aspx"
                Sreq = requests.get(url, headers=self.headers).text
                Ssoup = BeautifulSoup(Sreq, 'html.parser')
                contest = Ssoup.find_all('div',class_="contson")
                # print(contest)
                target_list = []
                for item in contest:
                    target = item["id"]
                    target = target[7:]
                    target_list.append(target)
                print(target_list)
                for times in range(0,10):
                    Sdest = 'Shiwen/' + str(count) + '.txt'
                    with open(Sdest,'w',encoding='utf-8') as Sfile:
                        try:
                            target_url = "https://so.gushiwen.org/shiwen2017/ajaxshiwencont.aspx?id=" + target_list[times] + "&value=yi"
                            req = requests.get(target_url,headers=self.headers).text
                            # print(req)
                            res_tr = r'<br /><span style="color:#76621c;">(.*?)</span>'
                            text = re.findall(res_tr,req,re.S|re.M)
                            # print(text)
                            output = ""
                            for item in text:
                                output+=item
                            print(output)
                            Sfile.writelines(output)
                            count = count + 1
                        except:
                            pass
        except:
            pass
if __name__ == '__main__':
    one_Instance = CrawlData()
    # one_Instance.getPageFromYuanwen()
    one_Instance.getShiWen()