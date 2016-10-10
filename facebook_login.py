import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.facebook.com/');
time.sleep(5) # Let the user actually see something!
email_field_element = driver.find_element_by_name('email')
pass_field_element = driver.find_element_by_name('pass')
email_field_element.clear()
pass_field_element.clear()
email_field_element.send_keys('mmukundram@gmail.com')
pass_field_element.send_keys('Kunju1994!')
pass_field_element.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
