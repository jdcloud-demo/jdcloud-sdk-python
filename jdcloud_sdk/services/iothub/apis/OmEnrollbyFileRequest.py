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


class OmEnrollbyFileRequest(JDCloudRequest):
    """
    物模型通过文件上传注册接口

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(OmEnrollbyFileRequest, self).__init__(
            '/file/{fileName}/om', 'POST', header, version)
        self.parameters = parameters


class OmEnrollbyFileParameters(object):

    def __init__(self, fileName, instanceId):
        """
        :param fileName: 物模型文件名称
        :param instanceId: 待上传物模型的IoT Hub实例编号
        """

        self.fileName = fileName
        self.instanceId = instanceId

