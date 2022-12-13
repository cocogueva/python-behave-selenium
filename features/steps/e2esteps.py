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
    except:
        context.driver.close()
        assert False, "Test is failed in adding items to the cart"

@then(u'Go to cart and checkout added items')
def checkout_cart(context):
    try:
        context.inventoryPage.goToCart()
        assert context.inventoryPage.validateCartUrl()
        context.inventoryPage.checkoutCart()
    except:
        context.driver.close()
        assert False, "Test is failed checking out items in the cart"

@then(u'Insert payment information')
def checkout_step_one(context):
    try:
        context.inventoryPage.fillStepOneInfo('Jorge', 'Guevara', '15036')
    except:
        context.driver.close()
        assert False, "Test is failed checking filling step one"

@when(u'Finish the checkout')
def finish_checkout(context):
    try:
        context.inventoryPage.finishCheckout()
    except:
        context.driver.close()
        assert False, "Test is failed almost at the end"

@then(u'You\'ll get a thanks')
def thanks(context):
    assert context.inventoryPage.validateMessage()
    
@then(u'Click hamburguer menu and click log out link')
def do_logout(context):
    context.loginPage.log_out()


@then(u'You\'ll be out of the system')
def step_impl(context):
    pass
