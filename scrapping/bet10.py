from selenium import webdriver
from xvfbwrapper import Xvfb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException


def bet10_scrapping():
	bet10 = webdriver.PhantomJS()
	bet10.set_window_size(1120, 550)
	bet10.get("http://partners.10bet.com/")
	bet10.find_element_by_id("username").send_keys("betfyuk")
	bet10.find_element_by_id("password").send_keys("dontfuckwithme")
	pwd = bet10.find_element_by_id("password")
	pwd.send_keys(Keys.RETURN)
	bet10.implicitly_wait(10)
	mtd_valArr = []
	table = bet10.find_element(by=By.ID, value = "dashboard_quick_stats")
	mtds_val = table.find_element(by=By.CLASS_NAME, value = "row_light_color")
	for mtd_val in mtds_val.find_elements_by_tag_name("td"):
		mtd_valArr.append(mtd_val.text)
	return mtd_valArr