def test_connection_to_site_rabota_by(connection_test_result):
    expected_result = True
    assert expected_result == connection_test_result, "There is no connection to https://rabota.by"


def test_searched_word_not_exist_in_rabota_by_site(searched_word_not_in_rabota_by_site):
    expected_result = True
    assert expected_result == searched_word_not_in_rabota_by_site, "The website contains searched word"
