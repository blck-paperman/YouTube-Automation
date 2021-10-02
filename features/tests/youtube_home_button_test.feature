# Created by Trofim Martynchuk at 10/2/2021
Feature: Test YouTube "Home" button

  Scenario: Check "Home" button on the main page
    Given Open Explore YouTube page
    When Click "Home" button
    Then Verify "Home" button working