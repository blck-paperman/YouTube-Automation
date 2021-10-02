# Created by Trofim Martynchuk at 10/2/2021
Feature: Test YouTube "Explore" button

  Scenario: Check "Explore" button on the main page
    Given Open YouTube page
    When Click "Explore" button
    Then Verify "Explore" button working