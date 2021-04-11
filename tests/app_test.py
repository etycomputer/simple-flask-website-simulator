import unittest

import pytest
import flask_unittest
from flask import Flask
from tests.app_factory import build_app
from re import search


class _TestBase(flask_unittest.AppTestCase):
    """
    Base AppTestCase with helper functions used across other testcases
    """

    def create_app(self) -> Flask:
        return build_app()


class TestSetup(_TestBase):
    """
    Make sure the testcases are set up correctly
    and all expected properties exist and are correct
    """

    def setUp(self, app: Flask):
        # Make sure app is passed in correctly and has correct type
        self.assertTrue(app is not None)
        self.assertTrue(isinstance(app, Flask))

    def tearDown(self, app: Flask):
        # Make sure app is passed in correctly and has correct type
        self.assertTrue(app is not None)
        self.assertTrue(isinstance(app, Flask))

    def test_ok(self, app: Flask):
        # Make sure app is passed in correctly and has correct type
        self.assertTrue(app is not None)
        self.assertTrue(isinstance(app, Flask))

    def test_hello(self, app: Flask):
        with app.test_client() as client:
            hello_response = client.get('/hello')
            self.assertEqual(200, hello_response.status_code,
                             'Test did not pass the Hello World 200 status code test.')
            self.assertEqual(b'Hello World!', hello_response.data,
                             'Test did not pass the Hello World body content test.')

    def test_main(self, app: Flask):
        with app.test_client() as client:
            main_response = client.get('/')
            self.assertEqual(200, main_response.status_code, 'Main path did not pass the 200 status code')
            self.assertTrue(search('Welcome to website simulator', main_response.data.decode('UTF-8')) is not None)

    def test_static_icon_file_exists(self, app: Flask):
        with app.test_client() as client:
            static_file_response = client.get('/icon/favicon.ico')
            self.assertEqual(200, static_file_response.status_code, '/icon/favicon.ico was not found')
            static_file_response = client.get('/icon/favicon-16x16.png')
            self.assertEqual(200, static_file_response.status_code, 'favicon-16x16.png was not found')
            static_file_response = client.get('/icon/favicon-32x32.png')
            self.assertEqual(200, static_file_response.status_code, 'favicon-32x32.png was not found')
            static_file_response = client.get('/icon/apple-touch-icon.png')
            self.assertEqual(200, static_file_response.status_code, 'apple-touch-icon.png was not found')
            static_file_response = client.get('/icon/android-chrome-192x192.png')
            self.assertEqual(200, static_file_response.status_code, 'android-chrome-192x192.png was not found')
            static_file_response = client.get('/icon/android-chrome-512x512.png')
            self.assertEqual(200, static_file_response.status_code, 'android-chrome-512x512.png was not found')

    def test_static_css_file_exists(self, app: Flask):
        with app.test_client() as client:
            static_file_response = client.get('/css/style.css')
            self.assertEqual(200, static_file_response.status_code, '/css/style.css was not found')


if __name__ == '__main__':
    unittest.main()
