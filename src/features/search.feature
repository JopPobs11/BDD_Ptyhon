@feature_search
Feature: Search Feature

@scenario_search_pertama
Scenario: Success get item search
    Given I am on the home Page
    When I click Search Bar
    And I fill laptop asus
    Then I will see list of laptop asus

@scenario_login
Scenario: Success login to home page
    Given I am on login page
    When I fill email with valid credential
    And I click selanjutnya
    And I fill password with valid credential
    Then I will direct to home page 