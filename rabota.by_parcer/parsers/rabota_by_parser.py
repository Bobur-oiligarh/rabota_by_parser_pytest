"""
The main parsing routine of "https://rabota.by"
"""

from bs4 import BeautifulSoup
import html5lib
from typing import List


class RabotaByParser:
    """
    A main class to parce
    """

    @staticmethod
    def get_vacancies_links(html: str) -> List[str]:
        """
        This method receive a html of page and return all vacancies detail page link
        """
        soup = BeautifulSoup(html, 'html5lib')
        vacancies = soup.findAll("div", class_="vacancy-serp-item vacancy-serp-item_redesigned")

        vacancies_links = []
        for vacancy in vacancies:
            vacancies_links.append(vacancy.find('a', class_='bloko-link').get('href'))
        return vacancies_links

    @staticmethod
    def get_vacancies_pagination_links(url: str, html: str) -> List[str]:
        """
        This method receive a html of page and return list of all pages links through this searching value
        """
        soup = BeautifulSoup(html, 'html5lib')
        total_pages = int(
            soup.find('div', class_='pager').find_all('span', class_='')[-2].text)  # Determine pages count

        page_link = soup.find('div', class_='pager').find('a').get('href') # Get page_link of the 2nd page in pagination
        page_number_index = page_link.find('page') + 5  # Determine an index of "page" to change it value later

        pages_links = list()
        for number in range(total_pages):
            page_url = page_link[:page_number_index] + \
                       str(number) + page_link[page_number_index + 1:]  # Changing page numbers in page_link
            pages_links.append(page_url)
        return pages_links

    @staticmethod
    def get_search_word_occurance_count_in_vacancy_description(search_word: str, html: str):
        """
        This method receive a html of page and return a number of occurance this word in each detail pages
        """
        search_word_count = 0
        soup = BeautifulSoup(html, 'html5lib')
        searching_elements = soup.find('div', class_='vacancy-description').text.split()
        for searching_element in searching_elements:
            if search_word in searching_element.lower():
                search_word_count += 1
        return search_word_count

    @staticmethod
    def get_header_of_page_with_searched_word(html: str) -> str:
        """Receives a html of page and returns text of header tag, if this tag is available

        """
        soup = BeautifulSoup(html, 'html5lib')
        searching_result_text = soup.find('h1', class_='bloko-header-section-3').text
        return searching_result_text


