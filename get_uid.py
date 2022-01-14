from  url_mange import Urlmanage
import requests
class get_uid(object):
    def userid(self,data,qua):
        list_id = []
        url="https://www.pixiv.net/ajax/user/%s/following?offset=0&limit=%s&rest=show&tag=&lang=zh"%(data,qua)
        a=requests.get(url,headers=Urlmanage().head1())
        j=a.json()
        l=j['body']['users']
        for i in l:
            list_id.append(i['userId'])
        print(list_id)
        # print(list_id)
        return list_id

