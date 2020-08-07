# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
import requests


class BaseApi:
    def request_api(self, reqData: dict):
        # 使用request 完成多请求的改造（get、post、delete）
        return requests.request(**reqData).json()
