from sauce_demo01 import SwagLabs

import pytest

url = "https://www.saucedemo.com/"

sauce_obj1 = SwagLabs(url)


def test_login():
    assert sauce_obj1.login_labs() == True
    print("success :testcase pass")


def test_before_cookie():
    assert sauce_obj1.before_login_cookie() == True
    print("success :Testcase pass")


def test_after_cookie():
    assert sauce_obj1.after_login_cookie() == True
    print("success :Testcase pass")


def test_logout():
    assert sauce_obj1.logout() == True
    print("success :Testcase pass")

