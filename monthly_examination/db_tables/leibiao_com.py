"""
爬取站点:  http://www.liebiao.com/
++++++++++++++++++++++友情提醒: 使用代理ip
++++++++++++++++++++++考虑1: 增量式爬取设计(加分项)
++++++++++++++++++++++考虑2: 去重(加分项)
运行, 展示效果
{{{{{{{要点}}}}}}}}
抓取所有城市信息(共30分);
1.1用Django建城市信息模型City, 用drf完成城市信息创建和城市列表展示接口 (10分)
1.2写爬虫爬取 所有城市的信息, 通过 城市信息创建接口, 把数据存入mysql中 (10分)
1.3要求 展示城市信息列表展示接口, 每页展示15条信息 (5分)
1.4xadmin后台展示 城市模型City, 并展示所有字段 (5分)
+++++++++++++++
2, 爬取某一城市的舞蹈培训分页链接 (共40分):
2.1 用Django建  舞蹈培训分页信息模型 DancePage,  与 城市信息模型City 外键关联(一个城市对应多个分页连接), 用drf完成 舞蹈培训分页信息创建 和 列表展示接口(10分)
2.2 写爬虫爬取 所属城市中舞蹈培训的分页连接, 通过 舞蹈培训分页信息创建接口, 把数据存入mysql中(10分)
2.3 根据城市id, 可以查看所属城市的 分页链接信息列表展示接口, 每页10个分页连接信息(5分)
2.4  xadmin后台展示 模型DancePage, 并展示所有字段(5分)
2.5  能够获取正确的分页数量(10分)
"""


import requests
import os,time,random
from lxml import etree
import datetime
import pymysql  #导入MySQL数据库
#用户名：root 密码：123123 数据库名：yuekao
db = pymysql.connect("127.0.0.1","root","123123","yuekao",charset="utf8")
cursor = db.cursor() #创建游标
print(db) #测试数据库连接成功还是失败----
def daili(): #代理
    pass
headers1={
    'Referer': 'http://anshan.liebiao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.53 Safari/537.36',
          } #handers=浏览器头部
cookies = {'Cookie': 'acw_tc=276aede315477067723695230e22394c27bc98d2a4da34d330261d69fc7482; _uv_id=168559515917710255; default_city=494; cities_last_visited=494; insert_cityandcate_record=494%2C1; Hm_lvt_d1c8e5c1164dcc070ae572bcabfe773f=1547706772,1547708071; lbids=ki7kd7df; _z=o18j97i0m0g2vlb07u8tdu2ga0; _csrf=MOFb3VFATsWnh7YvcEzq00VJZamd_fiy; _referid=0; _i=8801183; _u=u8801183; _p=LslfL3CixsQzLWQY89YRepQAxQ; Hm_lpvt_d1c8e5c1164dcc070ae572bcabfe773f=1547709361; root=1'}
def hanshu(url):#主函数=requests/请求
    ks = datetime.datetime.now()     #=====开始时间
    response = requests.get(url=url,headers=headers1,cookies=cookies,timeout=5) #求情头==
    js = ks-datetime.datetime.now() #=====结束时间
    print('状态码%',response.status_code,'时间%',js) #返回状态码===结果
    jx = etree.HTML(response.text)    #
    # city = jx.xpath('//div[4]/dl/dd/a//text()') #====解析所有城市名字
    # print(city,'______','数量/',len(city))    #===//div[4]/dl/dd/a//text()===一共城市数量是363
    # #数据写入数据库#######
    # for i in city:
    #     date1 = ("insert into demo_apps1_city_info(city) values (%s)")
    #     try:
    #         cursor.execute(date1,i)
    #         db.commit();  # 提交操作
    #         print('写入成功')
    #     except:
    #         db.rollback();
    #         print('失败')
    citi = ''.join(jx.xpath('//div[4]/dl[1]/dd/a[1]/@href')) # 莫城市的url链接
    print(citi)#鞍山城市的url链接
    response1 = requests.get(url=citi,headers=headers1,cookies=cookies,timeout=10) #鞍山下请求
    print('状态码%',response1.status_code) #返回状态码===结果
    list1 = []
    for page in range(1,16): #设置分页#循环列表  #双循环成自己需要的格式  ===送代方法
        urlp = str(citi)+'sou/%E8%88%9E%E8%B9%88/?pn='+str(page) #拼接====舞蹈培训===url
        # print(urlp)   #显示分页结果
        # print(urlp,'url结果')#url拼接成功
        list1.append(urlp) #添加列表
    # # 数据写入数据库#######
    # for i in list1:
    #     date1 = ("insert into demo_apps1_url_info(url) values (%s)")
    #     try:
    #         cursor.execute(date1, i)
    #         db.commit();  # 提交操作
    #         print('写入成功')
    #     except:
    #         db.rollback();
    #         print('失败')
    # print(list1)
    list2 = []
    for wudao in list1:#循环列表  #双循环成自己需要的格式  ===送代方法
        response2 = requests.get(url=wudao,headers=headers1,cookies=cookies,timeout=10) #舞蹈页面请求头
        print('状态码',response2.status_code)
        jx2 = etree.HTML(response2.text)
        url2 = ''.join(jx2.xpath('//div[3]/div/div[3]/div[1]/div[1]/ul/li/h3/a//@href')) #url结果
        # print(url2,len(url2))
        list2.append(url2) #添加到列表
        time.sleep(1)   #添加睡眠时间防止IP被封
    print(len(list2))
    list3 = []
    for urlu in list2: #循环列表  #双循环成自己需要的格式  ===送代方法
        urla = urlu.split('http:')
        for urla in urla:
            print(urla,'已就绪')
            list3.append(urla) #添加列表
    # print(list3,'------')
    # # 数据写入数据库#######
    # for i in list3:
    #     date1 = ("insert into demo_apps1_urls_info(ci_id,urls) values (1,%s)")
    #     try:
    #         cursor.execute(date1, i)
    #         db.commit();  # 提交操作
    #         print('写入成功')
    #     except:
    #         db.rollback();
    #         print('失败')
    num = 1
    for xian in list3:
        num =num+1
        if len(xian) >=47: #判断url长度进行拼接
            xian1 = 'http:'+str(xian)
            print(xian1,'已就绪')
            response3 = requests.get(xian1,headers=headers1,cookies=cookies,timeout=10)
            print('状态码',response3.status_code)
            jx3 = etree.HTML(response3.text)
            title = ''.join(jx3.xpath('//div[4]/div[1]/div[1]/div[1]/div[1]/h1//text()'))
            lei = ''.join(jx3.xpath('//div[4]/div[1]/div[1]/div[3]/div[2]/div[1]/dl[1]/dd/a//text()'))
            wei = ''.join(jx3.xpath('//div[4]/div[1]/div[1]/div[3]/div[2]/div[1]/dl[2]/dd//text()'))
            lian = ''.join(jx3.xpath('//div[4]/div[1]/div[1]/div[3]/div[2]/dl[2]/dd/span//text()'))
            xiangqing = ''.join(jx3.xpath('//div[4]/div[1]/div[1]/div[4]/div[2]//text()'))
            mobile = ''.join(jx3.xpath('//div[4]/div[1]/div[1]/div[3]/div[2]/div[2]/div/ul/li[1]/div/p[1]/span//text()'))
            print('第--{',format(num),'}--条数据','标题--',title,'类型--',lei,'位置---',wei,'联系人---',lian,'手机号',mobile,'详情--',xiangqing,'%------%爬取成功')
            # # # 数据写入数据库#######
            # date1 = ("insert into demo_apps1_users_info(user_id,title,leixing,weizhi,lianxi,phone,xq) values ('{}','{}','{}','{}','{}','{}','{}')".format(num,title,lei,wei,lian,mobile,xiangqing))
            # try:
            #     cursor.execute(date1)
            #     db.commit();  # 提交操作
            #     print('第--{}--',format(num),'数据写入成功')
            # except:
            #     db.rollback();
            #     print('失败')
        time.sleep(3)
    time.sleep(3)
if __name__=='__main__':#主程序接口----------失误写错了--已改正
    hanshu('http://www.liebiao.com/')
