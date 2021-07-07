import pytest
import json
from main import app

@pytest.fixture(scope='session')
def client():
    testing_client = app.test_client()
    with app.app_context():
        yield testing_client


@pytest.fixture(scope='session')
def input_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    yield data


@pytest.fixture(scope='session')
def output_data():
    with open('output.json', 'r') as f:
        data = json.load(f)
    yield data
