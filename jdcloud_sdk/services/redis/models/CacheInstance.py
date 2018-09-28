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


class CacheInstance(object):

    def __init__(self, cacheInstanceId=None, cacheInstanceName=None, cacheInstanceClass=None, cacheInstanceMemoryMB=None, cacheInstanceStatus=None, cacheInstanceDescription=None, createTime=None, azId=None, vpcId=None, subnetId=None, connectionDomain=None, port=None, charge=None, instanceVersion=None, auth=None):
        """
        :param cacheInstanceId: (Optional) 实例ID
        :param cacheInstanceName: (Optional) 实例名称
        :param cacheInstanceClass: (Optional) 实例规格代码，参见<a href="https://www.jdcloud.com/help/detail/411/isCatalog/1">实例规格代码</a>
        :param cacheInstanceMemoryMB: (Optional) 容量，单位MB
        :param cacheInstanceStatus: (Optional) 实例状态，running：运行，error：错误，creating：创建中，changing：变配中，deleting：删除中
        :param cacheInstanceDescription: (Optional) 实例描述
        :param createTime: (Optional) 创建时间
        :param azId: (Optional) az信息
        :param vpcId: (Optional) 所属VPC的ID
        :param subnetId: (Optional) 所属子网的ID
        :param connectionDomain: (Optional) 访问域名
        :param port: (Optional) 端口
        :param charge: (Optional) 计费信息
        :param instanceVersion: (Optional) 实例版本
        :param auth: (Optional) 是否免密
        """

        self.cacheInstanceId = cacheInstanceId
        self.cacheInstanceName = cacheInstanceName
        self.cacheInstanceClass = cacheInstanceClass
        self.cacheInstanceMemoryMB = cacheInstanceMemoryMB
        self.cacheInstanceStatus = cacheInstanceStatus
        self.cacheInstanceDescription = cacheInstanceDescription
        self.createTime = createTime
        self.azId = azId
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.connectionDomain = connectionDomain
        self.port = port
        self.charge = charge
        self.instanceVersion = instanceVersion
        self.auth = auth
