import allure
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class UserPage(BasePage):



    please_login = (By.XPATH, '//a[@href="#/app/login"]')
    member_center = (By.XPATH, '//a[text()="会员中心"]')
    my_orders = (By.XPATH, '//a[text()="我的订单"]')
    my_favorite = (By.XPATH, '//a[text()="我的收藏"]')
    my_address = (By.XPATH, '//a[text()="我的收货地址"]')
    shopping_cart = (By.XPATH, '//a[@href="#/app/shoppingcart/cart"]')

    btn_register = (By.CSS_SELECTOR, 'a[href="#/app/register"]')
    input_phone = (By.ID, 'jsRegMobile')
    btn_code = (By.ID, 'jsSendCode')
    input_code = (By.ID, 'jsPhoneRegCaptcha')
    input_password = (By.ID, 'jsPhoneRegPwd')
    btn_reg_and_login = (By.ID, 'jsMobileRegBtn')
    user_name = (By.XPATH, '//a[@href="#/app/home/member/userinfo"]')
    label_failed = ()

    label_wrong_code = (By.XPATH, '//p[text()="验证码格式错误"]')
    label_wrong_reg_password = (By.XPATH, '//p[text()="密码格式错误"]')
    label_user_exists = (By.XPATH,'//*[@id="mobile_register_form"]/p[1]')



    def user_exists(self, data):
        with allure.step('跳转到注册界面'):
            self.click(self.btn_register)
        with allure.step("输入已存在的账户名"):
            self.send_keys(self.input_phone, data['mobile'])
        with allure.step('点击发送验证码'):
            self.click(self.btn_code)
        with allure.step('查看是否出现提示'):
            text = self.get_text(self.label_user_exists)
        assert text == '用户已经存在'
