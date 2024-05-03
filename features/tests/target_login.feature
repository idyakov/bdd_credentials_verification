Feature: Test Scenarios for Login Target step

#  Scenario: Developer checking the login functionality
#    Given Open Target main page
#    And Target Signin button pressed
#    And Target Signin button popup
#    And Target input credentials
#    And Click sign in user
#    Then Verify the account
#    Given Verify the name
#    Then Verify the URL

   Scenario: Developer checking dropdown functionality
    Given Open Target help page
    And Search for a topic
    And Verify dropdown page is opened

@smoke
  Scenario: Developer checking incorrect credentials input functionality
    Given Open Target main page
    And Target Signin button pressed
    And Target Signin button popup
    And Target input credentials
    And Click sign in user
    And Verification uncorrected credential functionality