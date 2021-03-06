#!/usr/bin/env python
# coding: UTF-8

# Copyright 2012 Keita Kita
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

# Define test suite for unit test.

import os.path
import unittest

def suite():
    u"""
    Define unit test.
    """
    test_loader = unittest.TestLoader()
    return test_loader.discover(os.path.dirname(__file__))

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())

