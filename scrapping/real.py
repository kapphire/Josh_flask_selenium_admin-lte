from selenium import webdriver
from xvfbwrapper import Xvfb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException


def real_scrapping():

	display = Xvfb()
	display.start()

	Real = webdriver.Chrome()
	Real.get("http://affiliates.realdealbet.com/")
	Real.find_element_by_name("username").send_keys("id_betfyuk")
	Real.find_element_by_name("password").send_keys("dontfuckwithme")
	pwd = Real.find_element_by_name("password")
	pwd.send_keys(Keys.RETURN)
	Real.implicitly_wait(10)
	window_after = Real.window_handles[1]
	Real.switch_to_window(window_after)
	mtd_valArr = []
	table = Real.find_element(by=By.ID, value = "dashboard_quick_stats")
	mtds_val = table.find_element(by=By.CLASS_NAME, value = "row_light_color")
	for mtd_val in mtds_val.find_elements_by_tag_name("td"):
		mtd_valArr.append(mtd_val.text)
	return mtd_valArr
	Real.close()
	window_before = Real.window_handles[-1]
	Real.switch_to_window(window_before)
	Real.close()

	display.stop()
