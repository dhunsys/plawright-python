from play_wright.page_objects.order_history_page import OrdersHistoryPage


class DashboardPage:
    def __init__(self, page):
        self.page = page
    def navigateOrder(self):
        self.page.get_by_role("button", name="ORDERS").click()
        #once click is successfull it takes to order history page
        order_history_page=OrdersHistoryPage(self.page)
        return order_history_page;