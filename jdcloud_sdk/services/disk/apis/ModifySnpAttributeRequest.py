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


class ModifySnpAttributeRequest(JDCloudRequest):
    """
    修改快照的名字或描述信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifySnpAttributeRequest, self).__init__(
            '/regions/{regionId}/snapshots/{snapshotId}', 'PATCH', header, version)
        self.parameters = parameters


class ModifySnpAttributeParameters(object):

    def __init__(self, regionId, snapshotId, ):
        """
        :param regionId: 地域ID
        :param snapshotId: 快照ID
        """

        self.regionId = regionId
        self.snapshotId = snapshotId
        self.name = None
        self.description = None

    def setName(self, name):
        """
        :param name: (Optional) 快照名称
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 快照描述，name和description必须要指定一个
        """
        self.description = description

