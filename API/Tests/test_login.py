from API.Constants.login_constants import Login_Constants
import allure
import pytest
from API.Pages.login_page import Login_Page


class Test_Login(Login_Page):
    @allure.description('Login correctly')
    @pytest.mark.sanity
    def test_login_correctly(self):
        url = Login_Constants.url_login
        data = Login_Constants.valid_email_and_password
        login = Login_Page()
        login.Assert_Status_code(url, data, 200)
        login.Assert_Elapsed_time(url, data, 10)

    @allure.description('Login when password incorrectly')
    def test_login_with_incorrectly_password(self):
        url = Login_Constants.url_login
        data = Login_Constants.Invalid_password
        login = Login_Page()
        login.Assert_Status_code(url, data, 200)
        login.Assert_Elapsed_time(url, data, 10)

    @allure.description('Login when email incorrectly')
    def test_login_with_incorrectly_email(self):
        url = Login_Constants.url_login
        data = Login_Constants.Invalid_email
        login = Login_Page()
        login.Assert_Status_code(url, data, 200)
        login.Assert_Elapsed_time(url, data, 10)

    @allure.description('Login when email & password incorrectly')
    def test_login_with_incorrectly_email_and_password(self):
        url = Login_Constants.url_login
        data = Login_Constants.Invalid_password_and_email
        login = Login_Page()
        login.Assert_Status_code(url, data, 200)
        login.Assert_Elapsed_time(url, data, 10)

    @allure.description('Login when email & password are null')
    def test_login_with_null_email_and_password(self):
        url = Login_Constants.url_login
        data = {}
        login = Login_Page()
        login.Assert_Status_code(url, data, 200)
        login.Assert_Elapsed_time(url, data, 10)
