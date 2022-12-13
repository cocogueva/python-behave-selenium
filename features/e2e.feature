Feature: Saucelabs demo End to end

Background:
    Given The Saucelabs portal is opened
    And Provide the credentials
    When Click on the Login button
    Then Login is successful and inventory is opened
    
Scenario: Buy a few articles from inventory page
    And Add to cart two first elements
    And Go to cart and checkout added items
    And Insert payment information
    When Finish the checkout
    Then You'll get a thanks

Scenario: Logout of the system
    And Click hamburguer menu and click log out link
    Then You'll be out of the system