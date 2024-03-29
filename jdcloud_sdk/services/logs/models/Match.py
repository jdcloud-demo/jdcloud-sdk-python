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


class Match(object):

    def __init__(self, eq=None, not=None, range=None, regexp=None, simple_query_string=None, simpleQuery=None, substring=None):
        """
        :param eq: (Optional) 
        :param not: (Optional) 
        :param range: (Optional) 
        :param regexp: (Optional) 
        :param simple_query_string: (Optional) 
        :param simpleQuery: (Optional) 
        :param substring: (Optional) 
        """

        self.eq = eq
        self.not = not
        self.range = range
        self.regexp = regexp
        self.simple_query_string = simple_query_string
        self.simpleQuery = simpleQuery
        self.substring = substring
