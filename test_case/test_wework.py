# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
from api.wework import WeworkApi


class TestWework:
    def test_getToken(self):
        corpsecret = "xSDP_WU3oOxVWX3gFCM22B1KPftYbEXDW2uDOkszN9w"
        print(WeworkApi().getToken(corpsecret))
