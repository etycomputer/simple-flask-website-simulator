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

    def test_sleep(self, app: Flask):
        with app.test_client() as client:
            sleep_response = client.get('/sleep')
            self.assertEqual(200, sleep_response.status_code, '/sleep was not found')
            response_text = sleep_response.data.decode('UTF-8')
            self.assertTrue(search('Simulating website with %100 delay of 0.0 seconds', response_text) is not None)
            self.assertTrue(search('SUCCESSFUL', response_text) is not None)
            sleep_response = client.get('/sleep/1')
            self.assertEqual(200, sleep_response.status_code, '/sleep/1 was not found')
            response_text = sleep_response.data.decode('UTF-8')
            self.assertTrue(search('Simulating website with %100 delay of 1.0 seconds', response_text) is not None)
            self.assertTrue(search('SUCCESSFUL', response_text) is not None)
            sleep_response = client.get('/sleep/1/0')
            self.assertEqual(200, sleep_response.status_code, '/sleep/0/0 was not found')
            response_text = sleep_response.data.decode('UTF-8')
            self.assertTrue(search('SKIPPED', response_text) is not None)
            sleep_response = client.get('/sleep/1/500')
            self.assertEqual(400, sleep_response.status_code, '/sleep/0/500 was not found')
            response_text = sleep_response.data.decode('UTF-8')
            self.assertTrue(search('SUCCESSFUL', response_text) is not None)


if __name__ == '__main__':
    unittest.main()
