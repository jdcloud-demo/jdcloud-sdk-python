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


class DBInstance(object):

    def __init__(self, instanceId=None, instanceName=None, instanceType=None, engine=None, engineVersion=None, regionId=None, azId=None, instanceStatus=None, createTime=None, charge=None, tags=None):
        """
        :param instanceId: (Optional) 实例ID
        :param instanceName: (Optional) 实例名称，具体规则可参见帮助中心文档:[名称及密码限制](../../../documentation/Cloud-Database-and-Cache/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        :param instanceType: (Optional) 实例类别，例如主实例，只读实例等，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param engine: (Optional) 实例引擎类型，如MySQL或SQL Server等，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param engineVersion: (Optional) 实例引擎版本，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param regionId: (Optional) 地域ID，参见[地域及可用区对照表](../Enum-Definitions/Regions-AZ.md)
        :param azId: (Optional) 可用区ID，第一个为主实例在的可用区，参见[地域及可用区对照表](../Enum-Definitions/Regions-AZ.md)
        :param instanceStatus: (Optional) 实例状态，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param createTime: (Optional) 实例创建时间
        :param charge: (Optional) 计费配置
        :param tags: (Optional) 标签信息
        """

        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceType = instanceType
        self.engine = engine
        self.engineVersion = engineVersion
        self.regionId = regionId
        self.azId = azId
        self.instanceStatus = instanceStatus
        self.createTime = createTime
        self.charge = charge
        self.tags = tags
