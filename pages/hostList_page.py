from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class HostlistPage(BasePage):
    #定位器
    Addhost_BUTTON = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-head > div > div.ant-card-extra > button')
    #第一行数据的编辑按钮
    Edit1_BUTTON = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first.ant-table-cell-ellipsis > span > div > div:nth-child(1) > a')
    #第一行数据的直播配置
    Liveconfig1_BUTTON = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first.ant-table-cell-ellipsis > span > div > div:nth-child(2) > a')
    #第一行数据的域名管理
    DomainM_BUTTON = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first.ant-table-cell-ellipsis > span > div > div:nth-child(3) > a')
    #第一行数据的SDK授权
    SdkAuth_BUTTON = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td.ant-table-cell.ant-table-cell-fix-right.ant-table-cell-fix-right-first.ant-table-cell-ellipsis > span > div > div:nth-child(4) > a')
    #第一行数据的主体名名称
    Hostname1= (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > span')
    #第一行数据的主体账号
    Hostusername = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(3)')
    #邮箱
    Email1 = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4)')
    #主体类型
    HostType1 = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(5) > span')
    #账号来源
    AccountO1 = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(6) > span')
    #主体状态
    Hoststatus1 = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(7) > button > span')
    #备注
    Comment1 = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > div')
    #创建/注册时间
    CreateT1 = (By.CSS_SELECTOR,'#\/openusers\/list > div.ant-card.ant-card-bordered.mt-4.css-rsbjee > div.ant-card-body > div > div > div > div > div > div > table > tbody > tr:nth-child(2) > td:nth-child(9)')
    
    def __init__(self,driver):
      super().__init__(driver)
      self.logger.info("初始化登录页面")
    def open(self):
      self.driver.get('https://admin-quickvo.devplay.cc')
      js_script = """
                  localStorage.setItem('authToken', 'quickvo.eyJpZCI6IjM4QUM5MUQ0QTgyRDk2NkZBRTUwNjE4OTkxRUIxNDZQIiwiZXhwIjoxNzU2OTUxMjYyNDg3fQ.1YSeTLOFXMsFrEanPmzXwWse8CsYxuxkundbMjnKgEw');
                  """ 
      self.driver.execute_script(js_script)
      self.driver.get('https://admin-quickvo.devplay.cc/openusers/list')
      return self
    def AddHost(self):
      self.click(self.Addhost_BUTTON)
      
