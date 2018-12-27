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


class Tasks(object):

    def __init__(self, taskId=None, name=None, categoryId=None, category=None, format=None, size=None, status=None):
        """
        :param taskId: (Optional) 任务ID
        :param name: (Optional) 视频名称
        :param categoryId: (Optional) 分类ID
        :param category: (Optional) 分类名称
        :param format: (Optional) 格式
        :param size: (Optional) 文件大小
        :param status: (Optional) 上传状态
        """

        self.taskId = taskId
        self.name = name
        self.categoryId = categoryId
        self.category = category
        self.format = format
        self.size = size
        self.status = status
