from playwright.sync_api import Page, Playwright, expect

payload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}

class APIUtils:
    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": "shahabsrc@gmail.com", "userPassword": "Mstemp@123"})
        assert response.ok
        print(response.json())
        #get json as dictionary
        responseBody=response.json()
        #get token key value
        return responseBody["token"]

    def createOrder(self, playwright: Playwright):
        token=self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=payload,
                                            headers={"Authorization": token, "Content-Type": "application/json"})
        print(response)
