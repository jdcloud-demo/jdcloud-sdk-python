# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class DomainInfo(object):

    def __init__(self, id=None, domainName=None, createTime=None, expirationDate=None, packId=None, packName=None, resolvingStatus=None, creator=None, jcloudNs=None, lockStatus=None):
        """
        :param id: (Optional) 域名的唯一ID
        :param domainName: (Optional) 域名字符串
        :param createTime: (Optional) 创建时间，格式Unix timestamp，时间单位：毫秒
        :param expirationDate: (Optional) 过期时间，格式Unix timestamp，时间单位：毫秒
        :param packId: (Optional) 套餐类型，免费:0 企业版:1 企业高级版:2
        :param packName: (Optional) 套餐的名字
        :param resolvingStatus: (Optional) 解析的状态, 暂无解析:1，正常解析:2， 部分解析:3， 暂停解析:4 NS未修改:5
        :param creator: (Optional) 创建者
        :param jcloudNs: (Optional) 是否是京东云资源
        :param lockStatus: (Optional) 域名的锁定状态，0:未锁定， 1:已锁定
        """

        self.id = id
        self.domainName = domainName
        self.createTime = createTime
        self.expirationDate = expirationDate
        self.packId = packId
        self.packName = packName
        self.resolvingStatus = resolvingStatus
        self.creator = creator
        self.jcloudNs = jcloudNs
        self.lockStatus = lockStatus
