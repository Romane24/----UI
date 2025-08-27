import pytest
from selenium import webdriver
from utils.driver_manager import DriverManager 
import os
import time
import pytest_html

@pytest.fixture(scope='function' )
def browser():
  # 初始化浏览器
  driver = DriverManager.get_driver()#使用我们自定义的驱动管理
  yield driver
  # 关闭浏览器
  driver.quit()

@pytest.fixture
def login_page(browser):
  from pages.login_page import LoginPage
  page = LoginPage(browser)
  page.open()
  return LoginPage(browser)



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 只在用例失败时截图
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")  # 你的 fixture 名
        if driver:
            screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}_{int(time.time())}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(file_path)
            # 可选：将截图路径写入报告
            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.image(file_path))



