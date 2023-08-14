import time

import allure

from page.user_page import UserPage
from testcases.user_center.conftest import delete_user, get_code
from utils.mysql_util import db
from utils.read import read_yaml


@allure.epic('Project: Meike Market')
@allure.feature('Module: User')
class TestUser:
    @allure.title('Turn to login page(When un-login)')
    def test_go_login(self, driver):
        page = UserPage(driver)
        expected_url = 'http://meikefresh.5istudy.online/#/app/login'

        with allure.step('Please log in'):
            page.click(page.please_login)
        actual_url = page.get_current_url()
        assert actual_url == expected_url

        page.back()
        with allure.step('Click "my orders"'):
            page.move_to_element(page.member_center)
            page.click(page.my_orders)
        actual_url = page.get_current_url()
        assert actual_url == expected_url

        page.back()
        with allure.step('Click "my address"'):
            page.move_to_element(page.member_center)
            page.click(page.my_address)
        actual_url = page.get_current_url()
        assert actual_url == expected_url

        page.back()
        with allure.step("Click 'my favorite'"):
            page.move_to_element(page.member_center)
            page.click(page.my_favorite)
        actual_url = page.get_current_url()
        assert actual_url == expected_url

        page.back()
        with allure.step('Click Shopping Cart'):
            page.click(page.shopping_cart)
            page.switch_to_window()
        actual_url = page.get_current_url()
        assert actual_url == expected_url

    @allure.title('注册账号')
    def test_register(self, driver):
        page = UserPage(driver)
        data = read_yaml()['register_ok']
        with allure.step('Click register botton'):
            page.click(page.btn_register)

        with allure.step('Input username'):
            page.send_keys(page.input_phone, data['mobile'])

        with allure.step('Fetch authentication code'):
            page.click(page.btn_code)
            time.sleep(2)
        with allure.step('获取验证码'):
            # sql = f"SELECT code FROM users_verifycode WHERE mobile ={str(data['mobile'])} ORDER BY id LIMITI 1"
            sql = f"select code from users_verifycode where mobile = {data['mobile']} order by id desc limit 1;"
            code = db.select_db_one(sql)['code']

        with allure.step("输入验证码"):
            page.send_keys(page.input_code, code)

        with allure.step('输入密码'):
            page.send_keys(page.input_password, data['password'])

        with allure.step('点击注册并登录'):
            page.click(page.btn_reg_and_login)

        text = page.get_text(page.user_name)
        assert text == str(data['mobile'])
        time.sleep(3)
        delete_user(str(data['mobile']))

    @allure.title('注册失败')
    def test_register_failed(self, driver):
        page = UserPage(driver)
        data = read_yaml()['register_wrong_code']
        with allure.step('跳转到注册页'):
            page.click(page.btn_register)
        with allure.step('输入用户名'):
            page.send_keys(page.input_phone, data['mobile'])
        with allure.step('获取验证码'):
            page.click(page.btn_code)
            time.sleep(1)
        with allure.step('输入验证码'):
            code = get_code(data['mobile'])
            page.send_keys(page.input_code, f's+{code}')
        with allure.step("输入密码"):
            page.send_keys(page.input_password, data['password'])
        with allure.step("点击注册并登录"):
            page.click(page.btn_reg_and_login)
        with allure.step('定位错误提示'):
            label_text = page.get_text(page.label_wrong_code)
        assert label_text == '验证码格式错误'

    @allure.title("已存在的账户")
    def test_user_exists(self, driver):
        page = UserPage(driver)
        data = read_yaml()['register_ok']
        page.user_exists(data)