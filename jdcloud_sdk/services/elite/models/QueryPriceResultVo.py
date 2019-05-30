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


class QueryPriceResultVo(object):

    def __init__(self, totalPrice=None, totalPriceScale4=None, discountedTotalPrice=None, totalDiscount=None, totalOriginalPrice=None, remark=None):
        """
        :param totalPrice: (Optional) 总金额，小数后2位精度
        :param totalPriceScale4: (Optional) 总金额，小数后4位精度
        :param discountedTotalPrice: (Optional) 折扣后总金额
        :param totalDiscount: (Optional) 折扣优惠金额
        :param totalOriginalPrice: (Optional) 订单原价
        :param remark: (Optional) 备注
        """

        self.totalPrice = totalPrice
        self.totalPriceScale4 = totalPriceScale4
        self.discountedTotalPrice = discountedTotalPrice
        self.totalDiscount = totalDiscount
        self.totalOriginalPrice = totalOriginalPrice
        self.remark = remark