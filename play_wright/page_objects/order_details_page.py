class OrderDetailsPage:
    def __init__(self, page):
        self.page = page
    def verifyOrderMsg(self):
        # find row where order id exist and click view button in that row
        self.page.locator("p[class='tagline']").scroll_into_view_if_needed()
        print("text", self.page.locator("p[class='tagline']").text_content())
        return self.page.locator("p[class='tagline']").text_content()
