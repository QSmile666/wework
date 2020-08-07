# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
import json

from api.tag import Tag
from jsonpath import jsonpath


class TestTag:
    def setup(self):
        self.tag = Tag()

    # 整个流程跑
    def test_all(self):
        # 获取标签名字为zhangsan的标签id
        tag_id = jsonpath(self.tag.getTag(), '$..tag[?(@.name=="zhangsan")].id')
        # 如果标签id存在，则删除
        if tag_id:
            self.tag.deleteTag(tag_id[0])
        # 添加标签id
        self.tag.addTag("zhangsan")
        # 获取标签名字为zhangsan的标签id
        tag_id = jsonpath(self.tag.getTag(), '$..tag[?(@.name=="zhangsan")].id')
        self.tag.editTag(tag_id[0], "wangwu")

    def test_getTag(self):
        print(json.dumps(Tag().getTag(), indent=2))

    def test_addTag(self):
        print(Tag().addTag("tagName3"))

    def test_editTag(self):
        print(Tag().editTag("etjN3BBwAAv-FpTaZp2iTfgxgOv3ZOnw", "zhangsan"))

    def test_deleteTag(self):
        print(Tag().deleteTag("etjN3BBwAA-nIOzsPbyu_1-PqfS-9_OQ"))
