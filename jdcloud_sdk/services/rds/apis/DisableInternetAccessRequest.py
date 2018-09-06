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


class DisableInternetAccessRequest(JDCloudRequest):
    """
    关闭RDS实例的外网访问功能。关闭后，用户无法通过Internet访问RDS，但可以在京东云内网通过内网域名访问
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DisableInternetAccessRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:disableInternetAccess', 'POST', header, version)
        self.parameters = parameters


class DisableInternetAccessParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        """

        self.regionId = regionId
        self.instanceId = instanceId
