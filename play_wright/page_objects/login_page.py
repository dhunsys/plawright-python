from play_wright.page_objects.dashboard_page import DashboardPage


class LoginPage:
    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self,user_credential):
        self.page.get_by_placeholder("email@example.com").fill(user_credential["userEmail"])
        self.page.get_by_placeholder("enter your passsword").fill(user_credential["userPassword"])
        self.page.get_by_role("button", name="Login").click()
        # We know login will take to dashboard page so return dashboard object to avoid object creation
        dashboard_page=DashboardPage(self.page)
        return dashboard_page;