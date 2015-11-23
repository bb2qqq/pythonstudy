# coding: utf-8
"""
This module is trying to integrate all leetcode Solutions as useful tools.
"""

from Y13_Roman_to_integer import Solution as RI_Converter
from Y242_Valid_Anagram import Solution as AnagramChecker
from Y258_Add_Digits import Solution as DigitsCombiner
from Y263_Ugly_Number import Solution as UglyNumberChecker
from Y6_Zig_Zag_Conversion import Solution as ZigZagConverter

readme = {
    'RI_Converter': "Convert Roman to int, vice versa.",
    'AnagramChecker': "Check if 2 strings are anagrams.",
    'DigitsCombiner': "Add all digits of a number, repeat it, until the sum is a 1 digit number",
    'UglyNumberChecker': "Check if a number's prime factors only include 2, 3, 5",
    'ZigZagConverter': "Convert a sentence/str into a ZigZag Style",
}
