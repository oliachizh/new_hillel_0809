import logging
import pytest
import requests
from pygments.lexers import data

host = '127.0.0.1'
port = 7070
BASE_URL = f'http://{host}:{port}'

def get_content():
    return requests.get(f'{BASE_URL}/content').json()


def get_content_ids() -> list[int]:
    all_content = get_content()
    len_content = len(all_content['content'])
    ids = list(range(len_content))
    return ids



def test_get_content_success():
    response = requests.get(f'{BASE_URL}/content')
    assert response.status_code == 200

def get_content_ids() -> list[int]:
    all_content = get_content()
    len_content = len(all_content['content'])
    ids = list(range(len_content))
    return ids

@pytest.mark.parametrize('content_id', get_content_ids())
def test_get_content_by_id(content_id):
    response = requests.get(f'{BASE_URL}/content/{content_id}')
    logging.info(response.json())
    assert response.status_code == 200


def test_get_content_empty():
    content = get_content()
    assert content == {'content': []}


@pytest.mark.parametrize('data', [
    'Ola',
    1,
    True,
    [{'1': 2}]
])
@pytest.mark.api_test
def test_post_content_success(data):
    response = requests.post(f'{BASE_URL}/content', json=data)
    assert response.status_code == 201
    assert response.json()['message'] == "Content created successfully!"
    assert get_content()['content'][-1] == data


def test_post_content_missing_body():
    response = requests.post(f'{BASE_URL}/content', json='')
    assert response.status_code == 400
    assert response.json()['error'] == "Request must contain JSON data."


def test_post_content_no_body():
    response = requests.post(f'{BASE_URL}/content')
    assert response.status_code == 400
    assert response.json()['error'] == "Request must contain JSON data."

def test_post_content():
    payload = 1
    requests.post(f'{BASE_URL}/content', json=payload)

@pytest.mark.parametrize('data', [
    'new content',
    123,
    ['new content'],
    True,
    ''
])
def test_update_content_success(data):
    response = requests.put(f'{BASE_URL}]/content/0', json=data)
    assert response.status_code == 200
    assert response.json()['message'] == "Content updated successfully!"
    assert get_content()['content'][0] == data
    assert len(get_content()['content']) == 1

def test_update_content_missing_body():
    pass
