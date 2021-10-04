# Created by Trofim Martynchuk at 10/3/2021
Feature: Check "Sports" button


  Scenario: Check "Sports" button on the main page
    Given Open YouTube page
    When Click "Sports" button on left side
    Then Verify "Sports" button worked