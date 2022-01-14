
import threading
import os
import multiprocessing
from url_mange import Urlmanage
from get_uid import get_uid
from get_pid import get_pid
import requests
import re
class gevent(object):
#     #代理池
#     def get_proxy(self):
#         result = []
#         # 读取代理池ip并随机返回一个
#         with open('ip_pool_home.txt', 'r') as f:
#             for line in f:
#                 result.append(line.strip('\n'))
#         ips = list(filter(None, result))
#         proxies = {'http': random.choice(ips)}
#         return proxies



    def pro(self,url,uid):
        os.mkdir('/Users/' + uid)
        print("url22222===%s"%url)
        # proxies=gevent().get_proxy()
        str=[]
        str2=[]
        urls=[]
        names=[]
        headers2=Urlmanage().head2()
        headers=Urlmanage().head1()
        res = requests.get(url, headers=headers)
        print("res===%s"%res)
        list = res.json()
        # print(list)
        # json.dumps(list,sort_keys=True,indent=2)
        for l in list:
            l = list['body']['works']

        # print(l)
        # print(l.keys)

        for i in l:

            urls.append(l[i]['url'])

            names.append(l[i]['title'])

        # print(urls)
        for a in urls:
            str.append(re.findall('img/(.*?)_p0', a))
        url_img = 'https://i.pximg.net/img-original/img/{}_p0.jpg'
        url_img2 = 'https://i.pximg.net/img-original/img/{}_p0.png'

        i = 0
        string = 'https://www.pixiv.net/artworks/{}'
        pattern = re.compile(r'/(\d{4}.*)')
        for astr in str:
            string2 = string.format(pattern.findall(astr[0])[0])  # referer主链接拼接字符串
            # string2 = string.format(astr[0][-8:])  # referer主链接拼接字符串
            print("astr==%s" % astr)
            print("string2==%s" % string2)
            headers2['referer'] = string2  # 将headers的referer更新为拼接好的链接地址，进行访问
            print(url_img.format(astr[0]))
            rrr = requests.get(url_img.format(astr[0]), headers=headers2)
            rrr2 = requests.get(url_img2.format(astr[0]), headers=headers2)
            if rrr.status_code == 200:
                with open('/Users/%s/%s.png' % (uid, i), 'wb+') as f:  ##默认的存储路径
                    # if rrr.status_code==200:

                    f.write(rrr.content)

                    print("%s下载成功\n" % names[i])

            else:
                with open('/Users/%s/%s.png' % (uid, i), 'wb+') as p:
                    p.write(rrr2.content)
                    print("%s下载成功\n" % names[i])
            i += 1
if __name__ == '__main__':
    date= input("请输入你的主页id: ")
    qua=input("请输入爬取的用户数: ")
    uids = get_uid().userid(data=date,qua=qua)
    print("uids===%s"%uids)
    pool = multiprocessing.Pool(processes=4) #进程池
    for uid in uids:
        pids = get_pid().getpid(uid=uid)
        url = 'https://www.pixiv.net/ajax/user/{uid}/profile/illusts?{pid}&work_category=illustManga&is_first_page=1&lang=zh'.format(
            uid=uid, pid=pids)
        # print("url===%s"%url)
        print("uid===%s"%uid)
        # print("pids===%s"%pids)
        pool.apply_async(gevent().pro, (url, uid))

    pool.close()
    pool.join()
