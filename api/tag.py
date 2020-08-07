# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
from api.base_api import BaseApi
from api.wework import WeworkApi


class Tag(BaseApi):
    corpsecret = 'xSDP_WU3oOxVWX3gFCM22B1KPftYbEXDW2uDOkszN9w'

    # 进行初始化
    def __init__(self):
        self.token = WeworkApi().getToken(self.corpsecret)

    # 查询标签
    def getTag(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": []
            }
        }
        return self.request_api(data)

    # 添加标签
    def addTag(self, name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_name": "test",
                "tag": [
                    {
                        "name": name
                    }
                ]
            }
        }
        return self.request_api(data)

    # 更新标签（编辑标签)
    def editTag(self, tagId, name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": tagId,
                "name": name
            }
        }
        return self.request_api(data)

    # 删除标签
    def deleteTag(self, tagId):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [tagId]
            }
        }
        return self.request_api(data)
