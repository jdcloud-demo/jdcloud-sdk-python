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


class DescribeInstancesRequest(JDCloudRequest):
    """
    批量查询云物理服务器详细信息<br/>
支持分页查询，默认每页20条<br/>

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeInstancesRequest, self).__init__(
            '/regions/{regionId}/instances', 'GET', header, version)
        self.parameters = parameters


class DescribeInstancesParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID，可调用接口（describeRegiones）获取云物理服务器支持的地域
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.az = None
        self.name = None
        self.networkType = None
        self.deviceType = None
        self.subnetId = None
        self.enableInternet = None
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

    def setAz(self, az):
        """
        :param az: (Optional) 可用区，精确匹配
        """
        self.az = az

    def setName(self, name):
        """
        :param name: (Optional) 云物理服务器名称，支持模糊匹配
        """
        self.name = name

    def setNetworkType(self, networkType):
        """
        :param networkType: (Optional) 网络类型，精确匹配，支持basic，vpc
        """
        self.networkType = networkType

    def setDeviceType(self, deviceType):
        """
        :param deviceType: (Optional) 实例类型，精确匹配，调用接口（describeDeviceTypes）获取实例类型
        """
        self.deviceType = deviceType

    def setSubnetId(self, subnetId):
        """
        :param subnetId: (Optional) 子网ID
        """
        self.subnetId = subnetId

    def setEnableInternet(self, enableInternet):
        """
        :param enableInternet: (Optional) 是否启用外网, yes/no
        """
        self.enableInternet = enableInternet

    def setFilters(self, filters):
        """
        :param filters: (Optional) instanceId - 云物理服务器ID，精确匹配，支持多个<br/>
privateIp - 云物理服务器内网IP，精确匹配，支持多个<br/>
status - 云物理服务器状态，参考云物理服务器状态，精确匹配，支持多个

        """
        self.filters = filters

