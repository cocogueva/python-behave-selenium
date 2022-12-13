from behave import *
from selenium import webdriver
from configuration.config import TestData
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
import traceback

@given(u'The Saucelabs portal is opened')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)

    try:
        context.driver.get(TestData.URL)
        context.loginPage = LoginPage(context.driver)
        context.inventoryPage = InventoryPage(context.driver)
    except:
        context.driver.close()
        assert False,"Test is failed in open login page section"

@given(u'Provide the credentials')
def enter_login_creds(context):
    try:
        context.loginPage.enter_login_credentials(TestData.USERNAME, TestData.PASSWORD)
    except Exception: 
        traceback.print_exc()
        context.driver.close()
        assert False, "Test is failed in enter login credentials"

@when(u'Click on the Login button')
def enter_login(context):
    try:
        context.loginPage.enter_login()
    except:
        context.driver.close()
        assert False, "Test is failed in enter login"

@then(u'Login is successful and inventory is opened')
def validate_dashboard_page(context):
    try:
        context.inventoryPage.validateTitle()
    except:
        context.driver.close()
        assert False, "Test is failed in validate invetory page title"

@then(u'Add to cart two first elements')
def fill_cart(context):
    try:
        context.inventoryPage.addItemsToCart()
        assert context.inventoryPage.validateCartQuantity()
    except Exception: 
        traceback.print_exc()
        context.driver.close()
        assert False, "Test is failed in adding items to the cart"