from locators.quote_locators import QuoteLocator

class Parser:
    def __init__(self,parent):
        self.parent = parent

    def __repr__(self) -> str:
        return f"<Quote {self.quote} - {self.author} ({self.tag})>"

    @property
    def quote(self):
        return self.parent.find_element_by_css_selector(QuoteLocator.CONTENT).text
    
    @property
    def author(self):
        return self.parent.find_element_by_css_selector(QuoteLocator.AUTHOR).text

    @property
    def tag(self):
        return self.parent.find_element_by_css_selector(QuoteLocator.TAG).text