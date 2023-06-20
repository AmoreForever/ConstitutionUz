import requests
import re
from bs4 import BeautifulSoup


class Constitution:
    ALLOWED_LANGUAGES = ["oz", "uz", "ru", "en"]

    def __init__(self, language: str):  
        """
        Initialize Constitution class.

        Params:
            language (str): Language of the Constitution. Supported languages: "oz", "uz", "ru", "en".

        """
        if language in self.ALLOWED_LANGUAGES:
            self.language = language
        else:
            raise ValueError("Unsupported language.")

    def search_constitution_by_keywords(self, keyword):
        """Поиск статьи по ключевому слову."""
        url = f"https://constitution.uz/{self.language}/clause/index"
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        found_elements = soup.find_all(
            "p",
            string=lambda text: text
            and re.search(r"\b{}\b".format(keyword), text, re.IGNORECASE),
        )
        if found_elements:
            for element in found_elements:
                article_number = element.find_previous(
                    "p", class_="miniTitle"
                ).text.split(".")[0]
                article_text = element.text
                return f"{article_number}: {article_text}"
        else:
            if self.language == "uz":
                return "Izlash natijasi topilmadi."
            elif self.language == "oz":
                return "Излаш натижаси топилмади."
            elif self.language == "ru":
                return "Поиск не дал результатов."
            elif self.language == "en":
                return "Search yielded no results."

    def search_constitution_by_chapter(self, chapter_number: int):
        """Поиск главы по номеру."""
        url = f"https://constitution.uz/{self.language}/clause"
        response = requests.get(url)
        if response.status_code != 200:
            if self.language == "uz":
                return "Sayt bilan bog'lanishda xatolik yuz berdi."
            elif self.language == "oz":
                return "Сайт билан боғланишда хатолик юз берди."
            elif self.language == "ru":
                return "Ошибка при подключении к сайту."
            elif self.language == "en":
                return "Error connecting to the site."

        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        section_id = f"item{chapter_number}"
        return (
            section.get_text(strip=True)
            if (section := soup.find("section", {"id": section_id}))
            else f"Chapter {chapter_number} not found."
        )
