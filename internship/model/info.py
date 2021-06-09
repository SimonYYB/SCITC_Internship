from collections import OrderedDict
from urllib3 import encode_multipart_formdata
import requests
class info():
    def __init__(self):
        self.headers = {
            'Host': 'weijiao.scitc.com.cn',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryABCDEFGHIJKLMNOP',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x1700112a) NetType/4G'
        }
    def do_info(self, stu, Tel, ShiXi_Company, ShiXi_Duty, ShiXi_Teacher, ShiXi_TeaTel, s1, s2, s3):
        self.params = OrderedDict([
                ("Tel", (None, Tel)),
                ("ShiXi_Company", (None, ShiXi_Company.encode(encoding='gb2312'))),
                ('ShiXi_Duty', (None, ShiXi_Duty.encode(encoding='gb2312'))),
                ('ShiXi_Teacher', (None, ShiXi_Teacher.encode(encoding='gb2312'))),
                ('ShiXi_TeaTel', (None, ShiXi_TeaTel)),
                ('TripQuYuChang', (None, 1)),
                ('s1', (None, s1.encode(encoding='gb2312'))),
                ('s2', (None, s2.encode(encoding='gb2312'))),
                ('s3', (None, s3.encode(encoding='gb2312'))),
                ('UserName', (None, stu)),
                ('openid', (None, stu)),
                ('action', (None, 'save')),
                ('Submit', (None, '保  存'.encode(encoding='gb2312')))
            ])
        data = encode_multipart_formdata(self.params, boundary='----WebKitFormBoundaryABCDEFGHIJKLMNOP')
        res = requests.post('http://weijiao.scitc.com.cn/weixin_DingGang_Stu_SelfInfor.php', data=data[0], headers=self.headers)
        res.encoding = res.apparent_encoding
        # print(res.text)
        if '成功' in res.text:
            return True
        else:
            return False

if __name__ == "__main__":
    info = info()
    if info.do_info('学号', '', '','','','','','',''):
        print('修改信息成功')
    else:
        print('修改信息失败')