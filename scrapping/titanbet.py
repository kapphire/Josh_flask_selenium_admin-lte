from selenium import webdriver
from xvfbwrapper import Xvfb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException


def titan_scrapping():
	
	display = Xvfb()
	display.start()

	Titanbet = webdriver.Chrome()
	Titanbet.get("https://www.europartners.com/")
	Titanbet.find_element_by_xpath("//*[@id='wrapper']/header/section/nav/ul/li[1]/a/span").click()
	Titanbet.implicitly_wait(10)
	Titanbet.find_element_by_id("userName").send_keys("betfyuk")
	Titanbet.find_element_by_id("password").send_keys("qwerty123")
	pwd = Titanbet.find_element_by_id("password")
	pwd.send_keys(Keys.RETURN)
	Titanbet.implicitly_wait(10)
	commission = Titanbet.find_element_by_xpath("//*[@id='separateConv']/div[1]/div[2]").text
	return commission
	print("#########################")
	Titanbet.close()

	display.stop()