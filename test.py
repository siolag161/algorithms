"""
some tests. not exclusive but just to make sure it works
"""


import unittest

from kmp import KMP

class TestKMP(unittest.TestCase):

    def TestCase(self):
        kmp = KMP()
        rs = kmp.search_MP("abcabcabcabc", "cabc")
        self.assertListEqual(rs, [2,5,8])

        rs = kmp.search_MP("ABC ABCDAB ABCDABCDABDE", "ABCDABD")
        self.assertListEqual(rs, [15])

        
