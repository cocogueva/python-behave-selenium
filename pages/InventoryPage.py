from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    BTN_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BTN_BIKELIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_NUMBER = (By.CLASS_NAME, "shopping_cart_badge")

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