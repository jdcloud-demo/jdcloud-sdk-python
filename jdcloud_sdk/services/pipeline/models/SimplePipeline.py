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


class SimplePipeline(object):

    def __init__(self, uuid=None, name=None, startedAt=None, latestStatus=None, latestInstanceUuid=None):
        """
        :param uuid: (Optional) 流水线的uuid
        :param name: (Optional) 流水线名称
        :param startedAt: (Optional) 开始执行流水线的时间
        :param latestStatus: (Optional) 最近一次执行的状态(数据结构待商定)
        :param latestInstanceUuid: (Optional) 最新一次执行的实例ID
        """

        self.uuid = uuid
        self.name = name
        self.startedAt = startedAt
        self.latestStatus = latestStatus
        self.latestInstanceUuid = latestInstanceUuid