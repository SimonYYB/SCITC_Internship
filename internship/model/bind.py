#coding=utf-8
import requests
from .mysql_con import sql

mysql = sql()
class bind():
    def __init__(self):
        self.url = 'http://weijiao.scitc.com.cn/weixin_BangDingUser.php?'
        self.headers = {
            'Host': 'weijiao.scitc.com.cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://weijiao.scitc.com.cn',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x1700112a) NetType/WIFI Language/zh_CN',
            'Referer': 'http://weijiao.scitc.com.cn/weixin_BangDingUser.php?code=023zyzGa1CKRVz0ei5Ja1nHSWk1zyzGv&state=123'
        }
        self.data = {
            'UserName':'stu',
            'SFZ':'ID',
            'Submit':'%CC%E1+%BD%BB',
            'openid':'stu',
            'action':'save'
        }
    def do_bind(self, stu, ID, create=True):
        print('检测是否能够绑定')
        self.data['UserName'] = stu
        self.data['SFZ'] = ID
        self.data['openid'] = stu
        res = requests.post(self.url, data=self.data, headers=self.headers)
        res.encoding = res.apparent_encoding
        if "成功" in res.text:
            print('绑定成功')
            create_flag = False
            if create:
                create_flag = mysql.createUser(stu, ID)
            if create_flag:
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    bind = bind()
    if bind.do_bind('学号', '身份证号'):
        print('绑定成功')
    else:
        print('绑定失败')
