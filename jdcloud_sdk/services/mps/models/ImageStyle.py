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


class ImageStyle(object):

    def __init__(self, id=None, userId=None, styleName=None, params=None, paramAlias=None, regionId=None, bucketName=None, status=None, modifyTime=None, createdTime=None):
        """
        :param id: (Optional) 图片样式id(readOnly)
        :param userId: (Optional) 用户id(readOnly)
        :param styleName: (Optional) 图片样式名称
        :param params: (Optional) 图片样式参数
        :param paramAlias: (Optional) 图片样式参数别名
        :param regionId: (Optional) 所属区域(readOnly)
        :param bucketName: (Optional) 所属Bucket(readOnly)
        :param status: (Optional) 图片样式状态(readOnly)
        :param modifyTime: (Optional) 修改时间(readOnly)
        :param createdTime: (Optional) 创建时间(readOnly)
        """

        self.id = id
        self.userId = userId
        self.styleName = styleName
        self.params = params
        self.paramAlias = paramAlias
        self.regionId = regionId
        self.bucketName = bucketName
        self.status = status
        self.modifyTime = modifyTime
        self.createdTime = createdTime