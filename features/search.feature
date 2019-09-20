Feature: search

    Scenario: Search
        Given I load the website
        When I search for "selenium"
        Then I should see "https://www.seleniumhq.org/" in the results
