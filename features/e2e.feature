Feature: Saucelabs demo End to end

Background:
    Given The Saucelabs portal is opened
    And Provide the credentials
    When Click on the Login button
    Then Login is successful and inventory is opened
    
Scenario: Buy a few articles from inventory page
    And Add to cart two first elements
    #And Go to cart and checkout added items
    #And Insert payment information
    #And Finish the checkout
    #Then You'll get a thanks