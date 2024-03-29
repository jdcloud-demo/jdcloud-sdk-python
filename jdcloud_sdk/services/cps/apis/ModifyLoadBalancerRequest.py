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


class ModifyLoadBalancerRequest(JDCloudRequest):
    """
    修改负载均衡实例
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyLoadBalancerRequest, self).__init__(
            '/regions/{regionId}/slbs/{loadBalancerId}:modifyLoadBalancerAttributes', 'POST', header, version)
        self.parameters = parameters


class ModifyLoadBalancerParameters(object):

    def __init__(self, regionId, loadBalancerId, ):
        """
        :param regionId: 地域ID，可调用接口（describeRegiones）获取云物理服务器支持的地域
        :param loadBalancerId: 负载均衡实例ID
        """

        self.regionId = regionId
        self.loadBalancerId = loadBalancerId
        self.name = None
        self.description = None

    def setName(self, name):
        """
        :param name: (Optional) 名称
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 描述
        """
        self.description = description

