# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
from api.base_api import BaseApi


class WeworkApi(BaseApi):
    # 企业id
    corpId = 'ww6c619306416691d9'

    # 获取token
    def getToken(self, corpsecret):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": self.corpId,
                "corpsecret": corpsecret
            }
        }
        # 将获取的token值进行返回
        return self.request_api(data)["access_token"]
