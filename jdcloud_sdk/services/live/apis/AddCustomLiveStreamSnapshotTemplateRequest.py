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


class AddCustomLiveStreamSnapshotTemplateRequest(JDCloudRequest):
    """
    添加直播截图模板
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddCustomLiveStreamSnapshotTemplateRequest, self).__init__(
            '/snapshotCustoms:template', 'POST', header, version)
        self.parameters = parameters


class AddCustomLiveStreamSnapshotTemplateParameters(object):

    def __init__(self, format, width, height, fillType, snapshotInterval, saveMode, saveBucket, saveEndpoint, template):
        """
        :param format: 图片格式
        :param width: 图片宽度
        :param height: 范围
        :param fillType: 截图与设定的宽高不匹配时的处理规则
        :param snapshotInterval: 截图周期
        :param saveMode: 存储模式
        :param saveBucket: 保存bucket
        :param saveEndpoint: 保存endPoint
        :param template: 录制模板自定义名称
        """

        self.format = format
        self.width = width
        self.height = height
        self.fillType = fillType
        self.snapshotInterval = snapshotInterval
        self.saveMode = saveMode
        self.saveBucket = saveBucket
        self.saveEndpoint = saveEndpoint
        self.template = template

