def test_connection_to_site_rabota_by(connection_test_result):
    """
    Checks the connection to https://rabota.by website. Will fail when there is no connection.
    """
    expected_result = True
    assert expected_result == connection_test_result, "There is no connection to https://rabota.by"


def test_searched_word_not_exist_in_rabota_by_site(searched_word_not_in_rabota_by_site):
    """
    Test to check if searched word not consists in the https://rabota.by website.
    This test will fail if searched word consists in the above website.
    """
    expected_result = True
    assert expected_result == searched_word_not_in_rabota_by_site, "The website contains searched word"
