"""Fixtures for test_rabota_by_site.

"""
import os
import pytest
from clients.http_client import HttpClient
from requests import codes
import yaml
from typing import Dict, ClassVar
from parsers.rabota_by_parser import RabotaByParser


@pytest.fixture()
def http_client():
    """Makes an instance object of HttpClient.

    """
    return HttpClient()

@pytest.fixture()
def test_data(request) -> Dict[str, str]:
    """Gets and returns dict of datas to tests from test_data.yaml by current test name.

    """
    test_dir = os.path.dirname(request.module.__file__)
    test_data_file_path = os.path.join(test_dir, "test_data.yaml")  # Gets test_data file path.
    current_test_name = request.node.name
    with open(test_data_file_path) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data[current_test_name]

@pytest.fixture()
def connection_test_result(http_client: ClassVar[object], test_data: dict[str, str]) -> bool:
    """Receives an HttpClient object and test_datas, returns comparison - boolean object.

    """
    url = test_data['url']
    headers = test_data['headers']
    responce_connection = http_client.get_request(url, headers)
    return responce_connection.status_code == codes.ok

@pytest.fixture()
def rabota_by_parser():
    """Makes an instance object of RabotaByParser

    """
    return RabotaByParser()

@pytest.fixture()
def searched_word_not_in_rabota_by_site(
        http_client: ClassVar[object], rabota_by_parser: RabotaByParser, test_data: Dict) -> bool:
    """Checks that if the searched word consists in the https://rabota.by site.
Returns True if word in website or False otherwise.

    """
    headers = test_data['headers']
    url = test_data['url']
    word = test_data['word']
    full_url = url + word  # Have build the url of the page with searched word
    responce = http_client.get_request(full_url, headers)
    page_with_searched_word_header_text = rabota_by_parser.get_header_of_page_with_searched_word(responce.text)
    return page_with_searched_word_header_text == f"По запросу «{word}» ничего не найдено"

