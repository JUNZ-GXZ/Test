from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')
wd.switch_to.frame(wd.find_element_by_css_selector('[src="sample1.html"]'))
elements = wd.find_elements_by_css_selector('.plant')
for element in elements:
    print("----------------")
    print(element.get_attribute('outerHTML'))
wd.switch_to.default_content()   #跳出frame
wd.find_element_by_id("outerbutton").click()
wd.quit()