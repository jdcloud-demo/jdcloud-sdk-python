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


class RecordDescDetail(object):

    def __init__(self, recordId=None, orderId=None, certName=None, brand=None, certType=None, domainCount=None, certValidity=None, commonName=None, state=None, canceledReason=None, recordValidate=None, corpName=None, corpAddr=None, dnsNames=None, email=None):
        """
        :param recordId: (Optional) 证书申购记录Id
        :param orderId: (Optional) 交易系统订单Id
        :param certName: (Optional) 证书名称
        :param brand: (Optional) 证书品牌
        :param certType: (Optional) 证书类型
        :param domainCount: (Optional) 域名个数
        :param certValidity: (Optional) 证书年限
        :param commonName: (Optional) 证书绑定域名
        :param state: (Optional) 证书状态,1:未支付,2:待补全信息,3:待下单,4:待域名验证,5:已完成,6:审核不通过,7:已取消
        :param canceledReason: (Optional) 分销商返回的信息，代表订单被取消的原因
        :param recordValidate: (Optional) 
        :param corpName: (Optional) 公司名称
        :param corpAddr: (Optional) 公司地址
        :param dnsNames: (Optional) 备用域名
        :param email: (Optional) 联系人邮箱
        """

        self.recordId = recordId
        self.orderId = orderId
        self.certName = certName
        self.brand = brand
        self.certType = certType
        self.domainCount = domainCount
        self.certValidity = certValidity
        self.commonName = commonName
        self.state = state
        self.canceledReason = canceledReason
        self.recordValidate = recordValidate
        self.corpName = corpName
        self.corpAddr = corpAddr
        self.dnsNames = dnsNames
        self.email = email