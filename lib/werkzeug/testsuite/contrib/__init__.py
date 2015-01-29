# -*- coding: utf-8 -*-
"""
    werkzeug.blog.contrib
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests the contrib modules.

    :copyright: (c) 2013 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import unittest
from werkzeug.testsuite import iter_suites


def suite():
    suite = unittest.TestSuite()
    for other_suite in iter_suites(__name__):
        suite.addTest(other_suite)
    return suite
