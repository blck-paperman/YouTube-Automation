# Created by Trofim Martynchuk at 10/3/2021
Feature: Check "News" button


  Scenario: Check "News" button on the main page
    Given Open YouTube page
    When Click "News" button on left side
    Then Verify "News" button worked