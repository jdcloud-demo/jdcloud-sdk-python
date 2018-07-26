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


class GetSecurityTokenInfo(object):

    def __init__(self, type, code, action, durationSeconds=None):
        """
        :param type:  操作保护验证方式：1-短信,2-邮箱,3-MFA
        :param code:  验证码
        :param action:  操作action serviceName:actionName
        :param durationSeconds: (Optional) 令牌有效期，单位秒，OpenAPI第三方MFA方式验证有效，默认短信、邮箱token有效期300秒，MFA有效期30秒
        """

        self.type = type
        self.code = code
        self.action = action
        self.durationSeconds = durationSeconds