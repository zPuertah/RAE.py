
from bs4 import BeautifulSoup
import requests


DLE_MAIN_URL = 'https://dle.rae.es/'
Headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

#BRUH i cant use this exception :(
#class InvalidWord(Exception):
#    "This raises if a invalid word or None is given"
#    def __init__(self, message="\n You only can use strings to search words\n Usage: search_word('WORD')"):
#        self.message = message
#        super().__init__(self.message)

class Cilent():
    """
    This is a Client to get access to RAE and initializates the searcher
    Atributes:
    
    headers: Are the headers to get an 200-299 response (optional)
    url: Is the base URI to go to RAE (Provides by module)

    Docs at {link}

    """
    def __init__(self, Headers = Headers):
        self.url = DLE_MAIN_URL
        self.headers = Headers
        
    def search_word(self, Word:str):
        """
        
        This method search a word and returns a dict with the word as the key and the meaning as the value
        like this:
            { word:meaning }

        """


        rae_html = requests.get(f"{self.url}{Word}", headers= self.headers)
        rae_soup = BeautifulSoup(rae_html.text, 'lxml')
        art = rae_soup.find("article")
        word = art.find("header").get_text()
        get_def = art.find('p', class_="j").get_text()
        for i in range(20):
            if str(i) in get_def or "." in get_def:
                get_def = get_def.replace(str(i), "")
                get_def = get_def.replace(".", "")
        r = { word:get_def}
        return r
    def ends_with(self, Word:str):
        """

        This method search a list of words ending in the arg
        like this:
            [word_1, word_2, word_3]

        """
        rae_html = requests.get(f"{self.url}{Word}?m=32", headers= self.headers)
        rae_soup = BeautifulSoup(rae_html.text, 'lxml')
        div = rae_soup.find_all('div', class_="n1")
        Words = [x.find('a').get("data-eti") for x in div]
        return Words
    def starts_with(self, Word:str):
        """

        This method search a list of words starting in the arg
        like this:
            [word_1, word_2, word_3]

        """
        rae_html = requests.get(f"{self.url}{Word}?m=31", headers= self.headers)
        rae_soup = BeautifulSoup(rae_html.text, 'lxml')
        div = rae_soup.find_all('div', class_="n1")
        Words = [x.find('a').get("data-eti") for x in div]
        return Words
    def contains(self, Word:str):
        """

        This method search a list of words containing the arg
        like this:
            [word_1, word_2, word_3]

        """
        rae_html = requests.get(f"{self.url}{Word}?m=33", headers= self.headers)
        rae_soup = BeautifulSoup(rae_html.text, 'lxml')
        div = rae_soup.find_all('div', class_="n1")
        Words = [x.find('a').get("data-eti") for x in div]
        return Words