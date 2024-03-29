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


class SslCertModel(object):

    def __init__(self, certId=None, certName=None, commonName=None, certType=None, startTime=None, endTime=None, deletable=None, digest=None, aliasName=None, dnsNames=None, downloadable=None):
        """
        :param certId: (Optional) 证书Id
        :param certName: (Optional) 证书名称
        :param commonName: (Optional) 绑定域名
        :param certType: (Optional) 证书类型
        :param startTime: (Optional) 开始时间
        :param endTime: (Optional) 结束时间
        :param deletable: (Optional) 是否允许被删除,1允许,0不允许
        :param digest: (Optional) 对私钥文件使用sha256算法计算的摘要信息
        :param aliasName: (Optional) 证书别名
        :param dnsNames: (Optional) 域名
        :param downloadable: (Optional) 是否允许被下载,0->不允许,1->允许
        """

        self.certId = certId
        self.certName = certName
        self.commonName = commonName
        self.certType = certType
        self.startTime = startTime
        self.endTime = endTime
        self.deletable = deletable
        self.digest = digest
        self.aliasName = aliasName
        self.dnsNames = dnsNames
        self.downloadable = downloadable
