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


class DescribeStackResourcesRequest(JDCloudRequest):
    """
    查询资源栈中资源列表
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeStackResourcesRequest, self).__init__(
            '/regions/{regionId}/stacks/{stackId}/resources', 'GET', header, version)
        self.parameters = parameters


class DescribeStackResourcesParameters(object):

    def __init__(self, regionId, stackId, ):
        """
        :param regionId: 地域 ID
        :param stackId: 资源栈 ID
        """

        self.regionId = regionId
        self.stackId = stackId
        self.pageNumber = None
        self.pageSize = None
        self.search = None
        self.product = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 当前所在页，默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页面大小，默认为20；取值范围[1, 100]
        """
        self.pageSize = pageSize

    def setSearch(self, search):
        """
        :param search: (Optional) 按照京东云产品线名称或者资源逻辑ID进行模糊搜索
        """
        self.search = search

    def setProduct(self, product):
        """
        :param product: (Optional) 只按照京东云产品线名称进行模糊搜索，比如VM，Disk等
        """
        self.product = product

