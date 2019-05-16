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


class ManageQueryStreamInfo(object):

    def __init__(self, publishDomain=None, appName=None, streamName=None, publishStartTime=None, publishEndTime=None, publishUrl=None, status=None):
        """
        :param publishDomain: (Optional) 推流域名
        :param appName: (Optional) 应用名称
        :param streamName: (Optional) 流名称
        :param publishStartTime: (Optional) 推流开始时间
- UTC时间
  格式:yyyy-MM-dd'T'HH:mm:ss'Z'
  示例:2018-10-21T10:00:00Z

        :param publishEndTime: (Optional) 推流结束时间
- UTC时间
  格式:yyyy-MM-dd'T'HH:mm:ss'Z'
  示例:2018-10-21T10:00:00Z

        :param publishUrl: (Optional) 推流地址
        :param status: (Optional) 流状态：
- living-在线流
- stop-历史流
- forbid-禁用流

        """

        self.publishDomain = publishDomain
        self.appName = appName
        self.streamName = streamName
        self.publishStartTime = publishStartTime
        self.publishEndTime = publishEndTime
        self.publishUrl = publishUrl
        self.status = status
