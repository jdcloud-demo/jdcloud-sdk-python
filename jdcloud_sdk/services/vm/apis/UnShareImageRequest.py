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


class UnShareImageRequest(JDCloudRequest):
    """
    取消共享镜像，只允许操作您的个人私有镜像。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UnShareImageRequest, self).__init__(
            '/regions/{regionId}/images/{imageId}:unshare', 'POST', header, version)
        self.parameters = parameters


class UnShareImageParameters(object):

    def __init__(self, regionId, imageId, ):
        """
        :param regionId: 地域ID
        :param imageId: 镜像ID
        """

        self.regionId = regionId
        self.imageId = imageId
        self.pins = None

    def setPins(self, pins):
        """
        :param pins: (Optional) 需要取消的帐户
        """
        self.pins = pins

