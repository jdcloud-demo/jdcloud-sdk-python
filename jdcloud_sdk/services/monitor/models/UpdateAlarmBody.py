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


class UpdateAlarmBody(object):

    def __init__(self, calculation, metric, operation, period, serviceCode, threshold, times, contactGroups=None, contactPersons=None, downSample=None, noticePeriod=None):
        """
        :param calculation:  统计方法：平均值=avg、最大值=max、最小值=min、总和=sum
        :param contactGroups: (Optional) 通知的联系组，如 [“联系组1”,”联系组2”]
        :param contactPersons: (Optional) 通知的联系人，如 [“联系人1”,”联系人2”]
        :param downSample: (Optional) 取样频次
        :param metric:  根据产品线查询可用监控项列表 接口 返回的Metric字段
        :param noticePeriod: (Optional) 通知周期 单位：小时
        :param operation:  >=、>、<、<=、==、!=
        :param period:  统计周期（单位：分钟），可选值：2,5,15,30,60
        :param serviceCode:  产品名称
        :param threshold:  阈值
        :param times:  连续多少次后报警，可选值:1,2,3,5
        """

        self.calculation = calculation
        self.contactGroups = contactGroups
        self.contactPersons = contactPersons
        self.downSample = downSample
        self.metric = metric
        self.noticePeriod = noticePeriod
        self.operation = operation
        self.period = period
        self.serviceCode = serviceCode
        self.threshold = threshold
        self.times = times
