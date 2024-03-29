from selenium import webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')
# 点击打开新窗口的链接
link = wd.find_element_by_tag_name("a")
link.click()
# mainWindow变量保存当前窗口的句柄
mainWindow = wd.current_window_handle
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break
print(wd.title)
wd.switch_to.window(mainWindow)
print(wd.title)