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


class OrderSpec(object):

    def __init__(self, buyType, pkgType, ipNum, bp, ep, returnUrl, id=None, name=None, timeSpan=None, timeUnit=None):
        """
        :param buyType:  操作类型 1: 新购防护包, 3: 升级防护包
        :param id: (Optional) 防护包实例 Id, 升级防护包实例时必传
        :param name: (Optional) 防护包实例名称, 新购防护包时必传
长度限制为 1-80 个字符, 只允许包含中文, 字母, 数字, -, ., /, _

        :param pkgType:  套餐类型, 1: 独享 IP, 2: 共享 IP
        :param ipNum:  可防护 IP 数量, 5, 10, 50, 100 1000(不限)
        :param bp:  保底带宽: 10, 20, 30, 50, 单位: Gbps
        :param ep:  弹性带宽: 0, 10, 20, 单位: Gbps
        :param timeSpan: (Optional) 购买防护包时长, 新购防护包时必传
- timeUnit 为 3 时, 可取值 1-9
- timeUnit 为 4 时, 可取值 1-3

        :param timeUnit: (Optional) 购买时长类型, 新购防护包时必传
- 3: 月
- 4: 年

        :param returnUrl:  回调 url
        """

        self.buyType = buyType
        self.id = id
        self.name = name
        self.pkgType = pkgType
        self.ipNum = ipNum
        self.bp = bp
        self.ep = ep
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.returnUrl = returnUrl