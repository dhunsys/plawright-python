import time

from playwright.sync_api import Page, Playwright, expect

from api.apiBase import APIUtils


def test_verify_api_create_order_verify_from_ui(playwright: Playwright):
    #call api to create an oreder
    api_utils = APIUtils()
    order_id=api_utils.createOrder(playwright)
    print("Order placed with order_id: ",order_id)
    #verify order in GUI
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("shahabsrc@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Mstemp@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    # find row where order id exist and click view button in that row
    row=page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    page.locator("p[class='tagline']").scroll_into_view_if_needed()
    print("text",page.locator("p[class='tagline']").text_content())
    expect(page.locator("p[class='tagline']")).to_contain_text("Thank you for Shopping With Us")
    browser.close()

def test_bypass_login(playwright:Playwright):
    api=APIUtils()
    token=api.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #inject token to bypass login. token is key and vaue inside {token}
    page.add_init_script(f"""localStorage.setItem('token','{token}') """)#it takes javascript, so tripple quote is for java script
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    #verify Your Orders text
    expect(page.get_by_text("Your Orders")).to_be_visible()


