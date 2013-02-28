##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
import unittest


class Test_sort(unittest.TestCase):
    """Test zope.sequencesort.sort()
    """
    def _callFUT(self, *args, **kw):
        from zope.sequencesort.ssort import sort
        return sort(*args, **kw)

    def test_wo_args(self):
        self.assertEqual(self._callFUT(WORDLIST), RES_WO_ARGS)

    def test_w_only_key(self):
        self.assertEqual(self._callFUT(WORDLIST, (("key",),), mapping=1),
                         RES_W_ONLY_KEY)

    def test_w_key_and_cmp(self):
        self.assertEqual(self._callFUT(WORDLIST, (("key", "cmp"),), mapping=1),
                         RES_W_KEY_AND_CMP)

    def test_w_key_and_cmp_desc(self):
        self.assertEqual(self._callFUT(WORDLIST, (("key", "cmp", "desc"),),
                                       mapping=1), RES_W_KEY_AND_CMP_DESC)

    def test_w_multi_key(self):
        self.assertEqual(self._callFUT(WORDLIST, (("weight",), ("key",)),
                                       mapping=1), RES_W_MULTI_KEY)

    def test_w_multi_key_nocase_desc(self):
        self.assertEqual(self._callFUT(WORDLIST, (("weight",),
                                       ("key", "nocase", "desc")), mapping=1),
                         RES_W_MULTI_KEY_NOCASE_DESC)

    def test_w_custom_comparator(self):
        def myCmp(s1, s2):
            return -cmp(s1, s2)

        md = {"myCmp" : myCmp}
        self.assertEqual(self._callFUT(WORDLIST,
                                (("weight",), ("key", "myCmp", "desc")),
                                md,
                                mapping=1
                                ), RES_W_CUSTOM_COMPARATOR)


WORDLIST = [
   {"key": "aaa", "word": "AAA", "weight": 1},
   {"key": "bbb", "word": "BBB", "weight": 0},
   {"key": "ccc", "word": "CCC", "weight": 0},
   {"key": "ddd", "word": "DDD", "weight": 0},
   {"key": "eee", "word": "EEE", "weight": 1},
   {"key": "fff", "word": "FFF", "weight": 0},
   {"key": "ggg", "word": "GGG", "weight": 0},
   {"key": "hhh", "word": "HHH", "weight": 0},
   {"key": "iii", "word": "III", "weight": 1},
   {"key": "jjj", "word": "JJJ", "weight": -1},
   {"key": "kkk", "word": "KKK", "weight": 0},
   {"key": "lll", "word": "LLL", "weight": 0},
   {"key": "mmm", "word": "MMM", "weight": 0},
   {"key": "nnn", "word": "NNN", "weight": 0},
   {"key": "ooo", "word": "OOO", "weight": 1},
   {"key": "ppp", "word": "PPP", "weight": 0},
   {"key": "qqq", "word": "QQQ", "weight": -1},
   {"key": "rrr", "word": "RRR", "weight": 0},
   {"key": "sss", "word": "SSS", "weight": 0},
   {"key": "ttt", "word": "TTT", "weight": 0},
   {"key": "uuu", "word": "UUU", "weight": 1},
   {"key": "vvv", "word": "VVV", "weight": 0},
   {"key": "www", "word": "WWW", "weight": 0},
   {"key": "xxx", "word": "XXX", "weight": 0},
   {"key": "yyy", "word": "YYY", "weight": -1},
   {"key": "zzz", "word": "ZZZ", "weight": 0}
]

RES_WO_ARGS = [
    {'weight': 1, 'word': 'AAA', 'key': 'aaa'},
    {'weight': 0, 'word': 'BBB', 'key': 'bbb'},
    {'weight': 0, 'word': 'CCC', 'key': 'ccc'},
    {'weight': 0, 'word': 'DDD', 'key': 'ddd'},
    {'weight': 1, 'word': 'EEE', 'key': 'eee'},
    {'weight': 0, 'word': 'FFF', 'key': 'fff'},
    {'weight': 0, 'word': 'GGG', 'key': 'ggg'},
    {'weight': 0, 'word': 'HHH', 'key': 'hhh'},
    {'weight': 1, 'word': 'III', 'key': 'iii'},
    {'weight': -1, 'word': 'JJJ', 'key': 'jjj'},
    {'weight': 0, 'word': 'KKK', 'key': 'kkk'},
    {'weight': 0, 'word': 'LLL', 'key': 'lll'},
    {'weight': 0, 'word': 'MMM', 'key': 'mmm'},
    {'weight': 0, 'word': 'NNN', 'key': 'nnn'},
    {'weight': 1, 'word': 'OOO', 'key': 'ooo'},
    {'weight': 0, 'word': 'PPP', 'key': 'ppp'},
    {'weight': -1, 'word': 'QQQ', 'key': 'qqq'},
    {'weight': 0, 'word': 'RRR', 'key': 'rrr'},
    {'weight': 0, 'word': 'SSS', 'key': 'sss'},
    {'weight': 0, 'word': 'TTT', 'key': 'ttt'},
    {'weight': 1, 'word': 'UUU', 'key': 'uuu'},
    {'weight': 0, 'word': 'VVV', 'key': 'vvv'},
    {'weight': 0, 'word': 'WWW', 'key': 'www'},
    {'weight': 0, 'word': 'XXX', 'key': 'xxx'},
    {'weight': -1, 'word': 'YYY', 'key': 'yyy'},
    {'weight': 0, 'word': 'ZZZ', 'key': 'zzz'},
]

RES_W_ONLY_KEY = [
    {'weight': 1, 'word': 'AAA', 'key': 'aaa'},
    {'weight': 0, 'word': 'BBB', 'key': 'bbb'},
    {'weight': 0, 'word': 'CCC', 'key': 'ccc'},
    {'weight': 0, 'word': 'DDD', 'key': 'ddd'},
    {'weight': 1, 'word': 'EEE', 'key': 'eee'},
    {'weight': 0, 'word': 'FFF', 'key': 'fff'},
    {'weight': 0, 'word': 'GGG', 'key': 'ggg'},
    {'weight': 0, 'word': 'HHH', 'key': 'hhh'},
    {'weight': 1, 'word': 'III', 'key': 'iii'},
    {'weight': -1, 'word': 'JJJ', 'key': 'jjj'},
    {'weight': 0, 'word': 'KKK', 'key': 'kkk'},
    {'weight': 0, 'word': 'LLL', 'key': 'lll'},
    {'weight': 0, 'word': 'MMM', 'key': 'mmm'},
    {'weight': 0, 'word': 'NNN', 'key': 'nnn'},
    {'weight': 1, 'word': 'OOO', 'key': 'ooo'},
    {'weight': 0, 'word': 'PPP', 'key': 'ppp'},
    {'weight': -1, 'word': 'QQQ', 'key': 'qqq'},
    {'weight': 0, 'word': 'RRR', 'key': 'rrr'},
    {'weight': 0, 'word': 'SSS', 'key': 'sss'},
    {'weight': 0, 'word': 'TTT', 'key': 'ttt'},
    {'weight': 1, 'word': 'UUU', 'key': 'uuu'},
    {'weight': 0, 'word': 'VVV', 'key': 'vvv'},
    {'weight': 0, 'word': 'WWW', 'key': 'www'},
    {'weight': 0, 'word': 'XXX', 'key': 'xxx'},
    {'weight': -1, 'word': 'YYY', 'key': 'yyy'},
    {'weight': 0, 'word': 'ZZZ', 'key': 'zzz'},
]

RES_W_KEY_AND_CMP = [
    {'weight': 1, 'word': 'AAA', 'key': 'aaa'},
    {'weight': 0, 'word': 'BBB', 'key': 'bbb'},
    {'weight': 0, 'word': 'CCC', 'key': 'ccc'},
    {'weight': 0, 'word': 'DDD', 'key': 'ddd'},
    {'weight': 1, 'word': 'EEE', 'key': 'eee'},
    {'weight': 0, 'word': 'FFF', 'key': 'fff'},
    {'weight': 0, 'word': 'GGG', 'key': 'ggg'},
    {'weight': 0, 'word': 'HHH', 'key': 'hhh'},
    {'weight': 1, 'word': 'III', 'key': 'iii'},
    {'weight': -1, 'word': 'JJJ', 'key': 'jjj'},
    {'weight': 0, 'word': 'KKK', 'key': 'kkk'},
    {'weight': 0, 'word': 'LLL', 'key': 'lll'},
    {'weight': 0, 'word': 'MMM', 'key': 'mmm'},
    {'weight': 0, 'word': 'NNN', 'key': 'nnn'},
    {'weight': 1, 'word': 'OOO', 'key': 'ooo'},
    {'weight': 0, 'word': 'PPP', 'key': 'ppp'},
    {'weight': -1, 'word': 'QQQ', 'key': 'qqq'},
    {'weight': 0, 'word': 'RRR', 'key': 'rrr'},
    {'weight': 0, 'word': 'SSS', 'key': 'sss'},
    {'weight': 0, 'word': 'TTT', 'key': 'ttt'},
    {'weight': 1, 'word': 'UUU', 'key': 'uuu'},
    {'weight': 0, 'word': 'VVV', 'key': 'vvv'},
    {'weight': 0, 'word': 'WWW', 'key': 'www'},
    {'weight': 0, 'word': 'XXX', 'key': 'xxx'},
    {'weight': -1, 'word': 'YYY', 'key': 'yyy'},
    {'weight': 0, 'word': 'ZZZ', 'key': 'zzz'},
]

RES_W_KEY_AND_CMP_DESC = [
    {'weight': 0, 'word': 'ZZZ', 'key': 'zzz'},
    {'weight': -1, 'word': 'YYY', 'key': 'yyy'},
    {'weight': 0, 'word': 'XXX', 'key': 'xxx'},
    {'weight': 0, 'word': 'WWW', 'key': 'www'},
    {'weight': 0, 'word': 'VVV', 'key': 'vvv'},
    {'weight': 1, 'word': 'UUU', 'key': 'uuu'},
    {'weight': 0, 'word': 'TTT', 'key': 'ttt'},
    {'weight': 0, 'word': 'SSS', 'key': 'sss'},
    {'weight': 0, 'word': 'RRR', 'key': 'rrr'},
    {'weight': -1, 'word': 'QQQ', 'key': 'qqq'},
    {'weight': 0, 'word': 'PPP', 'key': 'ppp'},
    {'weight': 1, 'word': 'OOO', 'key': 'ooo'},
    {'weight': 0, 'word': 'NNN', 'key': 'nnn'},
    {'weight': 0, 'word': 'MMM', 'key': 'mmm'},
    {'weight': 0, 'word': 'LLL', 'key': 'lll'},
    {'weight': 0, 'word': 'KKK', 'key': 'kkk'},
    {'weight': -1, 'word': 'JJJ', 'key': 'jjj'},
    {'weight': 1, 'word': 'III', 'key': 'iii'},
    {'weight': 0, 'word': 'HHH', 'key': 'hhh'},
    {'weight': 0, 'word': 'GGG', 'key': 'ggg'},
    {'weight': 0, 'word': 'FFF', 'key': 'fff'},
    {'weight': 1, 'word': 'EEE', 'key': 'eee'},
    {'weight': 0, 'word': 'DDD', 'key': 'ddd'},
    {'weight': 0, 'word': 'CCC', 'key': 'ccc'},
    {'weight': 0, 'word': 'BBB', 'key': 'bbb'},
    {'weight': 1, 'word': 'AAA', 'key': 'aaa'},
]

RES_W_MULTI_KEY = [
    {'weight': -1, 'word': 'JJJ', 'key': 'jjj'},
    {'weight': -1, 'word': 'QQQ', 'key': 'qqq'},
    {'weight': -1, 'word': 'YYY', 'key': 'yyy'},
    {'weight': 0, 'word': 'BBB', 'key': 'bbb'},
    {'weight': 0, 'word': 'CCC', 'key': 'ccc'},
    {'weight': 0, 'word': 'DDD', 'key': 'ddd'},
    {'weight': 0, 'word': 'FFF', 'key': 'fff'},
    {'weight': 0, 'word': 'GGG', 'key': 'ggg'},
    {'weight': 0, 'word': 'HHH', 'key': 'hhh'},
    {'weight': 0, 'word': 'KKK', 'key': 'kkk'},
    {'weight': 0, 'word': 'LLL', 'key': 'lll'},
    {'weight': 0, 'word': 'MMM', 'key': 'mmm'},
    {'weight': 0, 'word': 'NNN', 'key': 'nnn'},
    {'weight': 0, 'word': 'PPP', 'key': 'ppp'},
    {'weight': 0, 'word': 'RRR', 'key': 'rrr'},
    {'weight': 0, 'word': 'SSS', 'key': 'sss'},
    {'weight': 0, 'word': 'TTT', 'key': 'ttt'},
    {'weight': 0, 'word': 'VVV', 'key': 'vvv'},
    {'weight': 0, 'word': 'WWW', 'key': 'www'},
    {'weight': 0, 'word': 'XXX', 'key': 'xxx'},
    {'weight': 0, 'word': 'ZZZ', 'key': 'zzz'},
    {'weight': 1, 'word': 'AAA', 'key': 'aaa'},
    {'weight': 1, 'word': 'EEE', 'key': 'eee'},
    {'weight': 1, 'word': 'III', 'key': 'iii'},
    {'weight': 1, 'word': 'OOO', 'key': 'ooo'},
    {'weight': 1, 'word': 'UUU', 'key': 'uuu'},
]

RES_W_MULTI_KEY_NOCASE_DESC = [
    {'weight': -1, 'word': 'YYY', 'key': 'yyy'},
    {'weight': -1, 'word': 'QQQ', 'key': 'qqq'},
    {'weight': -1, 'word': 'JJJ', 'key': 'jjj'},
    {'weight': 0, 'word': 'ZZZ', 'key': 'zzz'},
    {'weight': 0, 'word': 'XXX', 'key': 'xxx'},
    {'weight': 0, 'word': 'WWW', 'key': 'www'},
    {'weight': 0, 'word': 'VVV', 'key': 'vvv'},
    {'weight': 0, 'word': 'TTT', 'key': 'ttt'},
    {'weight': 0, 'word': 'SSS', 'key': 'sss'},
    {'weight': 0, 'word': 'RRR', 'key': 'rrr'},
    {'weight': 0, 'word': 'PPP', 'key': 'ppp'},
    {'weight': 0, 'word': 'NNN', 'key': 'nnn'},
    {'weight': 0, 'word': 'MMM', 'key': 'mmm'},
    {'weight': 0, 'word': 'LLL', 'key': 'lll'},
    {'weight': 0, 'word': 'KKK', 'key': 'kkk'},
    {'weight': 0, 'word': 'HHH', 'key': 'hhh'},
    {'weight': 0, 'word': 'GGG', 'key': 'ggg'},
    {'weight': 0, 'word': 'FFF', 'key': 'fff'},
    {'weight': 0, 'word': 'DDD', 'key': 'ddd'},
    {'weight': 0, 'word': 'CCC', 'key': 'ccc'},
    {'weight': 0, 'word': 'BBB', 'key': 'bbb'},
    {'weight': 1, 'word': 'UUU', 'key': 'uuu'},
    {'weight': 1, 'word': 'OOO', 'key': 'ooo'},
    {'weight': 1, 'word': 'III', 'key': 'iii'},
    {'weight': 1, 'word': 'EEE', 'key': 'eee'},
    {'weight': 1, 'word': 'AAA', 'key': 'aaa'},
]

RES_W_CUSTOM_COMPARATOR = [
    {'weight': -1, 'word': 'JJJ', 'key': 'jjj'},
    {'weight': -1, 'word': 'QQQ', 'key': 'qqq'},
    {'weight': -1, 'word': 'YYY', 'key': 'yyy'},
    {'weight': 0, 'word': 'BBB', 'key': 'bbb'},
    {'weight': 0, 'word': 'CCC', 'key': 'ccc'},
    {'weight': 0, 'word': 'DDD', 'key': 'ddd'},
    {'weight': 0, 'word': 'FFF', 'key': 'fff'},
    {'weight': 0, 'word': 'GGG', 'key': 'ggg'},
    {'weight': 0, 'word': 'HHH', 'key': 'hhh'},
    {'weight': 0, 'word': 'KKK', 'key': 'kkk'},
    {'weight': 0, 'word': 'LLL', 'key': 'lll'},
    {'weight': 0, 'word': 'MMM', 'key': 'mmm'},
    {'weight': 0, 'word': 'NNN', 'key': 'nnn'},
    {'weight': 0, 'word': 'PPP', 'key': 'ppp'},
    {'weight': 0, 'word': 'RRR', 'key': 'rrr'},
    {'weight': 0, 'word': 'SSS', 'key': 'sss'},
    {'weight': 0, 'word': 'TTT', 'key': 'ttt'},
    {'weight': 0, 'word': 'VVV', 'key': 'vvv'},
    {'weight': 0, 'word': 'WWW', 'key': 'www'},
    {'weight': 0, 'word': 'XXX', 'key': 'xxx'},
    {'weight': 0, 'word': 'ZZZ', 'key': 'zzz'},
    {'weight': 1, 'word': 'AAA', 'key': 'aaa'},
    {'weight': 1, 'word': 'EEE', 'key': 'eee'},
    {'weight': 1, 'word': 'III', 'key': 'iii'},
    {'weight': 1, 'word': 'OOO', 'key': 'ooo'},
    {'weight': 1, 'word': 'UUU', 'key': 'uuu'},
]


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(Test_sort),
    ))
