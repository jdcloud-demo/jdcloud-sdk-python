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


class ViewTree(object):

    def __init__(self, disabled=None, label=None, leaf=None, value=None, children=None):
        """
        :param disabled: (Optional) 此解析线路是否禁用
        :param label: (Optional) 解析线路的名称
        :param leaf: (Optional) 此数据是否是叶子节点
        :param value: (Optional) 解析线路ID
        :param children: (Optional) 
        """

        self.disabled = disabled
        self.label = label
        self.leaf = leaf
        self.value = value
        self.children = children
