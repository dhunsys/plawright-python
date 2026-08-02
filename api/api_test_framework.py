import json
import time

import pytest
from playwright.sync_api import Page, Playwright, expect

from api.apiBase import APIUtils
from pathlib import Path

from play_wright.page_objects.dashboard_page import DashboardPage
from play_wright.page_objects.login_page import LoginPage

#set path of json data file
file_path = Path(__file__).parent.parent / "data" / "credential.json"
with open(file_path) as f:
    test_data = json.load(f)
    print(test_data)
    user_credential_list = test_data['user_credentials']  # get list of data of dict and pass one by one to test


#run test 2 time with a data set in json
@pytest.mark.parametrize("user_credential", user_credential_list)
def test_verify_api_create_order_verify_from_ui_data(playwright: Playwright, user_credential):
    #call api to create an oreder
    api_utils = APIUtils()
    order_id = api_utils.create_order1(playwright, user_credential)
    print("Order placed with order_id: ", order_id)
    #verify order in GUI
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(user_credential["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user_credential["userPassword"])
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    # find row where order id exist and click view button in that row
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    page.locator("p[class='tagline']").scroll_into_view_if_needed()
    print("text", page.locator("p[class='tagline']").text_content())
    expect(page.locator("p[class='tagline']")).to_contain_text("Thank you for Shopping With Us")
    browser.close()


def test_bypass_login(playwright: Playwright):
    api = APIUtils()
    token = api.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #inject token to bypass login. token is key and vaue inside {token}
    page.add_init_script(
        f"""localStorage.setItem('token','{token}') """)  #it takes javascript, so tripple quote is for java script
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    #verify Your Orders text
    expect(page.get_by_text("Your Orders")).to_be_visible()


@pytest.mark.parametrize("user_credential", user_credential_list)
def test_verify_api_create_order_verify_from_ui_data_pageobject(playwright: Playwright, user_credential):
    #call api to create an oreder
    api_utils = APIUtils()
    order_id = api_utils.create_order1(playwright, user_credential)
    print("Order placed with order_id: ", order_id)
    #verify order in GUI
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    dashboard_page = login_page.login(user_credential)
    order_history_page = dashboard_page.navigateOrder()
    order_detailsPage = order_history_page.selectOrder(order_id)
    msg = order_detailsPage.verifyOrderMsg()
    assert msg == "Thank you for Shopping With Us"

    #expect(page.locator("p[class='tagline']")).to_contain_text("Thank you for Shopping With Us")
    browser.close()
