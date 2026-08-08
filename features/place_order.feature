Feature: Basic Addition
  In order to avoid mathematical mistakes
  As a user
  I want to calculate the sum of two numbers

  Scenario Outline: Add various sets of numbers
    Given I have a calculator
    When I add <first_number> and <second_number>
    Then the result should be <sum>

    Examples:
      | first_number | second_number | sum |
      | 5            | 7             | 12  |
      | -2           | 10            | 8   |
      | 0            | 0             | 0   |
      | 15.5         | 2.5           | 18  |