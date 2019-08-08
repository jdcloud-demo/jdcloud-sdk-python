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


class BatchCreateAlarmsSpec(object):

    def __init__(self, clientToken, resourceIds, rules, serviceCode, contacts=None, datacenter=None, enabled=None, ruleName=None, ruleType=None, saveTemplate=None, templateName=None, templateServiceCode=None, webHookContent=None, webHookProtocol=None, webHookSecret=None, webHookUrl=None):
        """
        :param clientToken:  幂等性校验参数，最长36位
        :param contacts: (Optional) 通知的联系人
        :param datacenter: (Optional) 地域
        :param enabled: (Optional) 是否启用, 1表示启用规则，0表示禁用规则，默认为1
        :param resourceIds:  报警规则对应实例列表，每次最多100个，例如"['resourceId1','resourceId2']"
        :param ruleName: (Optional) 规则名称，规则名称，最大长度42个字符，只允许中英文、数字、''-''和"_"
        :param ruleType: (Optional) 规则类型, 1表示资源监控，6表示站点监控，默认为1
        :param rules:  要批量创建的规则列表
        :param saveTemplate: (Optional) 是否保存为模板
        :param serviceCode:  产品线标识，规则对应的serviceCode
        :param templateName: (Optional) 模板名称，保存模板时，不能为空
        :param templateServiceCode: (Optional) 产品线标识，保存为模板时，模板对应的serviceCode
        :param webHookContent: (Optional) 回调content 注：仅webHookUrl和webHookContent均不为空时，才会创建webHook
        :param webHookProtocol: (Optional) webHook协议，目前支持http，https
        :param webHookSecret: (Optional) 回调secret，用户请求签名，防伪造
        :param webHookUrl: (Optional) 回调url，例如http://www.jdcloud.com
        """

        self.clientToken = clientToken
        self.contacts = contacts
        self.datacenter = datacenter
        self.enabled = enabled
        self.resourceIds = resourceIds
        self.ruleName = ruleName
        self.ruleType = ruleType
        self.rules = rules
        self.saveTemplate = saveTemplate
        self.serviceCode = serviceCode
        self.templateName = templateName
        self.templateServiceCode = templateServiceCode
        self.webHookContent = webHookContent
        self.webHookProtocol = webHookProtocol
        self.webHookSecret = webHookSecret
        self.webHookUrl = webHookUrl
