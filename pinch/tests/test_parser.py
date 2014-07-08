"""Tests for todo.txt parser"""

# Copyright 2014 Jonathan M. Lange
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

import testtools

from .. import (
    _parser,
    _todo,
)


class TestParser(testtools.TestCase):

    def test_empty(self):
        self.assertEqual(None, _parser.parse_line(''))

    def test_something(self):
        item = _parser.parse_line('a todo item')
        self.assertEqual(_todo.TodoItem(content='a todo item'), item)
