from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.quote_page_locators import QuotePageLocators
from selenium.webdriver.support.ui import Select
from parser.parser import Parser
from selenium.webdriver.common.by import By

class Page:
    def __init__(self,page):
        self.page = page

    @property
    def author_list(self):
        authors = " | ".join([i.text for i in self.page.find_elements_by_css_selector(QuotePageLocators.AUTHORS)][1:])
        return authors

    @property
    def author_dropdown(self):
        return Select(self.page.find_element_by_css_selector(QuotePageLocators.AUTHOR_DROPDOWN))
    
    @property
    def tag_list(self):
        tags = " | ".join(([i.text for i in self.page.find_elements_by_css_selector(QuotePageLocators.TAGS)][1:]))
        return tags

    @property
    def tag_dropdown(self):
        return Select(self.page.find_element_by_css_selector(QuotePageLocators.TAG_DROPDOWN))

    @property
    def search_button(self):
        return (self.page.find_element_by_css_selector(QuotePageLocators.SEARCH_BUTTON))

    @property
    def quote(self):
        return Parser(self.page.find_element_by_css_selector(QuotePageLocators.QUOTE))
    
    
    def select_author(self):
        while True:
            author_name = input("Please enter the author name you would like to quote from:\n" + self.author_list + "\n-->")
            try:
                self.author_dropdown.select_by_visible_text(author_name)
                break
            except:
                print("No Such Author! Please check your spelling!")

    def select_tag(self):
        while True:
            tag = input("Please select the tag of quote that you like to view:\n" + self.tag_list + "\n-->")
            try:
                self.tag_dropdown.select_by_visible_text(tag)
                break
            except:
                print("No Such Tag! Please check your spelling!")

    def search_quote(self):
        self.select_author()
        WebDriverWait(self.page,10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR,QuotePageLocators.TAGS_VALUE_OPTION)
            )
        )
        self.select_tag()
        self.search_button.click()
        print(self.quote)

    
    



    
    
    