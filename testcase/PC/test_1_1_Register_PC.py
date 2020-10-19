import unittest
import time, os
from Parameter import *

class WebDriverTests(unittest.TestCase):
	def setUp(self):
	    # create a new Browser session
	    setUpBrowser(self)
	    time.sleep(1)
	    print(" -- set up finished -- ")

	def tearDown(self):
	    time.sleep(1)
	    self.browser.quit()
	    print('-- tear down finished -- ')


	def test_1_1_Register_PC(self):
		print('==========test_1_1_Register_PC_註冊頁面、各個元素檢查==========')
		browser = self.browser
		browser.get(PC_URL)
		time.sleep(3)
		#登入頁面
		#還沒有帳號
		go_register = browser.find_element_by_xpath('//*[@id="supplementSubmi"]/div[4]/a[1]')

		go_register.click()
		time.sleep(2)

		# 開啟第二個視窗,可操作後台
		'''browser2 = webdriver.Chrome(chrome_options=self.options,desired_capabilities=d)
		browser2.get('https://www.google.com.tw/')
		time.sleep(2)'''
		#註冊頁面
		register_phone = browser.find_element_by_id('accountNumber')

		register_password = browser.find_element_by_id('thPassword')

		register_Verification = browser.find_element_by_id('msgCode')

		register_submit_button = browser.find_element_by_id('subAll')

		elements = [[register_phone,'電話欄'],[register_password,'密碼欄'],
		[register_Verification,'驗證碼欄'],[register_submit_button,'提交真實開戶按鈕']]
		for element in elements:
			try:
				element[0]
				print(element[1],"顯示正確!")
			except NoSuchElementException:
				print(element[1],"顯示錯誤!")
