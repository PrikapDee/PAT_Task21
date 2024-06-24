from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class SwagLabs:
    # username and password data

    username = "standard_user"
    password = "secret_sauce"
    # file path to create file

    # locators
    username_locator = "user-name"
    password_locator = "password"
    xpath_login = "/html/body/div/div/div[2]/div[1]/div/di""v/form/input"
    xpath_content = "/html/body"
    open_menu = "//button[@id='react-burger-menu-btn']"
    logout_button = "//a[@id='logout_sidebar_link']"

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # method to fetch ur of webpage
    def fetch_url(self):
        if self.login_labs():
            sleep(5)
            return self.driver.current_url
        else:
            print("error in fetching the url")
            return False

    # login method to log in to application
    def login_labs(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)
            self.driver.find_element(by=By.ID, value=self.username_locator).send_keys(self.username)
            self.driver.find_element(by=By.ID, value=self.password_locator).send_keys(self.password)
            self.driver.find_element(by=By.XPATH, value=self.xpath_login).click()
            sleep(3)
            return True

        except:
            print("error")
            return False

    def before_login_cookie(self):
        try:
            self.driver.get(self.url)
            cookie = self.driver.get_cookies()
            print("Before login cookie :", cookie)
            return True

        except:
            print("error in catching cookies")
            return False

    def after_login_cookie(self):
        try:
            self.login_labs()
            cookie = self.driver.get_cookies()
            print("after login cookie :", cookie)
            return True

        except:
            print("error in catching cookies")
            return False

    def logout(self):
        try:
            self.login_labs()
            sleep(4)
            self.driver.find_element(by=By.XPATH, value=self.open_menu).click()
            sleep(2)
            self.driver.find_element(by=By.XPATH, value=self.logout_button).click()
            print("log out")
            return True

        except:
            print("error in logout")
            return False
