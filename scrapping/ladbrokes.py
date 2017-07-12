from selenium import webdriver
from xvfbwrapper import Xvfb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException


def ladbrokes_scrapping():

	Ladbrokes = webdriver.PhantomJS()
	Ladbrokes.set_window_size(1120, 550)
	Ladbrokes.get("http://www.ladbrokespartners.com")
	Ladbrokes.find_element_by_class_name("top-login-link").click()
	Ladbrokes.find_element_by_id("loginusername").send_keys("betfyuk")
	Ladbrokes.find_element_by_id("loginPassword").send_keys("WjewEEUV")
	pwd = Ladbrokes.find_element_by_id("loginPassword")
	pwd.send_keys(Keys.RETURN)
	Ladbrokes.implicitly_wait(10)
	currentEaring = Ladbrokes.find_element_by_xpath("//*[@id='separateConv']/div[1]/div[2]").text
	print(currentEaring)
	return currentEaring
	Ladbrokes.close()