# -*- coding: utf-8 -*-
import json
import time
from lib.platform.tencent_sdk_302.openapi_v3 import OpenAPIV3
__author__ = 'du_du'

appid = 1106233605
appkey = 'STwl4MAK67bcemOd'
iplist = ('openapi.sparta.html5.qq.com',)


# 获取推荐的好友列表
def get_app_friends(openid, openkey):
    api = OpenAPIV3(appid, appkey, iplist)
    pf = 'qzone'
    j_data = api.call('/v3/relation/get_app_friends', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey
    })
    return j_data


def is_friend(openid, openkey, fopenid):
    api = OpenAPIV3(appid, appkey, iplist)
    pf = 'qzone'
    j_data = api.call('v3/relation/is_friend', {
        'pf': pf,
        'openid': openid,
        'openkey': openkey,
        'fopenid': fopenid
    })
    return j_data

