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


class Monitor(object):

    def __init__(self, alarmLimit=None, canRecover=None, canSwitch=None, clusters=None, domainName=None, hostStatus=None, hostValue=None, id=None, ipBackup01=None, ipBackup01Status=None, ipBackup01Type=None, ipBackup02=None, ipBackup02Status=None, ipBackup02Type=None, manualBackup=None, manualBackupStatus=None, manualBackupType=None, monitorEnable=None, monitorFreq=None, monitorPort=None, monitorRule=None, monitorUri=None, notifyEmail=None, notifyEmailEnable=None, notifyMsgBarEnable=None, notifySms=None, notifySmsEnable=None, protocol=None, stopRecoverRule=None, subDomainName=None, switchRecoverRule=None, type=None, usedType=None):
        """
        :param alarmLimit: (Optional) 连续几次触发报警
        :param canRecover: (Optional) 现在是否可以恢复
        :param canSwitch: (Optional) 现在是否可以切换
        :param clusters: (Optional) 机房探测点的集合
        :param domainName: (Optional) 主域名
        :param hostStatus: (Optional) 主机状态，0正常，1异常
        :param hostValue: (Optional) 监控对象
        :param id: (Optional) 监控项ID
        :param ipBackup01: (Optional) 备用地址1
        :param ipBackup01Status: (Optional) 备用地址1的状态，0正常，1异常
        :param ipBackup01Type: (Optional) 备用地址1的类型，1为ip 2为域名
        :param ipBackup02: (Optional) 备用地址2
        :param ipBackup02Status: (Optional) 备用地址2的状态，0正常，1异常
        :param ipBackup02Type: (Optional) 备用地址1的类型，1为ip 2为域名
        :param manualBackup: (Optional) 手动切换的地址
        :param manualBackupStatus: (Optional) 手动切换的地址的状态，0正常，1异常
        :param manualBackupType: (Optional) 手动切换的地址的类型，1为ip 2为域名
        :param monitorEnable: (Optional) 监控状况 开启监控 2，暂停监控 4
        :param monitorFreq: (Optional) 监控频率，单位s
        :param monitorPort: (Optional) 监控端口
        :param monitorRule: (Optional) 不做任何修改0，强制暂停解析记录1，自动切换到备用地址2
        :param monitorUri: (Optional) 监控路径
        :param notifyEmail: (Optional) 邮箱地址
        :param notifyEmailEnable: (Optional) 不发送邮件0， 发送邮件1
        :param notifyMsgBarEnable: (Optional) 不发送通知栏 0， 发送通知栏 1
        :param notifySms: (Optional) 手机号码
        :param notifySmsEnable: (Optional) 不发送短信 0， 发送短信 1
        :param protocol: (Optional) https 0，https 1
        :param stopRecoverRule: (Optional) 0自动恢复 1手动恢复
        :param subDomainName: (Optional) 子域名
        :param switchRecoverRule: (Optional) 0自动恢复至主host 1手动恢复至主host
        :param type: (Optional) 1为A记录，2为CNAME
        :param usedType: (Optional) 使用记录，host_value 0，ip_backup_01 1，ip_backup_02 2，cname_backup 3
        """

        self.alarmLimit = alarmLimit
        self.canRecover = canRecover
        self.canSwitch = canSwitch
        self.clusters = clusters
        self.domainName = domainName
        self.hostStatus = hostStatus
        self.hostValue = hostValue
        self.id = id
        self.ipBackup01 = ipBackup01
        self.ipBackup01Status = ipBackup01Status
        self.ipBackup01Type = ipBackup01Type
        self.ipBackup02 = ipBackup02
        self.ipBackup02Status = ipBackup02Status
        self.ipBackup02Type = ipBackup02Type
        self.manualBackup = manualBackup
        self.manualBackupStatus = manualBackupStatus
        self.manualBackupType = manualBackupType
        self.monitorEnable = monitorEnable
        self.monitorFreq = monitorFreq
        self.monitorPort = monitorPort
        self.monitorRule = monitorRule
        self.monitorUri = monitorUri
        self.notifyEmail = notifyEmail
        self.notifyEmailEnable = notifyEmailEnable
        self.notifyMsgBarEnable = notifyMsgBarEnable
        self.notifySms = notifySms
        self.notifySmsEnable = notifySmsEnable
        self.protocol = protocol
        self.stopRecoverRule = stopRecoverRule
        self.subDomainName = subDomainName
        self.switchRecoverRule = switchRecoverRule
        self.type = type
        self.usedType = usedType
