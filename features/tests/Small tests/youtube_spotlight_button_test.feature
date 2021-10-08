# Created by Trofim Martynchuk at 10/8/2021
Feature: Check "Spotlight" button


  Scenario: Check "Spotlight" button on the main page
    Given Open YouTube page
    When Click "Spotlight" button on left side
    Then Verify "Spotlight" button worked