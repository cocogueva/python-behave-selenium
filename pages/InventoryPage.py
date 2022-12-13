from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    BTN_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BTN_BIKELIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_NUMBER = (By.CLASS_NAME, "shopping_cart_badge")
    BTN_CHECKOUT = (By.ID, "checkout")

    TXT_NAME = (By.ID, "first-name")
    TXT_LAST = (By.ID, "last-name")
    TXT_CODE = (By.ID, "postal-code")
    BTN_CTNUE = (By.ID, "continue")

    #CHK_TITLE = (By.CLASS_NAME, "title")
    BTN_FINISH = (By.ID, "finish")

    THNX_MSG = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def validateTitle(self):
        assert self.get_title() == "Swag Labs"

    def addItemsToCart(self):
        self.click_element(self.BTN_BACKPACK)
        self.click_element(self.BTN_BIKELIGHT)

    def goToCart(self):
        self.click_element(self.CART_LINK)

    def validateCartQuantity(self):
        number = self.get_element_text(self.CART_NUMBER)
        return '2' in number

    def checkoutCart(self):
        self.click_element(self.BTN_CHECKOUT)

    def validateCartUrl(self):
        url = self.driver.current_url
        return '/cart.html' in url

    def fillStepOneInfo(self,fname,lname,pcode):
        self.input_element(self.TXT_NAME, fname)
        self.input_element(self.TXT_LAST, lname)
        self.input_element(self.TXT_CODE, pcode)
        self.click_element(self.BTN_CTNUE)

    def finishCheckout(self):
        self.click_element(self.BTN_FINISH)

    def validateMessage(self):
        msg = self.get_element_text(self.THNX_MSG)
        return 'THANK YOU FOR YOUR ORDER' in msg
