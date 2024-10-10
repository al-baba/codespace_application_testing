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


def test_hello_endpoint(client):
    response_1 = client.get('/')
    response_2 = client.get('/hello/')
    xml_response = client.get('/hello/?content-type=text%2Fxml')
    json_response = client.get('/hello/?content-type=application%2Fjson')
    # 'http://127.0.0.1:5000/hello/?content-type=application%2Fjson'
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert xml_response.status_code == 200
    assert json_response.status_code == 200


def test_name_endpoint(client):
    response_1 = client.get('/name/Alexander')
    response_2 = client.get('/name/Ali?content-type=text%2xml')
    xml_response = client.get('/name/Alex?content-type=text%2Fxml')
    json_response = client.get('/name/Alejandro?content-type=application%2Fjson')
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert xml_response.status_code == 200
    assert json_response.status_code == 200

