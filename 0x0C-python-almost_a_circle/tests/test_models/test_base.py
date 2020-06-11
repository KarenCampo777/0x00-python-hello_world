#!/usr/bin/python3

"""Unittest"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base tests"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_00(self):
        """Test 0"""
        base0 = Base()
        base1 = Base()
        self.assertEqual(base0.id, 1)
        self.assertEqual(base1.id, 2)

    def test_01(self):
        """Test 1"""
        base0 = Base(0)
        self.assertEqual(base0.id, 0)

    def test_02(self):
        """Test 2"""
        base0 = Base(12)
        self.assertEqual(base0.id, 12)

    def test_03(self):
        """Test 3"""
        base0 = Base("test")
        self.assertEqual(base0.id, "test")

    def test_04(self):
        """Test 4"""
        base0 = Base(-12)
        self.assertEqual(base0.id, -12)

    def test_05(self):
        """Test 5"""
        base0 = Base(None)
        self.assertEqual(base0.id, 1)

    def test_06(self):
        """Test 6"""
        base0 = Base({"test": "test"})
        self.assertEqual(base0.id, {"test": "test"})

    def test_07(self):
        """Test 7"""
        base0 = Base([1, 2, 3])
        self.assertEqual(base0.id, [1, 2, 3])

    def test_08(self):
        """Test 8"""
        base0 = Base(12.3)
        self.assertEqual(base0.id, 12.3)

    def test_09(self):
        """Test 9"""
        base0 = Base()
        self.assertEqual(str(type(base0)), "<class 'models.base.Base'>")
        self.assertEqual(base0.__dict__, {"id": 1})

    def test_10(self):
        """Test 10"""
        ret = Base.to_json_string(None)
        self.assertEqual(ret, "[]")