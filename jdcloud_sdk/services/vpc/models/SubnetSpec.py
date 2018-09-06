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


class SubnetSpec(object):

    def __init__(self, vpcId, subnetName, addressPrefix, routeTableId=None, description=None):
        """
        :param vpcId:  子网所属vpc的Id
        :param subnetName:  子网名称,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        :param addressPrefix:  子网网段，vpc内子网网段不能重叠，cidr的取值范围：10.0.0.0/8、172.16.0.0/12和192.168.0.0/16及它们包含的子网，且子网掩码长度为16-28之间，如果vpc含有cidr，则必须为vpc所在cidr的子网
        :param routeTableId: (Optional) 子网关联的路由表Id, 默认为vpc的默认路由表
        :param description: (Optional) 子网描述信息,允许输入UTF-8编码下的全部字符，不超过256字符。
        """

        self.vpcId = vpcId
        self.subnetName = subnetName
        self.addressPrefix = addressPrefix
        self.routeTableId = routeTableId
        self.description = description