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

def getJobLinks(page):
	links = []
	for link in page.find_all('a'):
		url = link.get('href')
		if url:
			if '/jobs' in url:
				links.append(url)
	return links

def getID(url):
	pUrl = urlparse.urlparse(url)
	return urlparse.parse_qs(pUrl.query)['id'][0]

def ViewBot(browser):
	visited = {}
	pList = []
	count = 0
	while True:
		time.sleep(random.uniform(3.5,6.9))
		page = BeautifulSoup(browser.page_source)
		people = getPeopleLinks(page)
		if people:
			for person in people:
				ID = getID(person)
				if ID not in visited:
					pList.append(person)
					visited[ID] = '1'
		
		if pList:
			person = pList.pop()
			browser.get(person)
			count += 1
		else:
			jobs = getJobLinks(page)
			if jobs:
				job = random.choice(jobs)
				root = 'http://www.linkedin.com'
				roots = 'http://www.linkedin.com'
				if root not in job or roots not in job:
					job = 'https://www.linkedin.com'+job
				browser.get(Job)
			else:
				print("[-] I'm lost. Exiting")
				break

		print("[+] "+browser.title+" visited. " + str(count) + " visited. " + str(length(pList)) + " to visit.")


parser = argparse.ArgumentParser()
parser.add_argument("email", help = "LinkedIn email")
parser.add_argument("password", help = "LinkedIn password")
args = parser.parse_args()
browser = webdriver.Firefox()
browser.get("https://google.com")
print("Hello here")
emailElement = browser.find_element_by_ID("session-key_login")
emailElement.send_keys(args.email)
passElement = broswer.find_element_by_ID("session-password_login")
passElement.send_keys(args.password)
passElement.submit()
os.system('clear')
print("[+] Success. Logged in.")
ViewBot(browser)
browser.close()

