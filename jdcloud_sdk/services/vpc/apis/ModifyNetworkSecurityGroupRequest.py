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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ModifyNetworkSecurityGroupRequest(JDCloudRequest):
    """
    修改安全组属性
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyNetworkSecurityGroupRequest, self).__init__(
            '/regions/{regionId}/networkSecurityGroups/{networkSecurityGroupId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifyNetworkSecurityGroupParameters(object):

    def __init__(self, regionId, networkSecurityGroupId, ):
        """
        :param regionId: Region ID
        :param networkSecurityGroupId: NetworkSecurityGroup ID
        """

        self.regionId = regionId
        self.networkSecurityGroupId = networkSecurityGroupId
        self.networkSecurityGroupName = None
        self.description = None

    def setNetworkSecurityGroupName(self, networkSecurityGroupName):
        """
        :param networkSecurityGroupName: (Optional) 安全组的名字。名称取值范围：1-32个中文、英文大小写的字母、数字和下划线分隔符
        """
        self.networkSecurityGroupName = networkSecurityGroupName

    def setDescription(self, description):
        """
        :param description: (Optional) 安全组的描述，取值范围：0-256个UTF-8编码下的全部字符
        """
        self.description = description

