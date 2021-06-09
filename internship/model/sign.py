#encoding=utf-8
import requests
import json
import MySQLdb
import urllib.parse
from .mysql_con import sql
#from .sendemail import mysendmail

mysql = sql()
# sendmessage = mysendmail()

headers = {
    'Host': 'weijiao.scitc.com.cn',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://weijiao.scitc.com.cn',
    'User-Agent': 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x1700112a) NetType/4G Language/zh_CN',
    'Referer': 'http://weijiao.scitc.com.cn/weixin_DingGang_Stu_AddInfor.php?'
}

data = {
	'type': 'type',
	'body': 'body',
	'Content': 'Content',
	'openid': 'openid',
	'action': 'save',
	'Submit': '%CC%E1++%BD%BB',
	'latitude': 'latitude',
	'longitude': 'longitude',
	'speed': '-1',
	'accuracy': '65',
	'networkType':'wifi'
}

url = "http://weijiao.scitc.com.cn/weixin_DingGang_Stu_AddInfor.php?openid="

def get_user_info(mysql):
    sql_order = "SELECT * FROM user;"
    mysql.cursor.execute(sql_order)
    res = mysql.cursor.fetchall()
    return res

def to_gb(s):
    res = str(s.encode('gb2312')).replace(r'\x', '%').upper()
    res = res.replace("B'", '').replace("'", '')
    return res

def submitsign(stu, _type, body, content, latitude, longitude):
    data['openid'] = stu
    data['type'] = to_gb(_type).encode(encoding='gb2312')
    data['body'] = to_gb(body).encode(encoding='gb2312')
    data['Content'] = to_gb(content).encode(encoding='gb2312')
    data['latitude'] = latitude
    data['longitude'] = longitude
    post_data = urllib.parse.urlencode(data)
    post_data = post_data.replace("%25", '%')
    # print(post_data)
    res = requests.post(url, data=post_data, headers=headers)
    res.encoding = res.apparent_encoding
    # print(res.text)
    if "成功" in res.text:
        print('签到提交成功')
        return True
    else:
        print("签到提交失败")
        print(res.text)
        return False

def signmain():
    users_data = get_user_info(mysql)
    colums = ['stu', 'ID', 'email', 'name', 'School_TeacherDepartName', 'School_TeacherName', 'Tel', 'ShiXi_Company', 'ShiXi_Duty', 'ShiXi_Teacher', 'ShiXi_TeaTel', 's1', 's2', 's3', 'longitude', 'latitude', 'type', 'body', 'content', 'switcher']
    for i in users_data:
        user = {}
        for x,y in zip(colums,i):
            user[x] = y
        if user['switcher'] == '0':
            continue
        print('CURRENT USER:', user['stu'])
        submit_flag = submitsign(user['stu'], user['type'], user['body'], user['content'], user['latitude'], user['longitude'])
    print('ALL COMPLETE')

if __name__ == "__main__":
    signmain()
