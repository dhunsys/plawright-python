from play_wright.page_objects.order_details_page import OrderDetailsPage


class OrdersHistoryPage:
    def __init__(self, page):
        self.page = page
    #click view button against given order in list
    def selectOrder(self,orderId):
        # find row where order id exist and click view button in that row
        row = self.page.locator("tr").filter(has_text=orderId)
        row.get_by_role("button", name="View").click()
        #once click takes to order detail page
        order_details_page=OrderDetailsPage(self.page)
        return order_details_page
