import time

from playwright.sync_api import Page, Playwright, expect

from api.apiBase import APIUtils


#change the url with order id of another user, verify app is secure to handle such case
def intercepRequest(route):
    #intercept using continure_-> resend request with order id of another user
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6960eae1c941646b7a8b3ed0")


def test_verify_api_intercept_request(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    #monitor any req going to below url, then use an order id of another account and pass it to same url to verify auauthorized access
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercepRequest)
    page.get_by_placeholder("email@example.com").fill("shahabsrc@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Mstemp@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()  # on click, url in route is triggered
    # now it will invoke above url and inturn intercepted, app should check the request is coming from wrong user and give proper error msg
    msg = page.locator(".blink_me").text_content()
    assert msg == 'You are not authorize to view this order'
    print(msg)
    time.sleep(5)
