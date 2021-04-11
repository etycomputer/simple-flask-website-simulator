import unittest

import flask_unittest


def normal_suite():
    from tests import app_test
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(app_test.TestSetup))
    return suite
