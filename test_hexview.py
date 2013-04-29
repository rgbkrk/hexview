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

    def test_entry_points(self):
        hexview.viewers
        hexview.annotators

    def test_basic_building(self):
        hex_view = hexview.HexView("ABCDEFGH")
        dump = hex_view.dump()
        self.assertIn("00000000:",dump)
        self.assertIn("4142 4344 4546 4748",dump)
        self.assertIn("ABCDEFGH",dump)

    def test_width(self):
        hex_view = hexview.HexView("A"*56,width=12)
        dump = hex_view.dump()
        self.assertIn(": " + "4141 "*6 + " AAAAAAAAAAAA",dump)

        hex_view.width = 3
        dump = hex_view.dump()
        self.assertIn(": " + "4141 41" + " AAA",dump)

if __name__  == "__main__":
    doctest.testmod(hexview)
    unittest.main()

