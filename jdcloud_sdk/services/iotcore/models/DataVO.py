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


class DataVO(object):

    def __init__(self, id=None, name=None, subNetId=None, subNetName=None, vpcId=None, vpcName=None, azName=None, pubDomain=None, priDomain=None, status=None, createTime=None, instanceId=None, instanceType=None):
        """
        :param id: (Optional) 系统流水号
        :param name: (Optional) 实例名称
        :param subNetId: (Optional) 子网编号
        :param subNetName: (Optional) 子网名称
        :param vpcId: (Optional) VPC编号
        :param vpcName: (Optional) VPC名称
        :param azName: (Optional) 可用区名称
        :param pubDomain: (Optional) 公网域名
        :param priDomain: (Optional) 内网域名
        :param status: (Optional) IoT Hub实例状态[10~100为创建中,0或1-运行中,2-欠费停服,3-待删除]
        :param createTime: (Optional) 创建时间
        :param instanceId: (Optional) 实例编号
        :param instanceType: (Optional) 实例类型[0-独享，1-共享]
        """

        self.id = id
        self.name = name
        self.subNetId = subNetId
        self.subNetName = subNetName
        self.vpcId = vpcId
        self.vpcName = vpcName
        self.azName = azName
        self.pubDomain = pubDomain
        self.priDomain = priDomain
        self.status = status
        self.createTime = createTime
        self.instanceId = instanceId
        self.instanceType = instanceType
