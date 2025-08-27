from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class DriverManager:
    # 类变量定义驱动路径（两种方式任选其一）
    EDGE_PATH = r"D:\U\UItest-3\msedgedriver.exe"  # 方式1：手动指定路径
    USE_AUTO_MANAGER = False  # 方式2：设置为True则自动管理驱动

    @staticmethod
    def get_driver(browser='edge'):
        if browser == 'edge':
            if DriverManager.USE_AUTO_MANAGER:
                # 方式1：自动下载管理驱动（推荐）
                service = EdgeService(EdgeChromiumDriverManager().install())
            else:
                # 方式2：使用手动指定的驱动路径
                service = EdgeService(executable_path=DriverManager.EDGE_PATH)
            
            driver = webdriver.Edge(service=service)
            return driver