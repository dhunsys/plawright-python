import time

from playwright.sync_api import Page, Playwright, expect

from api.apiBase import APIUtils

fake_response = {"data": [],
                 "message": "No orders"}  #This is response from server when there is no order in system. Make it same as server


#Browser login->click order->server->response->intercept->response->browser->verify response using play_wright
def intercept_response(route):
    route.fulfill(
        json=fake_response
    )  #give my response instead of server


def test_verify_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #use API
    api = APIUtils()
    orderiId = api.createOrder(playwright)
    print("order id", orderiId)
    # now use GUI to check order is is placed in order page. Next is play_wright
    # page.goto("https://testingsrc.blogspot.com/")
    # # get frame
    # page.locator("#menuItem").hover()
    # # takes time to show submenu so put wait
    # expect(page.locator("#submenu")).to_be_visible(timeout=5000)
    # page.close()


#I want to send fabricated response instead of real response from server
#Lets say there are many orders in system, if we view it will give all orders in response
#But I want even there are orders in system, I don't want to delete all still i want to send response as no orders found
def test_verify_api_intercept_response(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    #monitor traffic on below url, and use an order id of another account and pass it to same url to verify auauthorized access
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("shahabsrc@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Mstemp@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()  #invoke route url
    #above line will send fake response, based on that response client will create a page and show in browser so check that now
    msg = page.locator(".mt-4").text_content()
    print(msg)
    assert msg == " You have No Orders to show at this time. Please Visit Back Us "
    time.sleep(5)
