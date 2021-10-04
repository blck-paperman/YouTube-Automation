# Created by Trofim Martynchuk at 10/3/2021
Feature: Check "Learning" button


  Scenario: Check "Learning" button on the main page
    Given Open YouTube page
    When Click "Learning" button on left side
    Then Verify "Learning" button worked