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


class DescribeElasticIpsRequest(JDCloudRequest):
    """
    查询弹性公网IP列表<br/>
支持分页查询，默认每页20条<br/>

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeElasticIpsRequest, self).__init__(
            '/regions/{regionId}/elasticIps', 'GET', header, version)
        self.parameters = parameters


class DescribeElasticIpsParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID，可调用接口（describeRegiones）获取云物理服务器支持的地域
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.status = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认为20；取值范围[20, 100]
        """
        self.pageSize = pageSize

    def setStatus(self, status):
        """
        :param status: (Optional) 弹性公网IP状态，取值范围：associate、disassociate
        """
        self.status = status

    def setFilters(self, filters):
        """
        :param filters: (Optional) elasticIpId - 弹性公网IPID，精确匹配，支持多个<br/>
elasticIp - 弹性公网IP，精确匹配，支持多个

        """
        self.filters = filters

