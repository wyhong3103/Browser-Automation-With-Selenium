from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
chrome = webdriver.Chrome(executable_path= "C:\\Users\\ACER\\Desktop\\c0ding\\python\\webscraping\\chromedriver.exe", options = options)


