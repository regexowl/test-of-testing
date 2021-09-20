#!/usr/bin/env python

import unittest
from code import Greeting

class MyTest(unittest.TestCase):
    def test(self):
        greeting = Greeting()
        self.assertEqual(greeting.greet, "Hello world!")


if __name__ == '__main__':
    unittest.main()