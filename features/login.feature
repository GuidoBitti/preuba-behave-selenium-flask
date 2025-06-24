Feature: Login functionality

  Scenario: Successful login
    Given the user is on the login page
    When the user enters username "admin" and password "1234"
    Then the user should be redirected to the dashboard
