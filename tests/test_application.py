"""
To write a test using pytest for a Flask application, you typically need to follow a few steps:
    - Create a Test Configuration: Set up your Flask app in test mode, so it behaves correctly during testing.
    - Set Up a Test Client: Flask provides a built-in test client that simulates requests to the application without running an actual server.
    - Write Test Functions: Use the test_client() provided by Flask to simulate HTTP requests, and use pytest assertions to verify the responses.
"""

import pytest
import sys


from basic_rest_API.app import application  # import Flask app instance

print(sys.path)
@pytest.fixture
def client():
    application.config['TESTING'] = True    # enable test mode
    with application.test_client() as client:   # create test client
        yield client


def test_application(client):
    response = client.get('/')
    print(response)
    assert response.status_code == 200
    # assert response.data == b"Hello, World!"