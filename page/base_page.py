from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utils.log import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)


    def find_element(self, locator, conditon = 'visibility', retry = 1):
        for time in range(retry + 1):
            try:
                logger.info(f'Locationg the element {locator}')
                if conditon == 'visibility':
                    node  = self.wait.until(EC.visibility_of_element_located(locator))
                else:
                    node = self.wait.until(EC.presence_of_element_located(locator))
                return node
            except Exception as e:
                error_info = f'{locator} fails to locate, error info: {e}'
                logger.error(error_info)
                if time < retry:
                    logger.info(f'Re-locationg the location, current time: {time + 1}')
                else:
                    raise Exception(error_info)


    def send_keys(self, locator, text, enter = False):
        node = self.find_element(locator)
        node.clear()
        node.send_keys(text)
        logger.info(f'The input text is: {text}')
        if enter:
            node.send_keys(Keys.ENTER)

    def click(self, locator):
        node = self.find_element(locator)
        node.click()
        logger.info(f'Click the button: {locator}')


    def get_url(self, url = ''):
        self.driver.get(url)
        logger.indo(f'Open the url: {url}')

    def close_driver(self):
        self.driver.close()
        logger.info(f'Close the brower')

    def quit_driver(self):
        self.driver.quit()
        logger.info(f'Quit the brower')

    def refresh(self):
        self.driver.refresh()
        logger.info('Refresh the page')

    def switch_to_window(self, to_parent_window=False):
        total = self.driver.window_handles
        if to_parent_window:
            self.driver.switch_to.window(total[0])
        else:
            for window in total:
                if window != self.driver.current_window_handle:
                    self.driver.switch_to.window(window)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source

    def get_text(self, locator):
        node = self.find_element(locator)
        text = node.text
        if text == "":
            text = text.accessible_name
        logger.info(f'Text of the element is: {text}')
        return text

    def move_to_element(self, locator):
        node = self.find_element(locator)
        self.action.move_to_element(node).perform()
        logger.info(f'Mouse is locating at {locator}')

    def drag_and_drop(self, locator_start, locator_end):
        start = self.find_element(locator_start)
        end = self.find_element(locator_end)
        self.action.drag_and_drop(start, end).perform()
        logger.info(f'Mouse is moving from {locator_start} to {locator_end}')

    def drag_and_drop_by_offset(self, locator, x, y):
        node = self.find_element(locator)
        self.action.drag_and_drop_by_offset(node, x, y)
        logger.info(f"Moving ~~~")

    def select_by_index(self, locator, index):
        node = self.find_element(locator)
        select = Select(node)
        select.select_by_index(index)

    def select_by_value(self, locator, value):
        node = self.find_element(locator)
        select = Select(node)
        select.select_by_value(value)

    def select_by_visible_text(self, locator, visible_text):
        node = self.find_element(locator)
        select = Select(node)
        select.select_by_visible_text(visible_text)

    def back(self):
        self.driver.back()