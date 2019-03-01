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


class CCProtectionRule(object):

    def __init__(self, id=None, webRuleId=None, instanceId=None, name=None, enable=None, uri=None, matchType=None, detectPeriod=None, singleIpLimit=None, blockType=None, blockTime=None):
        """
        :param id: (Optional) CC 防护规则 ID
        :param webRuleId: (Optional) CC 防护规则对应的网站规则 ID
        :param instanceId: (Optional) CC 防护规则对应的实例 ID
        :param name: (Optional) CC 防护规则名称, 30 字符以内
        :param enable: (Optional) CC 防护规则状态: 0: 关闭, 1: 开启
        :param uri: (Optional) uri, 以 / 开头, 200 字符以内
        :param matchType: (Optional) 匹配 uri 类型, 0: 精确匹配, 1: 前缀匹配
        :param detectPeriod: (Optional) 检测周期, 单位为秒, 取值范围[5, 10800]
        :param singleIpLimit: (Optional) ip 访问次数, 取值范围[2, 2000]
        :param blockType: (Optional) 阻断类型, 1: 封禁, 2: 人机交互
        :param blockTime: (Optional) 阻断持续时间, 单位为分钟, 取值范围[1, 1440]
        """

        self.id = id
        self.webRuleId = webRuleId
        self.instanceId = instanceId
        self.name = name
        self.enable = enable
        self.uri = uri
        self.matchType = matchType
        self.detectPeriod = detectPeriod
        self.singleIpLimit = singleIpLimit
        self.blockType = blockType
        self.blockTime = blockTime
