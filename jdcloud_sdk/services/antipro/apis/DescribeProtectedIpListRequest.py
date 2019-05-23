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


class DescribeProtectedIpListRequest(JDCloudRequest):
    """
    查询已防护 IP 列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeProtectedIpListRequest, self).__init__(
            '/describeProtectedIpList', 'GET', header, version)
        self.parameters = parameters


class DescribeProtectedIpListParameters(object):

    def __init__(self, type, ):
        """
        :param type: 被防护 IP类型: 0: 全部, 1: 弹性公网 IP, 2: 云物理服务器公网 IP
        """

        self.pageNumber = None
        self.pageSize = None
        self.instanceId = None
        self.type = type
        self.ip = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小
        """
        self.pageSize = pageSize

    def setInstanceId(self, instanceId):
        """
        :param instanceId: (Optional) 实例 Id, 缺省时查询用户所有已防护 IP
        """
        self.instanceId = instanceId

    def setIp(self, ip):
        """
        :param ip: (Optional) 被防护 IP, 支持模糊查询
        """
        self.ip = ip

