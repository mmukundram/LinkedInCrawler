import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def getPeopleLinks(page):
	links = []
	for link in page.find_all('a'):
		url = link.get('href')
		if url:
			if 'profile/view?id=' in url:
				links.append(url)
	return links

def getID(url):
	pUrl = urlparse.urlparse(url)
	return urlparse.parse_qs(pUrl.query)['id'][0]

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.linkedin.com/uas/login')
time.sleep(5) # Let the user actually see something!
email_field_element = driver.find_element_by_name('session_key')
pass_field_element = driver.find_element_by_name('session_password')
email_field_element.clear()
pass_field_element.clear()
email_field_element.send_keys('ncsulibrarysystem@gmail.com')
pass_field_element.send_keys('ncsu27606')
pass_field_element.submit()
time.sleep(5) # Let the user actually see something!
page = BeautifulSoup(driver.page_source,"html.parser")
people = getPeopleLinks(page)
links = []
IDs = []
fileCount = 0
if people:
	for person in people:
		if person not in links:
			ID = getID(person)
			if ID not in IDs:
				IDs.append(ID)				
				links.append(person)
				driver.get(person)
				page = BeautifulSoup(driver.page_source,"html.parser")
				#print "File count = " + str(fileCount)
				for tag in page.find_all('span'):
					text = tag.get('class')
					if text:
						if 'full-name' in text:
							#print tag.text
							with open("html/"+tag.text+'.html',"w+") as f:
								for line in page.prettify('utf-8','minimal'):
									f.write(str(line))
								f.close()
								fileCount = fileCount + 1
		time.sleep(1)
driver.quit()
