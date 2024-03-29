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


class ExportLiveSnapshotDataRequest(JDCloudRequest):
    """
    导出直播截图张数数据
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ExportLiveSnapshotDataRequest, self).__init__(
            '/exportLiveSnapshotData', 'GET', header, version)
        self.parameters = parameters


class ExportLiveSnapshotDataParameters(object):

    def __init__(self, startTime, ):
        """
        :param startTime: 起始时间:
- UTC时间
  格式: yyyy-MM-dd'T'HH:mm:ss'Z'
  示例: 2018-10-21T10:00:00Z
- 支持最大查询90天以内的数据

        """

        self.publishDomain = None
        self.appName = None
        self.streamName = None
        self.startTime = startTime
        self.endTime = None

    def setPublishDomain(self, publishDomain):
        """
        :param publishDomain: (Optional) 推流域名
        """
        self.publishDomain = publishDomain

    def setAppName(self, appName):
        """
        :param appName: (Optional) 应用名称
        """
        self.appName = appName

    def setStreamName(self, streamName):
        """
        :param streamName: (Optional) 流名称
        """
        self.streamName = streamName

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间:
- UTC时间
  格式: yyyy-MM-dd'T'HH:mm:ss'Z'
  示例: 2018-10-21T10:00:00Z
- 为空,默认当前时间

        """
        self.endTime = endTime

