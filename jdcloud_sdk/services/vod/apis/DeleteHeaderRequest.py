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


class DeleteHeaderRequest(JDCloudRequest):
    """
    删除域名访问头参数
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteHeaderRequest, self).__init__(
            '/domains/{domainId}:deleteHeader', 'POST', header, version)
        self.parameters = parameters


class DeleteHeaderParameters(object):

    def __init__(self, domainId, ):
        """
        :param domainId: 域名ID
        """

        self.domainId = domainId
        self.headerName = None
        self.headerValue = None
        self.headerType = None

    def setHeaderName(self, headerName):
        """
        :param headerName: (Optional) 头参数名
        """
        self.headerName = headerName

    def setHeaderValue(self, headerValue):
        """
        :param headerValue: (Optional) 头参数值
        """
        self.headerValue = headerValue

    def setHeaderType(self, headerType):
        """
        :param headerType: (Optional) 头参数类型
        """
        self.headerType = headerType
