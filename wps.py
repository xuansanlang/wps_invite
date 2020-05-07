import requests


def wps_invite(sid: str) -> None:
    invite_url = 'http://zt.wps.cn/2018/clock_in/api/invite'
    s = requests.session()
    invite_users = {
        'Gyan': 698591042,
        '......': 589431441,
        '牧童': 336149595,
        '海宁': 317351847,
        #'Oumuamua': 355435909,
        'ik':395070149,
        '听听那冷雨':244784190,
        '土土1':255151061,
        '一点':190222315,
        'LauShyO':261715701,
        '收到！':353960616,
        '@lh':240594027,
        '土土':200156776,

    }
    for index,invite_userid in enumerate(invite_users.values()):
        headers = {
            'sid': sid
        }
        r = s.post(invite_url, headers=headers, data={
            'invite_userid': invite_userid})
        print("ID={}, 状态码: {}, 请求信息{}".format(list(invite_users.keys())[index], r.status_code, r.text))


if __name__ == '__main__':
    sid = 'V02Sq_6LRIXLO_ZBvvQmerlwkDfbiZM014f4267a0012ea67a7'
    wps_invite(sid)