import allure
import requests


class Login_Page:

    @allure.description('Login correctly')
    @allure.step("test status code need to be 200")
    def Assert_Status_code(self,URL,DATA,Status_Code):
        Req = requests.post(URL,json=DATA)
        assert Req.status_code == Status_Code

    @allure.step("the time elapse for the test takes < given seconds")
    def Assert_Elapsed_time(self,URL,DATA,Second):
        Req = requests.post(URL,json=DATA)
        assert Req.elapsed.total_seconds() < Second

