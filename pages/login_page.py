from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    #定位器
    #账号输入框
    USERNAME_INPUT = (By.ID, "normal_login_account")
    #密码输入框
    PASSWORD_INPUT = (By.ID, "normal_login_password")
    #验证码输入框
    CODE_INPUT = (By.ID, "normal_login_code")
    #登录按钮
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#normal_login > div:nth-child(4) > div > div > div > div > button")
    #切换邮箱登录按钮
    EMAIL_LOGIN_BUTTON = (By.XPATH,'//*[@id="normal_login"]/div[5]/div/div/div/div/div[2]/span')
    #账号错误提示
    ERROR_USERNAME_TIP = (By.XPATH,'//*[@id="normal_login_account_help"]/div')
    #密码错误提示
    ERROR_PASSWORD_TIP = (By.XPATH,'//*[@id="normal_login_password_help"]/div')
    #验证码错误提示
    ERROR_CODE_TIP = (By.XPATH,'//*[@id="normal_login_code_help"]/div')
  
    
    
    def __init__(self,driver):
      super().__init__(driver)
      self.logger.info("初始化登录页面")
    def open(self):
      self.driver.get("https://admin-quickvo.devplay.cc/login")
      return self

    #输入账号并验证
    def enter_username(self, username: str, expected_error: str = None) -> None:
      self.enter_text(self.USERNAME_INPUT, username)
      self.press_tab()
      self.logger.info(f"输入账号：{username}")
      
      time.sleep(0.5)
      
      if expected_error is not None:
          # 等待错误提示出现
          if not self.is_element_visible(self.ERROR_USERNAME_TIP, timeout=3):
              raise AssertionError(f"期望出现错误提示 '{expected_error}'，但实际未出现")
          
          actual_error = self.get_text(self.ERROR_USERNAME_TIP)
          if actual_error != expected_error:
              raise AssertionError(f"账号错误提示信息错误！期望: '{expected_error}'，实际: '{actual_error}'")
          
          self.logger.info(f"账号错误验证通过: {actual_error}")
      else:
          # 验证无错误提示
          if self.is_element_visible(self.ERROR_USERNAME_TIP, timeout=2):
            actual_error = self.get_text(self.ERROR_USERNAME_TIP)
            raise AssertionError(f"期望无错误提示，但实际出现错误: '{actual_error}'")
          else:
              self.logger.info("账号验证通过，无错误提示")    #输入密码并验证
              
    #输入密码并验证     
    def enter_password(self,password:str,expected_error: str = None)->None:
      self.enter_text(self.PASSWORD_INPUT, password)
      self.press_tab()
      self.logger.info(f"输入密码：{password}")
      
      time.sleep(0.5)
      
      if expected_error is not None:
          # 等待错误提示出现
          if not self.is_element_visible(self.ERROR_PASSWORD_TIP, timeout=3):
              raise AssertionError(f"期望出现错误提示 '{expected_error}'，但实际未出现")
          
          actual_error = self.get_text(self.ERROR_PASSWORD_TIP)
          if actual_error != expected_error:
              raise AssertionError(f"密码错误提示信息错误！期望: '{expected_error}'，实际: '{actual_error}'")
          
          self.logger.info(f"密码错误验证通过: {actual_error}")
      else:
          # 验证无错误提示
          if self.is_element_visible(self.ERROR_PASSWORD_TIP, timeout=2):
            actual_error = self.get_text(self.ERROR_PASSWORD_TIP)
            raise AssertionError(f"期望无错误提示，但实际出现错误: '{actual_error}'")
          else:
              self.logger.info("密码验证通过，无错误提示")    
    def enter_code(self,code:str,expected_error: str = None)->None:
      self.enter_text(self.CODE_INPUT, code)
      self.press_tab()
      self.logger.info(f"输入验证码：{code}")
      
      time.sleep(0.5)
      
      if expected_error is not None:
          # 等待错误提示出现
          if not self.is_element_visible(self.ERROR_CODE_TIP, timeout=3):
              raise AssertionError(f"期望出现错误提示 '{expected_error}'，但实际未出现")
          
          actual_error = self.get_text(self.ERROR_CODE_TIP)
          if actual_error != expected_error:
              raise AssertionError(f"验证码错误提示信息错误！期望: '{expected_error}'，实际: '{actual_error}'")
          
          self.logger.info(f"验证码错误验证通过: {actual_error}")
      else:
          # 验证无错误提示
          if self.is_element_visible(self.ERROR_CODE_TIP, timeout=2):
            actual_error = self.get_text(self.ERROR_CODE_TIP)
            raise AssertionError(f"期望无错误提示，但实际出现错误: '{actual_error}'")
          else:
              self.logger.info("验证码验证通过，无错误提示")        #点击登录按钮
    def click_login_btn(self)->None:
      self.click(self.LOGIN_BUTTON)
      self.logger.info("点击登录按钮")
    #点击邮箱登录按钮
    def click_email_login_btn(self)->None:
      self.click(self.EMAIL_LOGIN_BUTTON)
      self.logger.info("点击切换邮箱登录按钮")
    #登录
    def login(self,username:str,password:str,code:str,expect_error_username:str=None,expect_error_password:str=None,expect_error_code:str=None)->None:
      self.logger.info(f"开始登录流程，用户名: {username}")
      self.enter_username(username,expect_error_username)
      self.enter_password(password,expect_error_password)
      self.enter_code(code,expect_error_code)
      # 只有在所有验证都通过的情况下才点击登录
      if all(error is None for error in [expect_error_username, expect_error_password, expect_error_code]):
          self.click_login_btn()
          self.logger.info("登录按钮已点击")
      else:
          self.logger.info("存在期望的错误验证，跳过点击登录按钮")
      
    
    
    
      
    
    


