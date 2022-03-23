# Python Script Created by MRSlou
#天使动漫2022四月番投票排名数据

import urllib.request
from lxml import etree
import time

def create_request():
    url='https://www.tsdm39.net/forum.php?mod=viewthread&tid=1093323'
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate, br'
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '', #自己填cookie
        'dnt': 1,
        'Host': 'www.tsdm39.net',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows"'',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'sec-gpc': 1,
        'Upgrade-Insecure-Requests': 1,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    # proxy={'http':''}
    # handler = urllib.request.ProxyHandler(proxies=proxy)  # 获取handler对象
    # opener = urllib.request.build_opener(handler)  # 获取opener对象
    # response = opener.open(request)  # 调用open方法
    response=urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download(content):
    parser = etree.HTMLParser(encoding="utf-8")
    tree=etree.HTML(content,parser=parser)
    name_list=tree.xpath('//table[@summary="poll panel"]//label/text()') #获取番剧名
    result_list=tree.xpath('//table[@summary="poll panel"]//em/text()') #获取投票数
    for i in range(0,len(name_list)):
        name_list[i]=str("".join(name_list[i].split())) #去除空格符\xa0
        name_list[i]=name_list[i].replace(str(i+1)+".","") #去除序号
        result_list[i]=result_list[i].replace("(","").replace(")","") #去除数据所带括号
        result_list[i]=int(result_list[i])
    dic=dict(zip(name_list,result_list))
    return dic

def localize(dic):
    dat=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    # for j in range(len(dat)): #调试用
    #     print(dat[j]) #调试用
    fp=open('Data.txt','w',encoding='utf-8')
    fp.write('天使动漫论坛人气排名:\n')
    localtime = time.asctime(time.localtime(time.time())) #获取系统时间
    fp.write("统计时间为 :"+str(localtime)+'\n')
    for item in range(len(dat)):
        str1=str(item+1)+'.'+dat[item][0]+':'+str(dat[item][1])
        fp.write(str1+'\n')
    fp.close()

if __name__=='__main__': #程序入口
    request=create_request() #获取响应
    content=get_content(request) #获取网页内容
    dic=download(content) #解析数据
    localize(dic) #本地化
