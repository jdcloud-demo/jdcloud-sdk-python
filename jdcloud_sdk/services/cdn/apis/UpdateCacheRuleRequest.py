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


class UpdateCacheRuleRequest(JDCloudRequest):
    """
    修改缓存规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateCacheRuleRequest, self).__init__(
            '/domain/{domain}/cacheRule', 'PUT', header, version)
        self.parameters = parameters


class UpdateCacheRuleParameters(object):

    def __init__(self, domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.weight = None
        self.ttl = None
        self.contents = None
        self.cacheType = None
        self.configId = None

    def setWeight(self, weight):
        """
        :param weight: (Optional) 此条配置的权重值, 取值范围为1-10,1最大
        """
        self.weight = weight

    def setTtl(self, ttl):
        """
        :param ttl: (Optional) 缓存时间,单位秒
        """
        self.ttl = ttl

    def setContents(self, contents):
        """
        :param contents: (Optional) 规则内容。其他类型只能以/或者.开头，如/a/b或.jpg
        """
        self.contents = contents

    def setCacheType(self, cacheType):
        """
        :param cacheType: (Optional) 缓存方式：0、不缓存，1自定义
        """
        self.cacheType = cacheType

    def setConfigId(self, configId):
        """
        :param configId: (Optional) 配置id
        """
        self.configId = configId

