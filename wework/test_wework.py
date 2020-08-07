# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee

import requests
import random


class TestWeworkApi:
    corpid = 'ww6c619306416691d9'
    corpsecret = '2nWlaax4KBCNZZ9N0GNw1LhkpZx3qfBcKLKMlCj02O8'

    def setup(self):
        r = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}")
        # print(r.json())
        self.token = r.json()["access_token"]
        print(r.json()["access_token"])

    def test_wework_member(self):
        return

    def test_wework_depart(self):
        # 获取部门列表
        get_dept = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}")
        print(get_dept.json())

        # 删除部门
        dept_id = 11
        res_data = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={dept_id}")
        print(res_data.json())

        # 创建部门
        depart_data = {
            "name": "测试使用5",
            "name_en": "test5",
            "parentid": 1,
            "id": 15
        }
        res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}",
                            json=depart_data)
        print(res.json())

        # 更新部门
        updataDepart_data = {
            "id": 12,
            "name": "测试使用3",
            "name_en": "test3",
            "parentid": 1,
            "order": 3
        }

        res_updept = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}",
                            json=updataDepart_data)
        print(res_updept.json())