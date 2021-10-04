# Created by Trofim Martynchuk at 10/3/2021
Feature: Check "Live" button


  Scenario: Check "Live" button on the main page
    Given Open YouTube page
    When Click "Live" button on left side
    Then Verify "Live" button worked