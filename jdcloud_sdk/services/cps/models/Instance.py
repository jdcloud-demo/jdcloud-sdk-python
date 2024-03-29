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


class Instance(object):

    def __init__(self, instanceId=None, region=None, az=None, deviceType=None, name=None, description=None, status=None, enableInternet=None, enableIpv6=None, bandwidth=None, imageType=None, osTypeId=None, osName=None, osType=None, osVersion=None, sysRaidTypeId=None, sysRaidType=None, dataRaidTypeId=None, dataRaidType=None, networkType=None, vpcId=None, vpcName=None, subnetId=None, subnetName=None, privateIp=None, lineType=None, elasticIpId=None, publicIp=None, publicIpv6=None, charge=None):
        """
        :param instanceId: (Optional) 云物理服务器实例ID
        :param region: (Optional) 区域代码, 如 cn-east-1
        :param az: (Optional) 可用区, 如 cn-east-1a
        :param deviceType: (Optional) 实例类型, 如 cps.c.normal
        :param name: (Optional) 云物理服务器名称
        :param description: (Optional) 云物理服务器描述
        :param status: (Optional) 云物理服务器生命周期状态
        :param enableInternet: (Optional) 是否启用外网, 如 yes/no
        :param enableIpv6: (Optional) 是否启用IPv6, 如 yes/no
        :param bandwidth: (Optional) 带宽, 单位Mbps
        :param imageType: (Optional) 镜像类型, 如 standard
        :param osTypeId: (Optional) 操作系统类型ID
        :param osName: (Optional) 操作系统名称
        :param osType: (Optional) 操作系统类型, 如 ubuntu/centos
        :param osVersion: (Optional) 操作系统版本, 如 16.04
        :param sysRaidTypeId: (Optional) 系统盘RAID类型ID
        :param sysRaidType: (Optional) 系统盘RAID类型, 如 NORAID, RAID0, RAID1
        :param dataRaidTypeId: (Optional) 数据盘RAID类型ID
        :param dataRaidType: (Optional) 数据盘RAID类型, 如 NORAID, RAID0, RAID1
        :param networkType: (Optional) 网络类型, 如 basic, vpc
        :param vpcId: (Optional) 私有网络ID
        :param vpcName: (Optional) 私有网络名称
        :param subnetId: (Optional) 子网编号
        :param subnetName: (Optional) 子网名称
        :param privateIp: (Optional) 内网IP
        :param lineType: (Optional) 外网链路类型, 如 bgp
        :param elasticIpId: (Optional) 弹性公网IPID
        :param publicIp: (Optional) 公网IP
        :param publicIpv6: (Optional) 公网IPv6
        :param charge: (Optional) 计费信息
        """

        self.instanceId = instanceId
        self.region = region
        self.az = az
        self.deviceType = deviceType
        self.name = name
        self.description = description
        self.status = status
        self.enableInternet = enableInternet
        self.enableIpv6 = enableIpv6
        self.bandwidth = bandwidth
        self.imageType = imageType
        self.osTypeId = osTypeId
        self.osName = osName
        self.osType = osType
        self.osVersion = osVersion
        self.sysRaidTypeId = sysRaidTypeId
        self.sysRaidType = sysRaidType
        self.dataRaidTypeId = dataRaidTypeId
        self.dataRaidType = dataRaidType
        self.networkType = networkType
        self.vpcId = vpcId
        self.vpcName = vpcName
        self.subnetId = subnetId
        self.subnetName = subnetName
        self.privateIp = privateIp
        self.lineType = lineType
        self.elasticIpId = elasticIpId
        self.publicIp = publicIp
        self.publicIpv6 = publicIpv6
        self.charge = charge
