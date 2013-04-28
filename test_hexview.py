#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for hexview
"""

import unittest
import doctest

import hexview

class HexviewTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

doctests = doctest.DocTestSuite(hexview)

if __name__  == "__main__":
    unittest.main()
