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


class AddTagsSpec(object):

    def __init__(self, appCode, groupCode, resourceIds, serviceCode, srcServiceCode, tagK, tagV, ):
        """
        :param appCode:  应用码。调用此API前需找云监控提供
        :param groupCode:  组id。须确保在一个APP范围内全局唯一
        :param resourceIds:  资源列表。总资源不能超过100个
        :param serviceCode:  资源的产品线
        :param srcServiceCode:  打标签操作所属产品线的serviceCode
        :param tagK:  标签名称。调用此API前需要与云监控确认可以使用的标签名称
        :param tagV:  标签值
        """

        self.appCode = appCode
        self.groupCode = groupCode
        self.resourceIds = resourceIds
        self.serviceCode = serviceCode
        self.srcServiceCode = srcServiceCode
        self.tagK = tagK
        self.tagV = tagV
