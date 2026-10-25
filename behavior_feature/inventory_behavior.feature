Feature: inventory management
  Manage items in character inventory

  Background:
    Given the inventory contains 3 items

  Scenario: Use a potion
    When the character uses the potion
    Then 2 items should remain in the inventory

  Scenario: Find a treasure
    When the character finds a gem
    And the character adds it to the inventory
    Then 4 items should remain in the inventory