# -*- coding: utf-8 -*-

from .context import rvid

import unittest


class ReplaceSimpleValueWithNoneTestSuite(unittest.TestCase):
    """Replace a target value with an expected value."""

    def test_1_empty_string_with_none(self):
        self.assertEqual(rvid.replace({'key1': ''}), {'key1': None})

    def test_2_empty_string_with_none(self):
        self.assertEqual(rvid.replace({'key1': '', 'key2': ''}), {'key1': None, 'key2': None})

    def test_target_is_0_and_replace_it_with_none(self):
        self.assertEqual(rvid.replace({'key1': 0, 'key2': ''}, target=0), {'key1': None, 'key2': ''})

    def test_target_is_0_and_replace_it_with_1(self):
        self.assertEqual(rvid.replace({'key1': 0, 'key2': ''}, target=0, by=1), {'key1': 1, 'key2': ''})

    def test_target_is_0_and_replace_it_with_false(self):
        self.assertEqual(rvid.replace({'key1': 0, 'key2': ''}, target=0, by=False), {'key1': False, 'key2': ''})

    def test_result_is_deep_copied(self):
        source = {'key1': ''}
        result = rvid.replace(source)
        self.assertNotEqual(id(source), id(result))


class ReplaceDictWithNoneTestSuite(unittest.TestCase):
    """Replace a target value in dict with an expected value."""

    def test_1_empty_string_in_dict_with_none(self):
        self.assertEqual(rvid.replace({'key01': {'key11': ''}}), {'key01': {'key11': None}})

    def test_result_is_deep_copied(self):
        source = {'key01': {'key11': ''}}
        result = rvid.replace(source)
        self.assertNotEqual(id(source), id(result))
        self.assertNotEqual(id(source['key01']), id(result['key01']))

    def test_2_empty_string_in_dict_with_none(self):
        self.assertEqual(rvid.replace({'key01': {'key11': ''}, 'key02': {'key12': ''}}), {'key01': {'key11': None}, 'key02': {'key12': None}})

    def test_more_nested_dict(self):
        source = {
            'key001': {
                'key011': '',
                'key012': 0,
                'key013': 'Hello',
                'key014': {
                    'key021': '',
                    'key022': False,
                    'key023': {
                        'key031': {
                            'key041': ''
                        }
                    },
                },
            }
        }
        expected = {
            'key001': {
                'key011': None,
                'key012': 0,
                'key013': 'Hello',
                'key014': {
                    'key021': None,
                    'key022': False,
                    'key023': {
                        'key031': {
                            'key041': None
                        }
                    },
                },
            }
        }
        result = rvid.replace(source)
        self.assertEqual(result, expected)

    def test_more_nested_dict_replaced_0_with_1(self):
        source = {
            'key001': {
                'key011': '',
                'key012': 0,
                'key013': 'Hello',
                'key014': {
                    'key021': '',
                    'key022': False,
                    'key023': {
                        'key031': {
                            'key041': 0
                        }
                    },
                },
            }
        }
        expected = {
            'key001': {
                'key011': '',
                'key012': 1,
                'key013': 'Hello',
                'key014': {
                    'key021': '',
                    'key022': 1,
                    'key023': {
                        'key031': {
                            'key041': 1
                        }
                    },
                },
            }
        }
        result = rvid.replace(source, target=0, by=1)
        self.assertEqual(result, expected)


class ReplaceListWithNoneTestSuite(unittest.TestCase):
    """Replace a target value in dict with an expected value."""

    def test_1_empty_string_in_list_with_none(self):
        self.assertEqual(rvid.replace({'key01': ['', 0, False, '']}), {'key01': [None, 0, False, None]})

    def test_more_nested_list_in_dict(self):
        source = {
            'key001': {
                'key011': '',
                'key012': 0,
                'key013': 'Hello',
                'key014': {
                    'key021': '',
                    'key022': False,
                    'key023': {
                        'key031': {
                            'key041': 0
                        }
                    },
                },
            },
            'key002': [
                '',
                0,
                [
                    '',
                    'World',
                    {
                        'key100': '',
                        'key101': [
                            '',
                            1,
                            {
                                'key200': ''
                            },
                        ]
                    },
                ],
            ],
        }
        expected = {
            'key001': {
                'key011': None,
                'key012': 0,
                'key013': 'Hello',
                'key014': {
                    'key021': None,
                    'key022': False,
                    'key023': {
                        'key031': {
                            'key041': 0
                        }
                    },
                },
            },
            'key002': [
                None,
                0,
                [
                    None,
                    'World',
                    {
                        'key100': None,
                        'key101': [
                            None,
                            1,
                            {
                                'key200': None
                            },
                        ]
                    },
                ],
            ],
        }
        result = rvid.replace(source)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
