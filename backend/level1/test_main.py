def test_data_is_output(client, input_data, output_data):
    response = client.post('/', json=input_data)
    data = response.get_json()
    assert data is not None
    assert data == output_data


def test_200_response(client, input_data):
    response = client.post('/', json=input_data)
    assert response.status_code == 200


def assert_missing_data(client, data):
    """
    A helper function that posts the given data to the payload to the '/'
    endpoint and asserts that data is missing.
    Args:
        client - the flask app testing client
        data - the data to be sent to the '/' endpoint
    """
    response = client.post('/', json=data)
    assert response.status_code == 400
    data = response.get_json()
    assert data is not None
    assert data['message'] == 'Missing data'


def test_missing_articles(client, input_data):
    data = {k: v for k, v in input_data.items() if k != 'articles'}
    assert_missing_data(client, data)


def test_missing_carts(client, input_data):
    data = {k: v for k, v in input_data.items() if k != 'carts'}
    assert_missing_data(client, data)


def test_missing_data(client):
    data = {}
    assert_missing_data(client, data)


def test_too_few_carts(client, input_data):
    data = {k: v for k, v in input_data.items() if k != 'carts'}
    data['carts'] = []
    assert_missing_data(client, data)
