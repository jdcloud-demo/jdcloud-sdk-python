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


class CreateElasticIpsRequest(JDCloudRequest):
    """
    创建一个或者多个弹性Ip
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateElasticIpsRequest, self).__init__(
            '/regions/{regionId}/elasticIps/', 'POST', header, version)
        self.parameters = parameters


class CreateElasticIpsParameters(object):

    def __init__(self, regionId, maxCount, elasticIpSpec):
        """
        :param regionId: Region ID
        :param maxCount: 购买弹性ip数量；取值范围：[1,100]
        :param elasticIpSpec: 弹性ip规格
        """

        self.regionId = regionId
        self.maxCount = maxCount
        self.elasticIpAddress = None
        self.elasticIpSpec = elasticIpSpec

    def setElasticIpAddress(self, elasticIpAddress):
        """
        :param elasticIpAddress: (Optional) 指定弹性ip地址进行创建，当申请创建多个弹性ip时，必须为空
        """
        self.elasticIpAddress = elasticIpAddress

