import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Firefox("path/to/firefoxdriver")
browser.get("https://facebook.com/login")

browser.quit()
