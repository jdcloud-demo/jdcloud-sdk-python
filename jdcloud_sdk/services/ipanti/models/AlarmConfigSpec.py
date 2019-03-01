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


class AlarmConfigSpec(object):

    def __init__(self, blackHoleAlarmEmailStatus=None, blackHoleAlarmSmsStatus=None, blackHoleAlarmStatus=None, ddosAlarmEmailStatus=None, ddosAlarmSmsStatus=None, ddosAlarmStatus=None, errorCodeAlarmStatus=None, errorCodeDomain=None):
        """
        :param blackHoleAlarmEmailStatus: (Optional) 黑洞告警邮件开关 0 关闭 1 开启
        :param blackHoleAlarmSmsStatus: (Optional) 黑洞告警短信开关 0 关闭 1 开启
        :param blackHoleAlarmStatus: (Optional) 黑洞告警总开关  0 关闭 1 开启
        :param ddosAlarmEmailStatus: (Optional) DDos 攻击告警邮件开关  0 关闭 1 开启
        :param ddosAlarmSmsStatus: (Optional) DDos 攻击告警短信开关  0 关闭 1 开启
        :param ddosAlarmStatus: (Optional) DDos 告警总开关 0 关闭 1 开启
        :param errorCodeAlarmStatus: (Optional) 错误码告警总开关
        :param errorCodeDomain: (Optional) 错误码告警域名列表
        """

        self.blackHoleAlarmEmailStatus = blackHoleAlarmEmailStatus
        self.blackHoleAlarmSmsStatus = blackHoleAlarmSmsStatus
        self.blackHoleAlarmStatus = blackHoleAlarmStatus
        self.ddosAlarmEmailStatus = ddosAlarmEmailStatus
        self.ddosAlarmSmsStatus = ddosAlarmSmsStatus
        self.ddosAlarmStatus = ddosAlarmStatus
        self.errorCodeAlarmStatus = errorCodeAlarmStatus
        self.errorCodeDomain = errorCodeDomain
