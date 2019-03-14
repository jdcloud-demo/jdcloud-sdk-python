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


class Certificate(object):

    def __init__(self, id=None, name=None, content=None, rsaKey=None, domain=None, from=None, to=None, sigAlgName=None, issuer=None, organization=None, uploadTime=None, associatedDomains=None, sanDomains=None):
        """
        :param id: (Optional) 证书 Id
        :param name: (Optional) 证书名称
        :param content: (Optional) 证书
        :param rsaKey: (Optional) 秘钥
        :param domain: (Optional) 绑定域名
        :param from: (Optional) 证书生效时间
        :param to: (Optional) 证书到期时间
        :param sigAlgName: (Optional) 加密算法
        :param issuer: (Optional) 颁发者
        :param organization: (Optional) 颁发给
        :param uploadTime: (Optional) 上传时间
        :param associatedDomains: (Optional) 已关联域名
        :param sanDomains: (Optional) 推荐域名
        """

        self.id = id
        self.name = name
        self.content = content
        self.rsaKey = rsaKey
        self.domain = domain
        self.from = from
        self.to = to
        self.sigAlgName = sigAlgName
        self.issuer = issuer
        self.organization = organization
        self.uploadTime = uploadTime
        self.associatedDomains = associatedDomains
        self.sanDomains = sanDomains
