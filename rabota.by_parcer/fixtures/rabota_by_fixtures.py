import os.path

import html5lib
import pytest
from clients.http_client import HttpClient
from requests import codes
import yaml
from bs4 import BeautifulSoup


@pytest.fixture()
def http_client():
    return HttpClient()

@pytest.fixture()
def test_data(request):
    test_dir = os.path.dirname(request.module.__file__)
    test_data_file = os.path.join(test_dir, "test_data")  # Get test_data.file path.

    with open(test_data_file) as file:
        test_data = dict()
        if request.module.name == 'test_connection_to_site_rabota_by':  # Get test_data for your particular test by test name.
            test_data['headers'] = yaml.load(file, Loader=yaml.FullLoader)['general']
            test_data['url'] = yaml.load(file, Loader=yaml.FullLoader)['test_connection_to_site_rabota_by']
        elif request.module.name == "test_searched_word_not_exict_in_rabota_by_site":
            test_data['headers'] = yaml.load(file, Loader=yaml.FullLoader)['general']
            test_data['url'] = yaml.load(
                file, Loader=yaml.FullLoader)['test_searched_word_not_exict_in_rabota_by_site']['url']
    return test_data

@pytest.fixture()
def connection_test_result(http_client, test_data):
    url = test_data['url']
    headers = test_data['headers']
    responce_connection = http_client.get_request(url, headers)
    return responce_connection.status_code == codes.ok

@pytest.fixture()
def searched_word_not_in_rabota_by_site(http_client, test_data):
    headers = test_data['headers']
    url = test_data['url']
    responce = http_client.get_request(url, headers)
    soup = BeautifulSoup(responce.text, 'html5lib')
    searching_result_text = soup.find('h1', class_='bloko-header-section-3').text
    return searching_result_text == 'По запросу «shotgun» ничего не найдено'

