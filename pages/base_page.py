from typing import Tuple, Union, List, Optional, Any
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
from utils.logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.short_wait = WebDriverWait(driver, 5)  # 短等待用于快速检查
        self.logger = get_logger(self.__class__.__name__)
        self.action_chains = ActionChains(driver)
    
    def _get_element(self, locator: Tuple[By, str], timeout: int = 30) -> WebElement:
        """内部方法：获取元素，支持重试"""
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"元素未找到: {locator}")
            raise
    
    def _get_clickable_element(self, locator: Tuple[By, str], timeout: int = 30) -> WebElement:
        """内部方法：获取可点击元素"""
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.logger.error(f"元素不可点击: {locator}")
            raise
    
    def click(self, locator: Tuple[By, str], timeout: int = 30, retries: int = 2) -> None:
        """点击元素，支持重试机制"""
        for attempt in range(retries):
            try:
                element = self._get_clickable_element(locator, timeout)
                element.click()
                self.logger.info(f"点击元素: {locator}")
                return
            except (StaleElementReferenceException, TimeoutException) as e:
                if attempt == retries - 1:
                    self.logger.error(f"点击元素失败 after {retries} 尝试: {locator}")
                    raise
                self.logger.warning(f"点击重试 {attempt + 1}/{retries} for {locator}")
                time.sleep(1)
    
    def enter_text(self, locator: Tuple[By, str], text: str, clear: bool = True, timeout: int = 30) -> None:
        """输入文本"""
        try:
            element = self._get_clickable_element(locator, timeout)
            if clear:
                element.clear()
            element.send_keys(text)
            self.logger.info(f"输入文本 '{text}' 到元素: {locator}")
        except Exception as e:
            self.logger.error(f"输入文本失败: {locator}, 错误: {str(e)}")
            raise
    
    def get_text(self, locator: Tuple[By, str], timeout: int = 30) -> str:
        """获取元素文本"""
        try:
            element = self._get_element(locator, timeout)
            text = element.text
            self.logger.info(f"获取文本 '{text}' 从元素: {locator}")
            return text
        except Exception as e:
            self.logger.error(f"获取文本失败: {locator}, 错误: {str(e)}")
            raise
    
    def get_attribute(self, locator: Tuple[By, str], attribute: str, timeout: int = 30) -> str:
        """获取元素属性"""
        try:
            element = self._get_element(locator, timeout)
            value = element.get_attribute(attribute)
            self.logger.info(f"获取属性 '{attribute}'='{value}' 从元素: {locator}")
            return value
        except Exception as e:
            self.logger.error(f"获取属性失败: {locator}, 错误: {str(e)}")
            raise
    
    def is_element_present(self, locator: Tuple[By, str], timeout: int = 5) -> bool:
        """检查元素是否存在"""
        try:
            self.short_wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f"元素存在: {locator}")
            return True
        except TimeoutException:
            self.logger.info(f"元素不存在: {locator}")
            return False
    
    def is_element_visible(self, locator: Tuple[By, str], timeout: int = 5) -> bool:
        """检查元素是否可见"""
        try:
            self.short_wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"元素可见: {locator}")
            return True
        except TimeoutException:
            self.logger.info(f"元素不可见: {locator}")
            return False
    
    def is_element_clickable(self, locator: Tuple[By, str], timeout: int = 5) -> bool:
        """检查元素是否可点击"""
        try:
            self.short_wait.until(EC.element_to_be_clickable(locator))
            self.logger.info(f"元素可点击: {locator}")
            return True
        except TimeoutException:
            self.logger.info(f"元素不可点击: {locator}")
            return False
    
    def wait_for_element_invisible(self, locator: Tuple[By, str], timeout: int = 30) -> bool:
        """等待元素不可见"""
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            self.logger.info(f"元素已不可见: {locator}")
            return True
        except TimeoutException:
            self.logger.error(f"元素仍然可见: {locator}")
            return False
    
    def switch_to_new_window(self, timeout: int = 10) -> None:
        """切换到新窗口"""
        try:
            WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)
            original_window = self.driver.current_window_handle
            
            for window_handle in self.driver.window_handles:
                if window_handle != original_window:
                    self.driver.switch_to.window(window_handle)
                    break
            
            self.logger.info("切换到新窗口成功")
        except Exception as e:
            self.logger.error(f"切换窗口失败: {e}")
            raise
    
    def switch_to_frame(self, locator: Tuple[By, str], timeout: int = 30) -> None:
        """切换到iframe"""
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
            self.logger.info(f"切换到iframe: {locator}")
        except Exception as e:
            self.logger.error(f"切换iframe失败: {locator}, 错误: {str(e)}")
            raise
    
    def switch_to_default_content(self) -> None:
        """切换回默认内容"""
        self.driver.switch_to.default_content()
        self.logger.info("切换回默认内容")
    
    def hover(self, locator: Tuple[By, str], timeout: int = 30) -> None:
        """鼠标悬停"""
        try:
            element = self._get_element(locator, timeout)
            self.action_chains.move_to_element(element).perform()
            self.logger.info(f"鼠标悬停在元素: {locator}")
        except Exception as e:
            self.logger.error(f"鼠标悬停失败: {locator}, 错误: {str(e)}")
            raise
    
    def double_click(self, locator: Tuple[By, str], timeout: int = 30) -> None:
        """双击元素"""
        try:
            element = self._get_element(locator, timeout)
            self.action_chains.double_click(element).perform()
            self.logger.info(f"双击元素: {locator}")
        except Exception as e:
            self.logger.error(f"双击失败: {locator}, 错误: {str(e)}")
            raise
    
    def right_click(self, locator: Tuple[By, str], timeout: int = 30) -> None:
        """右键点击"""
        try:
            element = self._get_element(locator, timeout)
            self.action_chains.context_click(element).perform()
            self.logger.info(f"右键点击元素: {locator}")
        except Exception as e:
            self.logger.error(f"右键点击失败: {locator}, 错误: {str(e)}")
            raise
    
    def drag_and_drop(self, source_locator: Tuple[By, str], target_locator: Tuple[By, str], timeout: int = 30) -> None:
        """拖放元素"""
        try:
            source = self._get_element(source_locator, timeout)
            target = self._get_element(target_locator, timeout)
            self.action_chains.drag_and_drop(source, target).perform()
            self.logger.info(f"拖放元素从 {source_locator} 到 {target_locator}")
        except Exception as e:
            self.logger.error(f"拖放失败, 错误: {str(e)}")
            raise
    
    def select_dropdown_by_value(self, locator: Tuple[By, str], value: str, timeout: int = 30) -> None:
        """通过值选择下拉选项"""
        try:
            element = self._get_element(locator, timeout)
            select = Select(element)
            select.select_by_value(value)
            self.logger.info(f"选择下拉选项值: {value}")
        except Exception as e:
            self.logger.error(f"选择下拉选项失败: {value}, 错误: {str(e)}")
            raise
    
    def select_dropdown_by_visible_text(self, locator: Tuple[By, str], text: str, timeout: int = 30) -> None:
        """通过可见文本选择下拉选项"""
        try:
            element = self._get_element(locator, timeout)
            select = Select(element)
            select.select_by_visible_text(text)
            self.logger.info(f"选择下拉选项文本: {text}")
        except Exception as e:
            self.logger.error(f"选择下拉选项失败: {text}, 错误: {str(e)}")
            raise
    
    def get_all_options(self, locator: Tuple[By, str], timeout: int = 30) -> List[WebElement]:
        """获取下拉选项的所有选项"""
        try:
            element = self._get_element(locator, timeout)
            select = Select(element)
            options = select.options
            self.logger.info(f"获取到 {len(options)} 个下拉选项")
            return options
        except Exception as e:
            self.logger.error(f"获取下拉选项失败, 错误: {str(e)}")
            raise
    
    def take_screenshot(self, filename: str) -> None:
        """截取屏幕截图"""
        try:
            self.driver.save_screenshot(filename)
            self.logger.info(f"屏幕截图已保存: {filename}")
        except Exception as e:
            self.logger.error(f"截图失败: {str(e)}")
            raise
    
    def scroll_to_element(self, locator: Tuple[By, str], timeout: int = 30) -> None:
        """滚动到元素"""
        try:
            element = self._get_element(locator, timeout)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            self.logger.info(f"滚动到元素: {locator}")
        except Exception as e:
            self.logger.error(f"滚动到元素失败: {locator}, 错误: {str(e)}")
            raise
    
    def execute_javascript(self, script: str, *args) -> Any:
        """执行JavaScript"""
        try:
            result = self.driver.execute_script(script, *args)
            self.logger.info(f"执行JavaScript: {script}")
            return result
        except Exception as e:
            self.logger.error(f"执行JavaScript失败: {script}, 错误: {str(e)}")
            raise
    
    def wait_for_page_loaded(self, timeout: int = 30) -> None:
        """等待页面完全加载"""
        try:
            self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            self.logger.info("页面加载完成")
        except TimeoutException:
            self.logger.warning("页面加载超时")
    
    def refresh_page(self) -> None:
        """刷新页面"""
        self.driver.refresh()
        self.logger.info("页面已刷新")
        self.wait_for_page_loaded()
    
    def go_back(self) -> None:
        """返回上一页"""
        self.driver.back()
        self.logger.info("返回上一页")
        self.wait_for_page_loaded()
    
    def go_forward(self) -> None:
        """前进到下一页"""
        self.driver.forward()
        self.logger.info("前进到下一页")
        self.wait_for_page_loaded()
    
    def accept_alert(self, timeout: int = 10) -> None:
        """接受alert"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            self.logger.info("Alert已接受")
        except Exception as e:
            self.logger.error(f"处理alert失败: {str(e)}")
            raise
    
    def dismiss_alert(self, timeout: int = 10) -> None:
        """取消alert"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.dismiss()
            self.logger.info("Alert已取消")
        except Exception as e:
            self.logger.error(f"处理alert失败: {str(e)}")
            raise
    
    def get_alert_text(self, timeout: int = 10) -> str:
        """获取alert文本"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            self.logger.info(f"获取到alert文本: {text}")
            return text
        except Exception as e:
            self.logger.error(f"获取alert文本失败: {str(e)}")
            raise
    def press_tab(self) -> None:
        """按下Tab键（推荐使用）"""
        try:
            from selenium.webdriver.common.keys import Keys
            self.action_chains.send_keys(Keys.TAB).perform()
            self.logger.info("按下Tab键")
            time.sleep(0.2)  # 短暂等待焦点切换完成
        except Exception as e:
            self.logger.error(f"按下Tab键失败: {str(e)}")
            raise