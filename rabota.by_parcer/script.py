from clients.http_client import HttpClient
from parsers.rabota_by_parser import RabotaByParser

rabota_by_url = "https://rabota.by/search/vacancy?clusters=true&area=16&ored_clusters=true&enable_snippets=true&salary=&text=python"
base_url = "https://rabota.by"
default_headers = {"user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "}
http_client = HttpClient()
parser = RabotaByParser()
search_words = ['python', 'linux', 'flask']
output = dict()

if __name__ == '__main__':
    main_page_responce = http_client.get_request(rabota_by_url, headers=default_headers)
    pages_links = parser.get_vacancies_pagination_links(rabota_by_url, main_page_responce.text)

    for page_link in pages_links:
        page_full_url = base_url + page_link  # Building full url for each page that we have
        page_responce = http_client.get_request(page_full_url, headers=default_headers)
        python_vacancies_links = parser.get_vacancies_links(page_responce.text)
        for vacancy_link in python_vacancies_links:
            vacancy_responce = http_client.get_request(vacancy_link, headers=default_headers)
            for search_word in search_words:
                word_occurance_count = parser.get_search_word_occurance_count_in_vacancy_description(
                    search_word, vacancy_responce.text
                )
                if search_word not in output.keys():
                    output[search_word] = word_occurance_count
                else:
                    output[search_word] += word_occurance_count

    print(output)