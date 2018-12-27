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


class DevicesEnrollRequest(JDCloudRequest):
    """
    客户用该接口可以批量登记设备

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DevicesEnrollRequest, self).__init__(
            '/device', 'POST', header, version)
        self.parameters = parameters


class DevicesEnrollParameters(object):

    def __init__(self, ):
        """
        """

        self.instanceId = None
        self.device = None

    def setInstanceId(self, instanceId):
        """
        :param instanceId: (Optional) 
        """
        self.instanceId = instanceId

    def setDevice(self, device):
        """
        :param device: (Optional) 
        """
        self.device = device

