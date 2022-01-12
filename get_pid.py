import requests
from url_mange import Urlmanage
from get_uid import get_uid
class get_pid(object):
    def getpid(self,uid):
        url='https://www.pixiv.net/ajax/user/{uid}/profile/all?lang=zh'.format(uid=uid)
        l=requests.get(url,headers=Urlmanage().head1()).json()
        r=(l['body']['illusts'])
        # print(r)
        return 'ids[]='+'&ids[]='.join(r)

