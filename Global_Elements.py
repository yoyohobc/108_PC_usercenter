
#登入頁面
#還沒有帳號
go_register = browser.find_element_by_xpath('//*[@id="supplementSubmi"]/div[4]/a[1]')

#註冊頁面
register_phone = browser.find_element_by_id('accountNumber')

register_password = browser.find_element_by_id('thPassword')

register_Verification = browser.find_element_by_id('msgCode')

register_submit_button = browser.find_element_by_id('subAll')
