from API.Constants.login_constants import Login_Constants
import allure
import pytest
from API.Pages.SignUp_page import SignUp_Page


class Test_Login(SignUp_Page):
    @allure.description('SignUp correctly')
    @pytest.mark.sanity
    def test_SignUp_correctly(self):
        url = Login_Constants.url_login
        data = Login_Constants.valid_email_and_password
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 200)
        SignUp.Assert_Elapsed_time(url, data, 10)

    @allure.description('SignUp when password incorrectly')
    def test_SignUp_with_incorrectly_password(self):
        url = Login_Constants.url_login
        data = Login_Constants.Invalid_password
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 200)
        SignUp.Assert_Elapsed_time(url, data, 10)

    @allure.description('SignUp when email incorrectly')
    def test_SignUp_with_incorrectly_email(self):
        url = Login_Constants.url_login
        data = Login_Constants.Invalid_email
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 200)
        SignUp.Assert_Elapsed_time(url, data, 10)

    @allure.description('SignUp when email & password incorrectly')
    def test_SignUp_with_incorrectly_email_and_password(self):
        url = Login_Constants.url_login
        data = Login_Constants.Invalid_password_and_email
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 200)
        SignUp.Assert_Elapsed_time(url, data, 10)

    @allure.description('SignUp when email & password are null')
    def test_SignUp_with_null_email_and_password(self):
        url = Login_Constants.url_login
        data = {}
        SignUp = SignUp_Page()
        SignUp.Assert_Status_code(url, data, 200)
        SignUp.Assert_Elapsed_time(url, data, 10)
