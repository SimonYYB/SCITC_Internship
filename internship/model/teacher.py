from collections import OrderedDict
from urllib3 import encode_multipart_formdata
import requests
class teacher():
    def __init__(self):
        self.headers = {
            'Host': 'weijiao.scitc.com.cn',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryABCDEFGHIJKLMNOP',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x1700112a) NetType/4G'
        }
    def bind_teacher(self, stu, depart, teacher):
        self.params = OrderedDict([
                ("editteacher", (None, '1')),
                ("School_TeacherDepartName", (None, depart.encode(encoding='gb2312'))),
                ('School_TeacherName', (None, teacher.encode(encoding='gb2312'))),
                ('UserName', (None, stu)),
                ('openid', (None, stu)),
                ('action', (None, 'save')),
                ('Submit', (None, '保  存'.encode(encoding='gb2312')))
            ])
        data = encode_multipart_formdata(self.params, boundary='----WebKitFormBoundaryABCDEFGHIJKLMNOP')
        res = requests.post('http://weijiao.scitc.com.cn/weixin_DingGang_Stu_TeacherInfor.php', data=data[0], headers=self.headers)
        res.encoding = res.apparent_encoding
        if '成功' in res.text:
            return True
        else:
            return False

if __name__ == "__main__":
    teacher = teacher()
    if teacher.bind_teacher('', '', ''):
        print('绑定老师成功')
    else:
        print('绑定老师失败')